#!/usr/bin/env python3
"""
静态网站Markdown爬取工具（默认爬取小米Vela文档）
功能：
1. 自动爬取整个文档网站
2. 保持原始Markdown格式
3. 下载图片并保持正确引用
4. 维持原始目录结构
5. 自动处理相对/绝对路径
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
        """
        初始化爬虫
        :param base_url: 文档网站基础URL (默认小米Vela文档)
        :param output_dir: 输出目录 (默认 "docs")
        """
        self.base_url = base_url.rstrip('/')
        self.output_dir = Path(output_dir).resolve()
        self.visited = set()
        self.asset_map = {}  # 存储已下载资源
        
        # 配置HTTP会话
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache'
        })
        
        # 创建输出目录
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def _get_relative_path(self, url):
        """将URL转换为相对于base_url的路径"""
        return urlparse(url).path.replace(urlparse(self.base_url).path, '').lstrip('/')
        
    def _sanitize_filename(self, filename):
        """清理文件名中的特殊字符"""
        filename = unquote(filename)
        filename = re.sub(r'[\\/*?:"<>|]', "_", filename)
        return filename[:100]  # 限制文件名长度
        
    def download_asset(self, url, asset_type='images'):
        """
        下载资源文件（图片/CSS等）
        返回本地相对路径
        """
        if url in self.asset_map:
            return self.asset_map[url]
    
        try:
            asset_dir = self.output_dir / asset_type
            asset_dir.mkdir(parents=True, exist_ok=True)
        
            # 从 URL 中提取原始文件名
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
            
    def convert_html_to_markdown(self, html, page_url):
        """
        将HTML转换为Markdown并处理资源引用
        """
        soup = BeautifulSoup(html, 'html.parser')
        
        # 移除不需要的元素
        for element in soup(['script', 'style', 'nav', 'footer', 'iframe', 'svg']):
            element.decompose()
        
        # 移除特定组件
        for tag in ['header.navbar', 'aside.sidebar', 'div.page-nav', 'div.toc']:
            for element in soup.select(tag):
                element.decompose()
    
        # 处理图片
        for img in soup.find_all('img', src=True):
            img_url = urljoin(page_url, img['src'])
            local_path = self.download_asset(img_url, 'images')
            img['src'] = local_path
            
        # 处理代码块
        for pre in soup.find_all('pre'):
            code = pre.get_text()
            pre.replace_with(f"```\n{code}\n```")
            
        from html2text import HTML2Text
        h = HTML2Text()
        h.body_width = 0
        h.mark_code = True
        h.protect_links = True
        markdown = h.handle(str(soup))
        
        # 清理格式
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        markdown = re.sub(r'(!\[.*?\])\((\S+)\)', lambda m: f"{m.group(1)}({m.group(2)})", markdown)
        return markdown
        
    def save_markdown_file(self, content, url):
        """保存Markdown文件"""
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
        """处理单个页面"""
        if url in self.visited:
            return set()
            
        print(f"🔄 正在处理: {url}")
        self.visited.add(url)
        
        try:
            response = self.session.get(url, timeout=15)
            response.encoding = response.apparent_encoding
            
            if response.history:
                url = response.url
                
            md_content = self.convert_html_to_markdown(response.text, url)
            self.save_markdown_file(md_content, url)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            new_links = set()
            
            for a in soup.find_all('a', href=True):
                href = a['href']
                full_url = urljoin(url, href)
                
                if urlparse(full_url).netloc == urlparse(self.base_url).netloc:
                    clean_url = full_url.split('#')[0].split('?')[0]
                    if clean_url not in self.visited:
                        new_links.add(clean_url)
                        
            return new_links
            
        except Exception as e:
            print(f"❌ 处理失败: {url} - {e}")
            return set()
            
    def crawl(self, start_url=None, max_workers=16, delay=0.3):
        """开始爬取"""
        start_url = start_url or self.base_url
        self.visited = set()
        
        print(f"🚀 开始爬取: {self.base_url}")
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
    DEFAULT_URL = "https://iot.mi.com/vela/quickapp/zh"
    
    parser = argparse.ArgumentParser(description='静态文档网站Markdown爬取工具（默认爬取小米Vela文档）')
    parser.add_argument('url', nargs='?', default=DEFAULT_URL, 
                       help=f'文档网站基础URL (默认: {DEFAULT_URL})')
    parser.add_argument('-o', '--output', default='docs', help='输出目录 (默认: docs)')
    parser.add_argument('-s', '--start', help='起始URL (默认使用基础URL)')
    parser.add_argument('-w', '--workers', type=int, default=16, help='并发线程数 (默认: 16)')
    parser.add_argument('-d', '--delay', type=float, default=0.3, help='请求间隔(秒) (默认: 0.3)')
    
    args = parser.parse_args()
    
    scraper = MarkdownScraper(
        base_url=args.url,
        output_dir=args.output
    )
    
    scraper.crawl(
        start_url=args.start,
        max_workers=args.workers,
        delay=args.delay
    )