# VelaDocs

VelaDocs抓取 Xiaomi Vela JS 应用相关文档，并将其转换为 Markdown 格式，同时下载页面中的图片等资源并调整引用路径。供小米微辣开发者使用。

## 功能介绍

- 自动爬取指定文档网站页面
- 转换 HTML 为 Markdown 格式
- 下载页面中图片、CSS 等资源，并保存为相对路径
- 调整图片引用，使其在 Markdown 文档中正确显示
- 支持过滤掉页面中不需要的导航栏（如 `<header class="navbar">` 及 `<aside class="sidebar">`）

## 仓库结构

```
VelaDocs/
├── docs/                   # 爬虫生成的 Markdown 文件及资源，如图片等
└── docs.py                 # 爬虫脚本
```
### Docs结构
```
(venv) waijade@WaiJade:~/文档/GitHub/VelaDocs/docs$ tree
.
├── components
│   ├── basic
│   │   ├── a.md
│   │   ├── barcode.md
│   │   ├── chart.md
│   │   ├── image-animator.md
│   │   ├── image.md
│   │   ├── index.md
│   │   ├── marquee.md
│   │   ├── progress.md
│   │   ├── qrcode.md
│   │   ├── span.md
│   │   └── text.md
│   ├── container
│   │   ├── div.md
│   │   ├── index.md
│   │   ├── list-item.md
│   │   ├── list.md
│   │   ├── scroll.md
│   │   ├── stack.md
│   │   └── swiper.md
│   ├── form
│   │   ├── index.md
│   │   ├── input.md
│   │   ├── picker.md
│   │   ├── slider.md
│   │   └── switch.md
│   ├── general
│   │   ├── animation-style.md
│   │   ├── background-img-styles.md
│   │   ├── color.md
│   │   ├── events.md
│   │   ├── index.md
│   │   ├── methods.md
│   │   ├── properties.md
│   │   └── style.md
│   └── index.md
├── features
│   ├── basic
│   │   ├── app.md
│   │   ├── configuration.md
│   │   ├── device.md
│   │   ├── index.md
│   │   └── router.md
│   ├── data
│   │   ├── file.md
│   │   ├── index.md
│   │   └── storage.md
│   ├── grammar.md
│   ├── index.md
│   ├── network
│   │   ├── fetch.md
│   │   ├── index.md
│   │   ├── interconnect.md
│   │   ├── request.md
│   │   └── uploadtask.md
│   ├── other
│   │   ├── audio.md
│   │   ├── index.md
│   │   └── prompt.md
│   ├── security
│   │   ├── cipher.md
│   │   ├── crypto.md
│   │   └── index.md
│   └── system
│       ├── battery.md
│       ├── brightness.md
│       ├── event.md
│       ├── geolocation.md
│       ├── index.md
│       ├── network.md
│       ├── record.md
│       ├── sensor.md
│       └── vibrator.md
├── guide
│   ├── best-practice
│   │   ├── business.md
│   │   ├── index.md
│   │   ├── memory.md
│   │   └── start.md
│   ├── design
│   │   ├── index.md
│   │   └── multi-screens.md
│   ├── developer-materials
│   │   ├── extension-components.md
│   │   └── index.md
│   ├── framework
│   │   ├── index.md
│   │   ├── manifest.md
│   │   ├── other
│   │   │   ├── background-running.md
│   │   │   ├── hap-schema.md
│   │   │   ├── i18n.md
│   │   │   ├── index.md
│   │   │   ├── language-list.md
│   │   │   └── launch-mode.md
│   │   ├── page-switch.md
│   │   ├── project-structure.md
│   │   ├── script
│   │   │   ├── global-data-method.md
│   │   │   ├── index.md
│   │   │   ├── lifecycle.md
│   │   │   └── page-data.md
│   │   ├── style
│   │   │   ├── index.md
│   │   │   ├── media-query.md
│   │   │   └── page-style-and-layout.md
│   │   ├── template
│   │   │   ├── component.md
│   │   │   ├── computed.md
│   │   │   ├── event.md
│   │   │   ├── for.md
│   │   │   ├── if.md
│   │   │   ├── index.md
│   │   │   └── Props.md
│   │   └── ux.md
│   ├── index.md
│   ├── multi-screens
│   │   ├── conditional-compilation.md
│   │   ├── index.md
│   │   ├── samples.md
│   │   └── specs.md
│   ├── other
│   │   ├── faq.md
│   │   └── tips.md
│   ├── publish
│   │   ├── acceptance-criteria.md
│   │   └── index.md
│   ├── start
│   │   ├── add-interactivity.md
│   │   ├── data-fetch.md
│   │   ├── index.md
│   │   ├── project-overview.md
│   │   ├── toolkit-params.md
│   │   ├── use-ide.md
│   │   └── user-interface.md
│   ├── start.md
│   └── version
│       ├── APILevel2.md
│       ├── APILevel3.md
│       ├── APILevel4.md
│       └── index.md
├── images
├── index.md
├── samples
│   └── index.md
├── tools
│   ├── debug
│   │   ├── debug.md
│   │   ├── memory.md
│   │   ├── multi-screens.md
│   │   ├── start.md
│   │   └── watch-log.md
│   ├── dev
│   │   ├── build.md
│   │   ├── format.md
│   │   └── start.md
│   ├── emulator
│   │   ├── create-emulator.md
│   │   └── emulator-run.md
│   ├── index.md
│   ├── project
│   │   ├── creat-project.md
│   │   ├── project.md
│   │   └── template.md
│   ├── release
│   │   ├── release.md
│   │   └── start.md
│   ├── start
│   │   └── project.md
│   └── toolkit
│       ├── start.md
│       └── update.md
├── vela
│   └── quickapp
│       └── index.md
└── zh
    └── components.md

40 directories, 277 files
```
## 环境要求

- Python 3.x
- 第三方依赖：
  - requests
  - beautifulsoup4
  - html2text

## 使用步骤

1. **创建并激活虚拟环境**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **安装依赖**

   如果有 `requirements.txt`，执行：
   
   ```bash
   pip install -r requirements.txt
   ```
   
   或者手动安装：
   
   ```bash
   pip install requests beautifulsoup4 html2text
   ```

3. **运行爬虫脚本**

   ```bash
   python docs.py https://iot.mi.com/vela/quickapp/zh -o docs
   ```
   
   参数说明：
   - 第一个参数为基础 URL，例如 `https://iot.mi.com/vela/quickapp/zh`
   - `-o` 指定输出目录（默认为 `docs`）

## 常见问题

- **图片路径问题**  
  爬虫默认下载图片时会保持源文件名，如需调整图片引用路径，可修改 `download_asset` 或 `save_markdown_file` 方法，确保生成的 Markdown 文件中的图片路径正确（如相对引用）。

- **内容过滤问题**  
  如果抓取的 Markdown 文档中仍包含不需要的导航栏内容，请检查 `convert_html_to_markdown` 方法中是否正确移除了 `<header class="navbar">` 和 `<aside class="sidebar">` 部分。

## 许可
 docs来自小米vela官方文档，爬取下来供开发者使用，仅用于学习交流。