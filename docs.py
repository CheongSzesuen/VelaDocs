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
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
from pathlib import Path
import time
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
from datetime import datetime
import threading
import sys


class ColoredOutput:
    """用于美化输出的类"""
    # ANSI 转义序列
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    @staticmethod
    def red(text):
        return f"{ColoredOutput.RED}{text}{ColoredOutput.RESET}"

    @staticmethod
    def green(text):
        return f"{ColoredOutput.GREEN}{text}{ColoredOutput.RESET}"

    @staticmethod
    def yellow(text):
        return f"{ColoredOutput.YELLOW}{text}{ColoredOutput.RESET}"

    @staticmethod
    def blue(text):
        return f"{ColoredOutput.BLUE}{text}{ColoredOutput.RESET}"

    @staticmethod
    def magenta(text):
        return f"{ColoredOutput.MAGENTA}{text}{ColoredOutput.RESET}"

    @staticmethod
    def cyan(text):
        return f"{ColoredOutput.CYAN}{text}{ColoredOutput.RESET}"

    @staticmethod
    def bold(text):
        return f"{ColoredOutput.BOLD}{text}{ColoredOutput.RESET}"

    @staticmethod
    def status_processing(text):
        return f"{ColoredOutput.YELLOW}[PROCESSING]{ColoredOutput.RESET} {text}"

    @staticmethod
    def status_success(text):
        return f"{ColoredOutput.GREEN}[SUCCESS]{ColoredOutput.RESET} {text}"

    @staticmethod
    def status_error(text):
        return f"{ColoredOutput.RED}[ERROR]{ColoredOutput.RESET} {text}"

    @staticmethod
    def status_info(text):
        return f"{ColoredOutput.CYAN}[INFO]{ColoredOutput.RESET} {text}"


class ProgressBar:
    """简单的进度条"""
    def __init__(self, total, width=50):
        self.total = total
        self.width = width
        self.current = 0
        self.lock = threading.Lock()

    def update(self, increment=1):
        with self.lock:
            self.current += increment
            percentage = int((self.current / self.total) * 100)
            filled = int((self.current / self.total) * self.width)
            bar = '█' * filled + '░' * (self.width - filled)
            sys.stdout.write(f'\r|{bar}| {percentage}% ({self.current}/{self.total})')
            sys.stdout.flush()

    def finish(self):
        print()  # 换行


class MarkdownScraper:
    def __init__(self, base_url, output_dir="docs"):
        self.base_url = base_url.rstrip('/')
        self.output_dir = Path(output_dir).resolve()

        # --- 新增逻辑：根据 base_url 确定子目录 ---
        parsed_base = urlparse(self.base_url)
        path_parts = parsed_base.path.strip('/').split('/')
        self.subdir = ''
        if path_parts and path_parts[-1] in ['zh', 'en']:
            self.subdir = path_parts[-1]

        # 如果存在子目录，则调整输出路径
        if self.subdir:
            self.output_dir = self.output_dir / self.subdir

        self.visited = set()
        self.asset_map = {}
        self.processed_pages = 0
        self.failed_pages = 0
        self.downloaded_assets = 0

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache'
        })

        # 确保最终的输出目录存在
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # 用于进度条的锁
        self.stats_lock = threading.Lock()

    def _get_relative_path(self, url):
        parsed_url = urlparse(url)
        parsed_base = urlparse(self.base_url)
        path = parsed_url.path
        base_path = parsed_base.path
        rel_path = path.replace(base_path, '', 1).lstrip('/')
        return rel_path

    def _sanitize_filename(self, filename):
        filename = unquote(filename)
        return re.sub(r'[\\/*?:"<>|]', "_", filename)[:100]

    def download_asset(self, url, asset_type='images'):
        if url in self.asset_map:
            return self.asset_map[url]

        try:
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

            if not save_path.exists():
                response = self.session.get(url, stream=True, timeout=15)
                response.raise_for_status()
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                # 更新统计
                with self.stats_lock:
                    self.downloaded_assets += 1
                print(ColoredOutput.status_success(f"Asset downloaded: {filename}"))

            relative_path = f"{asset_type}/{filename}"
            self.asset_map[url] = relative_path
            return relative_path

        except Exception as e:
            print(ColoredOutput.status_error(f"Asset download failed: {url} - {e}"))
            return url

    def _clean_markdown(self, markdown):
        """小米Vela文档专用清理函数"""
        # 修复标题格式（移除锚点#号）
        markdown = re.sub(r'^#\s+#\s+(.*)$', r'## \1', markdown, flags=re.MULTILINE)

        # 修复代码块格式
        markdown = re.sub(r'```(\w+)\s+', r'```\1\n', markdown)
        markdown = re.sub(r'(\S)\s+```', r'\1\n```', markdown)

        # 修复方法调用中的多余空格
        markdown = re.sub(r'(\w)\s+\.\s+(\w)', r'\1.\2', markdown)

        # 修复括号内的多余空格
        markdown = re.sub(r'\(\s+', '(', markdown)
        markdown = re.sub(r'\s+\)', ')', markdown)

        # 修复表格对齐
        markdown = re.sub(r'\|(\s*-+\s*)\|', r'|:---:|', markdown)

        # 清理多余空行
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        return markdown

    def convert_html_to_markdown(self, html, page_url):
        soup = BeautifulSoup(html, 'html.parser')

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
            if parent_div:
                lang_match = re.search(r'language-(\w+)', ' '.join(parent_div['class']))
                language = lang_match.group(1) if lang_match else ''
                code = pre.get_text('\n')

                if language == 'javascript':
                    code = re.sub(r'(\w)\s+\.\s+(\w)', r'\1.\2', code)
                    code = re.sub(r'\s+\(\s+', '(', code)
                    code = re.sub(r'\s+\)\s+', ')', code)

                pre.replace_with(f"```{language}\n{code}\n```")

        # 处理图片
        for img in soup.find_all('img', src=True):
            img_url = urljoin(page_url, img['src'])
            local_path = self.download_asset(img_url, 'images')
            img['src'] = local_path

        # 使用html2text转换
        from html2text import HTML2Text
        h = HTML2Text()
        h.body_width = 0
        h.mark_code = True
        h.protect_links = True
        markdown = h.handle(str(soup))

        # 后处理清理
        markdown = self._clean_markdown(markdown)
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
            abs_img_path = Path(self.output_dir) / img_path
            rel_img_path = os.path.relpath(abs_img_path, start=md_path.parent)
            return f"![{alt_text}]({rel_img_path})"

        final_content = re.sub(r'!\[(.*?)\]\((.*?)\)', adjust_img, final_content)

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        # 更新统计
        with self.stats_lock:
            self.processed_pages += 1
        print(ColoredOutput.status_success(f"Saved: {md_path.relative_to(self.output_dir)}"))
        return md_path

    def process_page(self, url):
        if url in self.visited:
            return set()

        print(ColoredOutput.status_processing(f"Processing: {url}"))
        self.visited.add(url)

        try:
            response = self.session.get(url, timeout=500)
            response.encoding = response.apparent_encoding

            if response.history:
                url = response.url

            md_content = self.convert_html_to_markdown(response.text, url)
            self.save_markdown_file(md_content, url)

            soup = BeautifulSoup(response.text, 'html.parser')
            new_links = set()

            expected_base_path = urlparse(self.base_url).path

            for a in soup.find_all('a', href=True):
                href = a['href']
                full_url = urljoin(url, href)

                parsed_full = urlparse(full_url)
                parsed_base = urlparse(self.base_url)

                if parsed_full.netloc == parsed_base.netloc:
                    if not parsed_full.path.startswith(expected_base_path):
                        continue

                    clean_url = full_url.split('#')[0].split('?')[0]
                    if clean_url not in self.visited:
                        new_links.add(clean_url)

            return new_links

        except Exception as e:
            print(ColoredOutput.status_error(f"Failed to process: {url} - {e}"))
            # 更新失败统计
            with self.stats_lock:
                self.failed_pages += 1
            return set()

    def crawl(self, start_url=None, max_workers=16, delay=0.3):
        start_url = start_url or self.base_url
        self.visited = set()

        print("\n" + "="*80)
        print(ColoredOutput.bold(ColoredOutput.magenta("🚀 开始爬取任务")))
        print("="*80)
        print(f"  📌 目标 URL: {ColoredOutput.cyan(start_url)}")
        print(f"  📁 输出目录: {ColoredOutput.cyan(self.output_dir)}")
        print(f"  👥 并发线程数: {ColoredOutput.yellow(max_workers)}")
        print(f"  ⏱️  请求间隔: {ColoredOutput.yellow(delay)}s")
        print("-"*80)

        all_urls_to_process = {start_url}
        processed_urls = set()
        futures_map = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交第一个任务
            futures_map[executor.submit(self.process_page, start_url)] = start_url

            while futures_map:
                for future in as_completed(futures_map):
                    url = futures_map[future]
                    try:
                        new_links = future.result()
                        processed_urls.add(url)
                        
                        # 添加新发现的链接到待处理集合
                        for link in new_links:
                            if link not in processed_urls and link not in all_urls_to_process:
                                all_urls_to_process.add(link)
                        
                        # 如果还有未处理的链接，提交新任务
                        submitted_this_round = 0
                        for link in list(all_urls_to_process - processed_urls):
                            if submitted_this_round < max_workers: # 限制此轮提交数量
                                time.sleep(delay)
                                futures_map[executor.submit(self.process_page, link)] = link
                                submitted_this_round += 1
                            else:
                                break # 避免一次性提交过多任务

                    except Exception as e:
                        print(ColoredOutput.status_error(f"Task failed: {url} - {e}"))
                        with self.stats_lock:
                            self.failed_pages += 1
                    finally:
                        del futures_map[future]

        print("\n" + "="*80)
        print(ColoredOutput.bold(ColoredOutput.green("✅ 爬取任务完成！")))
        print("="*80)
        
        # 打印最终统计
        print(f"  📊 已处理页面: {ColoredOutput.green(self.processed_pages)}")
        print(f"  📊 已下载资源: {ColoredOutput.green(self.downloaded_assets)}")
        print(f"  ⚠️  失败页面: {ColoredOutput.red(self.failed_pages)}")
        print(f"  📄 总共访问 URL: {ColoredOutput.yellow(len(self.visited))}")
        print("-"*80)
        print(f"  📁 Markdown文件保存在: {ColoredOutput.cyan(self.output_dir)}")
        print(f"  🖼️  图片保存在: {ColoredOutput.cyan(self.output_dir / 'images')}")
        print("="*80)


if __name__ == "__main__":
    DEFAULT_URL = "https://iot.mi.com/vela/quickapp/"

    output_dir = "docs"
    delay = 0.3
    workers = 16

    languages = ['zh', 'en']

    print(ColoredOutput.bold(ColoredOutput.blue("🔧 小米Vela文档爬取工具")))
    print(ColoredOutput.bold(ColoredOutput.blue("="*50)))

    for lang in languages:
        lang_url = f"{DEFAULT_URL}{lang}/"
        print(f"\n{ColoredOutput.bold(f'--- 🌐 开始爬取 {lang.upper()} 版本 ---')}")
        
        scraper = MarkdownScraper(
            base_url=lang_url,
            output_dir=output_dir
        )
        scraper.crawl(
            start_url=lang_url,
            max_workers=workers,
            delay=delay
        )
        
        print(f"{ColoredOutput.bold(f'--- ✅ {lang.upper()} 版本爬取完成 ---')}\n")

    print("\n" + "="*80)
    print(ColoredOutput.bold(ColoredOutput.magenta("🎉 所有语言版本爬取完成！")))
    print("="*80)
    print(f"  📁 总输出目录: {ColoredOutput.cyan(output_dir)}")
    print(f"  📁 中文版文件: {ColoredOutput.cyan(output_dir + '/zh')}")
    print(f"  📁 英文版文件: {ColoredOutput.cyan(output_dir + '/en')}")
    print(f"  🖼️  中文版图片: {ColoredOutput.cyan(output_dir + '/zh/images')}")
    print(f"  🖼️  英文版图片: {ColoredOutput.cyan(output_dir + '/en/images')}")
    print("="*80)
