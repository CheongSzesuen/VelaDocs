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

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache'
        })

        # 确保最终的输出目录存在
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _get_relative_path(self, url):
        # 计算相对于 base_url 的路径，但不包含 base_url 中的语言部分
        # 例如，如果 base_url 是 https://iot.mi.com/vela/quickapp/zh/  ，url 是 https://iot.mi.com/vela/quickapp/zh/guide/start
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

            relative_path = f"{asset_type}/{filename}"
            self.asset_map[url] = relative_path
            return relative_path

        except Exception as e:
            print(f"⚠️ 资源下载失败: {url} - {e}")
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
                # 提取语言类型
                lang_match = re.search(r'language-(\w+)', ' '.join(parent_div['class']))
                language = lang_match.group(1) if lang_match else ''

                # 提取原始代码（保留换行和缩进）
                code = pre.get_text('\n')

                # 特殊处理JavaScript代码
                if language == 'javascript':
                    code = re.sub(r'(\w)\s+\.\s+(\w)', r'\1.\2', code)
                    code = re.sub(r'\s+\(\s+', '(', code)
                    code = re.sub(r'\s+\)\s+', ')', code)

                # 替换为Markdown代码块
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

        print(f"✅ 已保存: {md_path.relative_to(self.output_dir)}")
        return md_path

    def process_page(self, url):
        if url in self.visited:
            return set()

        print(f"🔄 正在处理: {url}")
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
            print(f"❌ 处理失败: {url} - {e}")
            return set()

    def crawl(self, start_url=None, max_workers=16, delay=0.3):
        start_url = start_url or self.base_url
        self.visited = set()

        print(f"🚀 开始爬取: {start_url}")
        print(f"📁 输出目录: {self.output_dir}")

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
                        print(f"❌ 任务失败: {url} - {e}")
                    finally:
                        del future_to_url[future]

        print(f"\n🎉 爬取完成！共处理 {len(self.visited)} 个页面")
        print(f"📝 Markdown文件保存在: {self.output_dir}")
        print(f"🖼️ 图片保存在: {self.output_dir}/images")

if __name__ == "__main__":
    # 修正默认 URL 为基础路径 (移除末尾空格)
    DEFAULT_URL = "https://iot.mi.com/vela/quickapp/"

    # 不再使用命令行参数，直接硬编码
    base_url = DEFAULT_URL
    output_dir = "docs"
    delay = 0.3
    workers = 512 # 使用合理的并发数

    languages = ['zh', 'en'] # 要爬取的语言版本

    for lang in languages:
        lang_url = f"{base_url}{lang}/"
        print(f"\n--- 开始爬取 {lang.upper()} 版本 ---")
        scraper = MarkdownScraper(
            base_url=lang_url, # 使用带语言的 URL 作为基础 URL
            output_dir=output_dir # 使用总输出目录
        )
        scraper.crawl(
            start_url=lang_url, # 从带语言的 URL 开始
            max_workers=workers,
            delay=delay
        )
        print(f"--- {lang.upper()} 版本爬取完成 ---\n")

    print("🎉 所有语言版本爬取完成！")
    print(f"📝 Markdown文件保存在: {output_dir}")
    print(f"🖼️ 图片保存在: {output_dir}/zh/images 和 {output_dir}/en/images")
