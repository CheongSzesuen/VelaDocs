<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/start/project-overview.html -->

# 项目概览

本章节基于[安装环境](</vela/quickapp/zh/guide/start/use-ide.html>)中初始化的项目，介绍 Vela JS 应用项目各部分的作用。

## 目录结构

典型的项目目录结构如下：

```bash
├── README.md            # 项目说明文件
├── package.json         # 项目配置文件
├── build/               # 构建中间产物
├── dist/                # 最终构建产物
├── sign/                # 签名文件
│   ├── certificate.pem
│   └── private.pem
└── src/                 # 源码目录
    ├── app.ux           # 应用入口文件
    ├── manifest.json    # 项目配置文件
    ├── common/          # 公共资源目录
    │   ├── components/  # 组件目录
    │   │   └── button.ux
    │   ├── images/      # 图片目录
    │   │   └── logo.png
    │   └── scripts/     # 脚本目录
    │       └── index.js
    ├── i18n/            # 多语言配置目录
    │   ├── defaults.json
    │   ├── en.json
    │   └── zh-CN.json
    └── pages/           # 页面目录
        ├── detail/detail.ux
        └── index/index.ux
```

## 各目录说明

### src/

源码目录，所有应用代码都放在这里。`src/` 是固定的目录名称，不可更改。

### src/manifest.json

项目配置文件，用于声明应用基本信息（包名、版本等）、系统接口权限以及页面路由。详细字段说明参考[项目配置](</vela/quickapp/zh/guide/framework/manifest.html>)。

### src/app.ux

应用入口文件，用于定义应用级别的生命周期回调、全局数据和全局方法。详细用法参考 [app.ux](</vela/quickapp/zh/guide/framework/ux.html#appux>)。

### src/pages/

页面目录，每个页面对应一个子目录。页面由 ux 文件描述，也可以将样式和逻辑拆分为独立的 css/js 文件。详细说明参考[项目结构](</vela/quickapp/zh/guide/framework/project-structure.html>)。

### src/common/

公共资源目录，用于存放跨页面共享的组件、图片、脚本和样式等资源。

### src/i18n/

多语言配置目录，存放各语言对应的 JSON 文件，用于实现应用的国际化。详细用法参考[多语言](</vela/quickapp/zh/guide/framework/other/i18n.html>)。

### build/ 和 dist/

`build/` 存放构建过程中的中间产物，`dist/` 存放最终的构建输出文件（rpk 包）。这两个目录由构建工具自动生成，无需手动维护。

### sign/

签名文件目录，包含 `certificate.pem`（证书）和 `private.pem`（私钥），用于对应用包进行签名。

### package.json

项目的 npm 配置文件，定义项目依赖和构建脚本。
