#!/usr/bin/env python3
"""
静态网站Markdown爬取工具（小米Vela文档专用优化版）
主要修复：
1. 标题锚点问题（移除多余的#符号）
2. 代码块格式问题（修复空格和语法高亮）
3. 表格对齐问题
4. 整体排版优化
"""

import os
import re
import requests
from bs4 import BeautifulSoup, NavigableString
from urllib.parse import urljoin, urlparse, unquote
from pathlib import Path
import time
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import urllib3
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 禁用SSL警告（可选）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 导入rich库用于美化命令行输出
try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich import print as rprint
    RICH_AVAILABLE = True
except ImportError:
    # 如果rich不可用，回退到普通输出
    RICH_AVAILABLE = False
    console = None
    Progress = None

# ASCII Art for VelaDocs
VELA_ASCII_ART = """
_    __     __         ____                 
| |  / /__  / /___ _   / __ \\____  __________
| | / / _ \\/ / __ \'/  / / / / __ \\/ ___/ ___/
| |/ /  __/ / /_/ /  / /_/ / /_/ / /__(__  ) 
|___/\\___/_/\\__,_/  /_____/\\____/\\___/____/  
                                             
"""

class MarkdownScraper:
    def __init__(self, base_url, output_dir="docs"):
        self.base_url = base_url.rstrip('/')
        self.output_dir = Path(output_dir).resolve()

        # --- 新增逻辑：根据 base_url 确定子目录 ---
        parsed_base = urlparse(self.base_url)
        path_parts = parsed_base.path.strip('/').split('/')
        # 假设语言标识符是 URL 路径的最后一部分，且是 'zh' 或 'en'
        self.subdir = ''
        if path_parts and path_parts[-1] in ['zh', 'en']:
            self.subdir = path_parts[-1]
        # ----------------------------

        # 如果存在子目录，则调整输出路径
        if self.subdir:
            self.output_dir = self.output_dir / self.subdir

        self.visited = set()
        self.asset_map = {}
        self.total_pages = 0
        self.processed_pages = 0

        self.session = requests.Session()
        self.session.trust_env = False
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache'
        })

        # 配置重试策略
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # 确保最终的输出目录存在
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # 初始化rich控制台
        if RICH_AVAILABLE:
            self.console = Console()
        else:
            self.console = None

    def _missing_image_text(self, img_url):
        filename = os.path.basename(urlparse(img_url).path) or "unknown-image"
        if self.subdir == 'en':
            return f"Image missing: {filename} <{img_url}>"
        return f"图片缺失: {filename} <{img_url}>"

    def _build_code_block(self, language, code):
        language = (language or '').strip()
        code = code.replace('\r\n', '\n').replace('\r', '\n').strip('\n')
        fence = f"```{language}".rstrip()
        return f"{fence}\n{code}\n```"

    def _restore_code_blocks(self, markdown, code_blocks):
        for placeholder, code_block in code_blocks:
            markdown = markdown.replace(placeholder, code_block)
        return markdown

    def _normalize_code_block_spacing(self, markdown):
        # 确保代码块起始围栏前有空行，避免与列表或正文挤在同一行
        markdown = re.sub(
            r'([^\n])([ \t]*)```([\w+-]+)\n',
            r'\1\n\n```\3\n',
            markdown
        )

        # 相邻代码块之间强制分隔，避免闭合围栏与下一个起始围栏连在同一行
        markdown = re.sub(
            r'```\s+```([\w+-]+)\n',
            r'```\n\n```\1\n',
            markdown
        )

        markdown = re.sub(
            r'```[ \t]+```',
            '```\n\n```',
            markdown
        )

        # 某些页面在列表中的代码块会把行号或编号粘到闭合围栏后面，形成 ```0 / ```1，
        # 这会导致后续内容被错误地吞进代码块。这里将这类尾缀剥离掉。
        markdown = re.sub(
            r'^([ \t]*)```[0-9]+([ \t]*)$',
            r'\1```\2',
            markdown,
            flags=re.MULTILINE
        )

        # 统一清理围栏行尾多余空格
        markdown = re.sub(r'^```([\w+-]*)[ \t]+$', r'```\1', markdown, flags=re.MULTILINE)
        markdown = re.sub(r'^```[ \t]+$', r'```', markdown, flags=re.MULTILINE)
        return markdown

    def _normalize_table_continuations(self, markdown):
        lines = markdown.split('\n')
        normalized = []
        i = 0

        def is_table_row(line):
            stripped = line.strip()
            return stripped.count('|') >= 3 and not stripped.startswith('```')

        def is_table_separator(line):
            stripped = line.strip().replace(' ', '')
            return bool(re.match(r'^[-:|]+$', stripped))

        while i < len(lines):
            line = lines[i]
            if (
                normalized
                and is_table_row(normalized[-1])
                and not is_table_separator(normalized[-1])
            ):
                stripped = line.strip()
                if stripped and '|' not in stripped and not stripped.startswith('```'):
                    normalized[-1] = f"{normalized[-1]}<br>{stripped}"
                    i += 1
                    continue

            normalized.append(line)
            i += 1

        return '\n'.join(normalized)

    def _get_relative_path(self, url):
        # 计算相对于 base_url 的路径，但不包含 base_url 中的语言部分
        # 例如，如果 base_url 是 https://iot.mi.com/vela/quickapp/zh/    ，url 是 https://iot.mi.com/vela/quickapp/zh/guide/start  
        # 则 path 是 /vela/quickapp/zh/guide/start，base_path 是 /vela/quickapp/zh
        # 结果是 /guide/start，去掉开头的 / 变成 guide/start
        parsed_url = urlparse(url)
        parsed_base = urlparse(self.base_url)
        path = parsed_url.path
        base_path = parsed_base.path
        # 移除 base_path 在 path 中的前缀部分
        rel_path = path.replace(base_path, '', 1).lstrip('/')
        return rel_path

    def _sanitize_filename(self, filename):
        filename = unquote(filename)
        return re.sub(r'[\\/*?:"<>|]', "_", filename)[:100]

    def _get_site_root_path(self):
        base_path = urlparse(self.base_url).path.rstrip('/')
        if self.subdir and base_path.endswith(f"/{self.subdir}"):
            base_path = base_path[:-(len(self.subdir) + 1)]
        return base_path or '/'

    def _build_asset_candidates(self, url, asset_type='images', page_url=None):
        candidates = []

        def add(candidate):
            if candidate and candidate not in candidates:
                candidates.append(candidate)

        add(url)
        if asset_type != 'images':
            return candidates

        parsed_url = urlparse(url)
        parsed_base = urlparse(self.base_url)
        origin = f"{parsed_base.scheme}://{parsed_base.netloc}"
        filename = os.path.basename(unquote(parsed_url.path))
        site_root_path = self._get_site_root_path().rstrip('/')

        lang_image_prefix = f"/{self.subdir}/images/"
        if self.subdir and lang_image_prefix in parsed_url.path:
            add(urljoin(origin, parsed_url.path.replace(lang_image_prefix, "/images/", 1)))

        if filename:
            if page_url:
                page_parts = [part for part in urlparse(page_url).path.strip('/').split('/') if part]
                if len(page_parts) >= 2:
                    section_name = page_parts[-2]
                    add(urljoin(origin, f"{site_root_path}/images/{section_name}/{filename}"))

            add(urljoin(origin, f"{site_root_path}/images/{filename}"))

        return candidates

    def _inspect_asset_payload(self, asset_type, content_type, first_chunk):
        if not first_chunk:
            return False, "响应体为空", None

        if asset_type != 'images':
            return True, "", None

        content_type = (content_type or '').lower()
        sample = first_chunk[:512].lstrip()
        lower_sample = sample.lower()
        html_markers = (
            b'<!doctype html',
            b'<html',
            b'<head',
            b'<body',
        )
        if 'text/html' in content_type or any(lower_sample.startswith(marker) for marker in html_markers):
            return False, "响应是 HTML 页面", None

        if b'<svg' in lower_sample or content_type == 'image/svg+xml':
            image_kind = 'svg'
        elif first_chunk.startswith(b'\x89PNG\r\n\x1a\n'):
            image_kind = 'png'
        elif first_chunk.startswith(b'\xff\xd8\xff'):
            image_kind = 'jpeg'
        elif first_chunk.startswith((b'GIF87a', b'GIF89a')):
            image_kind = 'gif'
        elif first_chunk.startswith(b'RIFF') and first_chunk[8:12] == b'WEBP':
            image_kind = 'webp'
        else:
            content_type_map = {
                'image/png': 'png',
                'image/jpeg': 'jpeg',
                'image/jpg': 'jpeg',
                'image/gif': 'gif',
                'image/webp': 'webp',
            }
            image_kind = content_type_map.get(content_type)

        if not image_kind:
            if content_type and content_type != 'application/octet-stream':
                return False, f"响应类型异常: {content_type}", None
            return False, "不是可识别的图片格式", None

        return True, "", image_kind

    def _is_existing_asset_valid(self, path, url, asset_type):
        try:
            with open(path, 'rb') as f:
                first_chunk = f.read(512)
        except OSError:
            return False

        is_valid, _, _ = self._inspect_asset_payload(asset_type, '', first_chunk)
        return is_valid

    def _download_asset_to_path(self, url, save_path, asset_type='images', page_url=None):
        request_headers = {}
        if asset_type == 'images':
            request_headers.update({
                'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                'Referer': page_url or f"{self.base_url}/",
            })

        with self.session.get(url, stream=True, timeout=15, headers=request_headers) as response:
            response.raise_for_status()
            content_type = response.headers.get('Content-Type', '').split(';')[0].strip().lower()
            chunks = response.iter_content(8192)
            first_chunk = next(chunks, b'')

            is_valid, reason, image_kind = self._inspect_asset_payload(asset_type, content_type, first_chunk)
            if not is_valid:
                raise ValueError(reason)

            if asset_type == 'images':
                declared_ext = Path(urlparse(url).path).suffix.lower()
                ext_map = {
                    '.png': 'png',
                    '.jpg': 'jpeg',
                    '.jpeg': 'jpeg',
                    '.gif': 'gif',
                    '.webp': 'webp',
                    '.svg': 'svg',
                }
                declared_kind = ext_map.get(declared_ext)
                if declared_kind and image_kind and declared_kind != image_kind:
                    if self.console:
                        self.console.print(f"[cyan]资源后缀与实际格式不一致，沿用原文件名: {url}[/cyan]")
                    else:
                        print(f"资源后缀与实际格式不一致，沿用原文件名: {url}")

            with open(save_path, 'wb') as f:
                f.write(first_chunk)
                for chunk in chunks:
                    f.write(chunk)

    def download_asset(self, url, asset_type='images', page_url=None):
        if url in self.asset_map:
            return self.asset_map[url]

        try:
            original_url = url
            asset_dir = self.output_dir / asset_type
            asset_dir.mkdir(parents=True, exist_ok=True)

            parsed = urlparse(url)
            orig_filename = os.path.basename(unquote(parsed.path))
            if not orig_filename:
                ext = os.path.splitext(parsed.path)[1][1:] or 'bin'
                filename = f"{hashlib.md5(url.encode()).hexdigest()[:8]}.{ext}"
            else:
                filename = self._sanitize_filename(orig_filename)

            save_path = asset_dir / filename

            if save_path.exists() and not self._is_existing_asset_valid(save_path, url, asset_type):
                if self.console:
                    self.console.print(f"[yellow]检测到无效资源，准备重下: {save_path.name}[/yellow]")
                else:
                    print(f"检测到无效资源，准备重下: {save_path.name}")
                save_path.unlink()

            if not save_path.exists():
                last_error = None
                for candidate_url in self._build_asset_candidates(url, asset_type, page_url):
                    try:
                        if self.console:
                            self.console.print(f"[yellow]下载资源: {candidate_url}[/yellow]")
                        else:
                            print(f"下载资源: {candidate_url}")
                        self._download_asset_to_path(candidate_url, save_path, asset_type, page_url)
                        url = candidate_url
                        break
                    except Exception as e:
                        last_error = e
                        if save_path.exists():
                            save_path.unlink()
                        if self.console:
                            self.console.print(f"[yellow]资源候选地址失败: {candidate_url} - {e}[/yellow]")
                        else:
                            print(f"资源候选地址失败: {candidate_url} - {e}")
                else:
                    raise last_error or ValueError("没有可用的资源地址")

            relative_path = f"{asset_type}/{filename}"
            self.asset_map[original_url] = relative_path
            self.asset_map[url] = relative_path
            return relative_path

        except Exception as e:
            if RICH_AVAILABLE:
                self.console.print(f"[red]资源下载失败: {original_url if 'original_url' in locals() else url} - {e}[/red]")
            else:
                print(f"资源下载失败: {original_url if 'original_url' in locals() else url} - {e}")
            return None

    def _clean_markdown(self, markdown):
        """小米Vela文档专用清理函数"""
        # 仅清理非代码块区域，避免误改代码内容
        parts = re.split(r'(```.*?```)', markdown, flags=re.DOTALL)
        cleaned_parts = []

        for part in parts:
            if part.startswith('```') and part.endswith('```'):
                cleaned_parts.append(part)
                continue

            # 修复标题格式（移除锚点#号）
            part = re.sub(r'^#\s+#\s+(.*)$', r'## \1', part, flags=re.MULTILINE)

            # 修复表格对齐
            part = re.sub(r'\|(\s*-+\s*)\|', r'|:---:|', part)

            # 清理多余空行
            part = re.sub(r'\n{3,}', '\n\n', part)
            cleaned_parts.append(part)

        markdown = ''.join(cleaned_parts)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        return markdown.strip() + '\n'

    def convert_html_to_markdown(self, html, page_url):
        soup = BeautifulSoup(html, 'html.parser')
        code_blocks = []

        # 移除不需要的元素
        for element in soup(['script', 'style', 'nav', 'footer', 'iframe', 'svg']):
            element.decompose()

        # 移除特定组件
        for tag in ['header.navbar', 'aside.sidebar', 'div.page-nav', 'div.toc']:
            for element in soup.select(tag):
                element.decompose()

        # 特殊处理标题（移除锚点链接）
        for header in soup.find_all(re.compile('^h[1-6]$')):
            if header.find('a', class_='header-anchor'):
                header.a.decompose()
                header_text = header.get_text().strip()
                header.string = header_text

        # 处理代码块
        for pre in soup.find_all('pre'):
            parent_div = pre.find_parent('div', class_=re.compile('language-'))
            code_tag = pre.find('code')
            class_source = []
            if parent_div and parent_div.get('class'):
                class_source.extend(parent_div.get('class', []))
            if code_tag and code_tag.get('class'):
                class_source.extend(code_tag.get('class', []))

            # 提取语言类型
            class_text = ' '.join(class_source)
            lang_match = re.search(r'language-([\w+-]+)', class_text)
            language = lang_match.group(1) if lang_match else ''

            # 提取原始代码（保留换行和缩进）
            code = pre.get_text()
            placeholder = f"CODE_BLOCK_PLACEHOLDER_{len(code_blocks)}"
            code_blocks.append((placeholder, self._build_code_block(language, code)))

            # 用占位符替换，避免 html2text 压平 fenced code block
            target = parent_div if parent_div else pre
            target.replace_with(NavigableString(f"\n\n{placeholder}\n\n"))

        # 处理图片
        for img in soup.find_all('img', src=True):
            img_url = urljoin(page_url, img['src'])
            local_path = self.download_asset(img_url, 'images', page_url)
            if local_path:
                img['src'] = local_path
                continue

            missing_text = NavigableString(self._missing_image_text(img_url))
            img.replace_with(missing_text)

        # 使用html2text转换
        from html2text import HTML2Text
        h = HTML2Text()
        h.body_width = 0
        h.mark_code = True
        h.protect_links = True
        markdown = h.handle(str(soup))

        # 后处理清理
        markdown = self._clean_markdown(markdown)
        markdown = self._restore_code_blocks(markdown, code_blocks)
        markdown = self._normalize_code_block_spacing(markdown)
        markdown = self._normalize_table_continuations(markdown)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        return markdown

    def save_markdown_file(self, content, url):
        rel_path = self._get_relative_path(url)
        if not rel_path or rel_path.endswith('/'):
            rel_path += 'index'
        rel_path = re.sub(r'\.(html|htm|php|aspx)$', '', rel_path)
        md_path = (self.output_dir / rel_path).with_suffix('.md')
        md_path.parent.mkdir(parents=True, exist_ok=True)

        final_content = f"<!-- 源地址: {url} -->\n\n{content}"

        def adjust_img(match):
            alt_text = match.group(1)
            img_path = match.group(2)
            if re.match(r'^[a-z]+://', img_path, flags=re.IGNORECASE):
                return f"![{alt_text}]({img_path})"
            abs_img_path = Path(self.output_dir) / img_path
            rel_img_path = os.path.relpath(abs_img_path, start=md_path.parent)
            return f"![{alt_text}]({rel_img_path})"

        final_content = re.sub(r'!\[(.*?)\]\((.*?)\)', adjust_img, final_content)

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        if RICH_AVAILABLE:
            self.console.print(f"[green]已保存文件:[/green] {md_path.relative_to(self.output_dir)}")
        else:
            print(f"已保存文件: {md_path.relative_to(self.output_dir)}")
        return md_path

    def process_page(self, url, progress_task=None):
        if url in self.visited:
            return set()

        if RICH_AVAILABLE:
            self.console.print(f"[blue]请求页面:[/blue] {url}")
        else:
            print(f"请求页面: {url}")
        
        self.visited.add(url)

        try:
            # 尝试正常请求
            try:
                response = self.session.get(url, timeout=500, verify=True)
            except requests.exceptions.SSLError:
                # 如果SSL验证失败，尝试禁用SSL验证（不推荐用于生产环境，但适用于文档爬取）
                if RICH_AVAILABLE:
                    self.console.print(f"[yellow]SSL验证失败，尝试不验证SSL:[/yellow] {url}")
                else:
                    print(f"SSL验证失败，尝试不验证SSL: {url}")
                response = self.session.get(url, timeout=500, verify=False)
                
            response.encoding = response.apparent_encoding

            if response.history:
                url = response.url

            if RICH_AVAILABLE:
                self.console.print(f"[cyan]转换内容:[/cyan] {url}")
            else:
                print(f"转换内容: {url}")
                
            md_content = self.convert_html_to_markdown(response.text, url)
            self.save_markdown_file(md_content, url)

            soup = BeautifulSoup(response.text, 'html.parser')
            new_links = set()

            # --- 修改链接发现逻辑 ---
            # 获取当前 scraper 实例的基础路径，用于验证发现的链接
            expected_base_path = urlparse(self.base_url).path # 例如: /vela/quickapp/zh/

            for a in soup.find_all('a', href=True):
                href = a['href']
                full_url = urljoin(url, href)

                parsed_full = urlparse(full_url)
                parsed_base = urlparse(self.base_url)

                # 检查域名是否相同
                if parsed_full.netloc == parsed_base.netloc:
                    # 检查路径是否以当前 scraper 的基础路径开头
                    if not parsed_full.path.startswith(expected_base_path):
                        # 如果发现的链接不是以当前 scraper 的语言路径开头，则跳过
                        continue

                    clean_url = full_url.split('#')[0].split('?')[0]
                    if clean_url not in self.visited:
                        new_links.add(clean_url)

            return new_links

        except Exception as e:
            if RICH_AVAILABLE:
                self.console.print(f"[red]处理失败: {url} - {e}[/red]")
            else:
                print(f"处理失败: {url} - {e}")
            return set()

    def crawl(self, start_url=None, max_workers=16, delay=0.3):
        start_url = start_url or self.base_url
        self.visited = set()
        self.processed_pages = 0

        if RICH_AVAILABLE:
            info_table = Table(show_header=False, box=None)
            info_table.add_column(style="green")
            info_table.add_column(style="yellow")
            info_table.add_row("开始爬取:", start_url)
            info_table.add_row("输出目录:", str(self.output_dir))
            info_table.add_row("并发数:", str(max_workers))
            self.console.print(info_table)
            self.console.print()
        else:
            print(f"开始爬取: {start_url}")
            print(f"输出目录: {self.output_dir}")

        # 首先获取所有需要处理的链接
        all_urls = set()
        urls_to_process = [start_url]
        
        if RICH_AVAILABLE:
            self.console.print("[cyan]扫描页面链接...[/cyan]")
        else:
            print("扫描页面链接...")
            
        while urls_to_process:
            current_url = urls_to_process.pop()
            if current_url in all_urls:
                continue
                    
            all_urls.add(current_url)
            try:
                # 尝试正常请求
                try:
                    response = self.session.get(current_url, timeout=500, verify=True)
                except requests.exceptions.SSLError:
                    # SSL错误时尝试不验证SSL
                    if RICH_AVAILABLE:
                        self.console.print(f"[yellow]预扫描SSL错误，尝试不验证SSL:[/yellow] {current_url}")
                    else:
                        print(f"预扫描SSL错误，尝试不验证SSL: {current_url}")
                    response = self.session.get(current_url, timeout=500, verify=False)
                    
                soup = BeautifulSoup(response.text, 'html.parser')
                
                expected_base_path = urlparse(self.base_url).path
                parsed_base = urlparse(self.base_url)
                
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    full_url = urljoin(current_url, href)
                    
                    parsed_full = urlparse(full_url)
                    if (parsed_full.netloc == parsed_base.netloc and 
                        parsed_full.path.startswith(expected_base_path)):
                        clean_url = full_url.split('#')[0].split('?')[0]
                        if clean_url not in all_urls:
                            urls_to_process.append(clean_url)
                            
            except Exception as e:
                if RICH_AVAILABLE:
                    self.console.print(f"[yellow]预扫描警告: {current_url} - {e}[/yellow]")
                else:
                    print(f"预扫描警告: {current_url} - {e}")

        self.total_pages = len(all_urls)
        
        if RICH_AVAILABLE:
            self.console.print(f"[cyan]发现 {self.total_pages} 个页面，开始处理...[/cyan]")
            self.console.print()
            
            # 使用Rich的进度条
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeElapsedColumn(),
                console=self.console
            ) as progress:
                task = progress.add_task("爬取进度", total=self.total_pages)
                
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    future_to_url = {executor.submit(self.process_page, url): url for url in all_urls}
                    
                    for future in as_completed(future_to_url):
                        url = future_to_url[future]
                        try:
                            future.result()
                            progress.update(task, advance=1)
                        except Exception as e:
                            if RICH_AVAILABLE:
                                self.console.print(f"[red]任务失败: {url} - {e}[/red]")
                            else:
                                print(f"任务失败: {url} - {e}")
        else:
            # 原始的处理方式
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_url = {executor.submit(self.process_page, start_url): start_url}

                while future_to_url:
                    for future in as_completed(future_to_url):
                        url = future_to_url[future]
                        try:
                            new_links = future.result()
                            for link in new_links:
                                if link not in self.visited:
                                    time.sleep(delay)
                                    future_to_url[executor.submit(self.process_page, link)] = link
                        except Exception as e:
                            print(f"任务失败: {url} - {e}")
                        finally:
                            del future_to_url[future]

        # 完成信息
        if RICH_AVAILABLE:
            self.console.print()
            success_panel = Panel(
                f"[green]爬取完成！共处理 {len(self.visited)} 个页面[/green]\n"
                f"[cyan]Markdown文件保存在: {self.output_dir}[/cyan]\n"
                f"[cyan]图片保存在: {self.output_dir}/images[/cyan]",
                title="完成",
                border_style="green",
                expand=False
            )
            self.console.print(success_panel)
        else:
            print(f"\n爬取完成！共处理 {len(self.visited)} 个页面")
            print(f"Markdown文件保存在: {self.output_dir}")
            print(f"图片保存在: {self.output_dir}/images")

if __name__ == "__main__":
    # 显示ASCII Art（统一使用蓝色）
    if RICH_AVAILABLE:
        console = Console()
        console.print(VELA_ASCII_ART, style="bold blue")
    else:
        print(VELA_ASCII_ART)
    
    # 修正默认 URL 为基础路径 (移除末尾空格)
    DEFAULT_URL = "https://iot.mi.com/vela/quickapp/"

    # 不再使用命令行参数，直接硬编码
    base_url = DEFAULT_URL
    output_dir = "docs"
    delay = 0.2
    workers = 32 # 使用合理的并发数

    languages = ['zh', 'en'] # 要爬取的语言版本

    for lang in languages:
        lang_url = f"{base_url}{lang}/"
        if RICH_AVAILABLE:
            console.print(f"\n[bold blue]开始爬取 {lang.upper()} 版本[/bold blue]")
        else:
            print(f"\n开始爬取 {lang.upper()} 版本")
        
        scraper = MarkdownScraper(
            base_url=lang_url, # 使用带语言的 URL 作为基础 URL
            output_dir=output_dir # 使用总输出目录
        )
        scraper.crawl(
            start_url=lang_url, # 从带语言的 URL 开始
            max_workers=workers,
            delay=delay
        )
        
        if RICH_AVAILABLE:
            console.print(f"[bold blue]{lang.upper()} 版本爬取完成[/bold blue]\n")
        else:
            print(f"{lang.upper()} 版本爬取完成\n")

    if RICH_AVAILABLE:
        console.print("[bold blue]所有语言版本爬取完成！[/bold blue]")
        console.print(f"[blue]Markdown文件保存在: {output_dir}[/blue]")
        console.print(f"[blue]图片保存在: {output_dir}/zh/images 和 {output_dir}/en/images[/blue]")
    else:
        print("所有语言版本爬取完成！")
        print(f"Markdown文件保存在: {output_dir}")
        print(f"图片保存在: {output_dir}/zh/images 和 {output_dir}/en/images")
