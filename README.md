# VelaDocs

VelaDocs抓取 [Xiaomi Vela JS](https://iot.mi.com/vela/quickapp/) 文档，并将其转换为 Markdown 格式。供小米微辣开发者使用。如果你使用Chromium内核浏览器，建议搭配[VelaDocsCopier](https://github.com/CheongSzesuen/VelaDocsCopier)使用，可在网站**一键复制**该页文档。

## 使用方法

运行成功后，会在当前目录生成 `docs` 文件夹，里面存放所有文档。

不克隆仓库，直接通过命令行一键下载脚本并启动。

Linux / macOS：

```bash
curl -L 'https://cdn.jsdelivr.net/gh/CheongSzesuen/VelaDocs@main/run_scraper-linux%26mac.sh' -o run_scraper-linux\&mac.sh || curl -L 'https://raw.githubusercontent.com/CheongSzesuen/VelaDocs/main/run_scraper-linux%26mac.sh' -o run_scraper-linux\&mac.sh && chmod +x './run_scraper-linux&mac.sh' && ./run_scraper-linux\&mac.sh
```

Windows PowerShell：

```powershell
try { Invoke-WebRequest 'https://cdn.jsdelivr.net/gh/CheongSzesuen/VelaDocs@main/run_scraper-win.cmd' -OutFile 'run_scraper-win.cmd' -UseBasicParsing } catch { Invoke-WebRequest 'https://raw.githubusercontent.com/CheongSzesuen/VelaDocs/main/run_scraper-win.cmd' -OutFile 'run_scraper-win.cmd' -UseBasicParsing }; .\run_scraper-win.cmd
```

## 许可证
Docs来自小米vela官方文档，爬取供开发者使用，仅用于学习交流。
