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


class RealTimeStats:
    """实时统计信息类"""
    def __init__(self):
        self.processed_pages = 0
        self.failed_pages = 0
        self.downloaded_assets = 0
        self.currently_processing = ""  # 当前正在处理的 URL
        self.lock = threading.Lock()
        self.start_time = datetime.now()

    def update_processing(self, url):
        with self.lock:
            self.currently_processing = url

    def inc_processed(self):
        with self.lock:
            self.processed_pages += 1

    def inc_failed(self):
        with self.lock:
            self.failed_pages += 1

    def inc_assets(self):
        with self.lock:
            self.downloaded_assets += 1

    def get_stats(self):
        with self.lock:
            return {
                'processed': self.processed_pages,
                'failed': self.failed_pages,
                'assets': self.downloaded_assets,
                'current': self.currently_processing,
                'elapsed': datetime.now() - self.start_time
            }

    def display_line(self):
        stats = self.get_stats()
        elapsed_str = str(stats['elapsed']).split('.')[0] # 移除微秒
        # 使用 \r 开头，\033[K 清除行尾内容
        sys.stdout.write(f"\r{ColoredOutput.CYAN}[INFO]{ColoredOutput.RESET} 已耗时: {elapsed_str} | 已处理: {stats['processed']} | 失败: {stats['failed']} | 资源: {stats['assets']} | 当前: {stats['current'][:50]}{'...' if len(stats['current']) > 50 else ''}\033[K")
        sys.stdout.flush()


class MarkdownScraper:
    def __init__(self, base_url, output_dir="docs", stats=None):
        self.base_url = base_url.rstrip('/')
        self.output_dir = Path(output_dir).resolve()
        self.stats = stats if stats else RealTimeStats() # 接收外部传入的统计对象

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

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache'
        })

        # 确保最终的输出目录存在
        self.output_dir.mkdir(parents=True, exist_ok=True)

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
                self.stats.inc_assets()
                # 不再打印单个资源下载信息，保持行内更新
                # print(ColoredOutput.status_success(f"Asset downloaded: {filename}"))

            relative_path = f"{asset_type}/{filename}"
            self.asset_map[url] = relative_path
            return relative_path

        except Exception as e:
            print() # 换行以避免与行内统计冲突
            print(ColoredOutput.status_error(f"资源下载失败: {url} - {e}"))
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

        self.stats.inc_processed()
        # 不再打印单个文件保存信息，保持行内更新
        # print(ColoredOutput.status_success(f"Saved: {md_path.relative_to(self.output_dir)}"))
        return md_path

    def process_page(self, url):
        if url in self.visited:
            return set()

        self.stats.update_processing(url) # 更新当前处理的URL
        # 注意：这里不直接打印，而是通过定时器在行内更新
        # print(ColoredOutput.status_processing(f"Processing: {url}"))

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
            print() # 换行以避免与行内统计冲突
            print(ColoredOutput.status_error(f"处理失败: {url} - {e}"))
            self.stats.inc_failed()
            return set()


def run_crawler_with_realtime_stats(scraper_instance, start_url, max_workers, delay):
    """在单独的线程中运行爬虫，并在主线程中更新实时统计"""
    import threading
    import time

    stats = scraper_instance.stats
    stop_display = threading.Event()

    def display_loop():
        while not stop_display.is_set():
            stats.display_line()
            time.sleep(0.5) # 每0.5秒更新一次显示

    # 启动显示线程
    display_thread = threading.Thread(target=display_loop, daemon=True)
    display_thread.start()

    # 在当前线程运行爬虫主逻辑
    start_url = start_url or scraper_instance.base_url
    scraper_instance.visited = set()

    print("\n" + "="*80)
    print(ColoredOutput.bold(ColoredOutput.magenta("🚀 开始爬取任务")))
    print("="*80)
    print(f"  目标 URL: {ColoredOutput.cyan(start_url)}")
    print(f"  输出目录: {ColoredOutput.cyan(scraper_instance.output_dir)}")
    print(f"  并发线程数: {ColoredOutput.yellow(max_workers)}")
    print(f"  请求间隔: {ColoredOutput.yellow(delay)}s")
    print("-"*80)
    print("  实时状态: ") # 开始行内更新

    all_urls_to_process = {start_url}
    processed_urls = set()
    futures_map = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交第一个任务
        futures_map[executor.submit(scraper_instance.process_page, start_url)] = start_url

        while futures_map:
            for future in as_completed(futures_map):
                url = futures_map[future]
                try:
                    new_links = future.result()
                    processed_urls.add(url)
                    
                    for link in new_links:
                        if link not in processed_urls and link not in all_urls_to_process:
                            all_urls_to_process.add(link)
                    
                    submitted_this_round = 0
                    for link in list(all_urls_to_process - processed_urls):
                        if submitted_this_round < max_workers:
                            time.sleep(delay)
                            futures_map[executor.submit(scraper_instance.process_page, link)] = link
                            submitted_this_round += 1
                        else:
                            break

                except Exception as e:
                    print() # 换行
                    print(ColoredOutput.status_error(f"任务失败: {url} - {e}"))
                    stats.inc_failed()
                finally:
                    del futures_map[future]

    # 停止显示线程
    stop_display.set()
    display_thread.join()

    # 打印最终结果
    print("\n" + "="*80) # 换行并打印分隔符
    print(ColoredOutput.bold(ColoredOutput.green("✅ 爬取任务完成！")))
    print("="*80)
    
    final_stats = stats.get_stats()
    print(f"  已处理页面: {ColoredOutput.green(final_stats['processed'])}")
    print(f"  已下载资源: {ColoredOutput.green(final_stats['assets'])}")
    print(f"  失败页面: {ColoredOutput.red(final_stats['failed'])}")
    print(f"  总耗时: {ColoredOutput.yellow(str(final_stats['elapsed']).split('.')[0])}")
    print(f"  总共访问 URL: {ColoredOutput.yellow(len(scraper_instance.visited))}")
    print("-"*80)
    print(f"  Markdown文件保存在: {ColoredOutput.cyan(scraper_instance.output_dir)}")
    print(f"  图片保存在: {ColoredOutput.cyan(scraper_instance.output_dir / 'images')}")
    print("="*80)


if __name__ == "__main__":
    DEFAULT_URL = "https://iot.mi.com/vela/quickapp/"

    output_dir = "docs"
    delay = 0.3
    workers = 16

    languages = ['zh', 'en']

    print(ColoredOutput.bold(ColoredOutput.blue("🔧 小米Vela文档爬取工具")))
    print(ColoredOutput.bold(ColoredOutput.blue("="*50)))

    # 为所有语言版本共享一个统计对象
    shared_stats = RealTimeStats()

    for lang in languages:
        lang_url = f"{DEFAULT_URL}{lang}/"
        print(f"\n{ColoredOutput.bold(f'--- 🌐 开始爬取 {lang.upper()} 版本 ({lang_url}) ---')}")
        
        scraper = MarkdownScraper(
            base_url=lang_url,
            output_dir=output_dir,
            stats=shared_stats # 传递共享的统计对象
        )
        run_crawler_with_realtime_stats(
            scraper_instance=scraper,
            start_url=lang_url,
            max_workers=workers,
            delay=delay
        )
        
        print(f"{ColoredOutput.bold(f'--- ✅ {lang.upper()} 版本爬取完成 ---')}\n")

    print("\n" + "="*80)
    print(ColoredOutput.bold(ColoredOutput.magenta("🎉 所有语言版本爬取完成！")))
    print("="*80)
    final_stats = shared_stats.get_stats()
    print(f"  总计已处理页面: {ColoredOutput.green(final_stats['processed'])}")
    print(f"  总计已下载资源: {ColoredOutput.green(final_stats['assets'])}")
    print(f"  总计失败页面: {ColoredOutput.red(final_stats['failed'])}")
    print(f"  总耗时: {ColoredOutput.yellow(str(final_stats['elapsed']).split('.')[0])}")
    print(f"  总输出目录: {ColoredOutput.cyan(output_dir)}")
    print(f"  中文版文件: {ColoredOutput.cyan(output_dir + '/zh')}")
    print(f"  英文版文件: {ColoredOutput.cyan(output_dir + '/en')}")
    print(f"  中文版图片: {ColoredOutput.cyan(output_dir + '/zh/images')}")
    print(f"  英文版图片: {ColoredOutput.cyan(output_dir + '/en/images')}")
    print("="*80)

