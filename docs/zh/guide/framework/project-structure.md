<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/project-structure.html -->

# 项目结构

## 应用资源

一个应用包含：描述项目配置信息的 [manifest 文件](</vela/quickapp/zh/guide/framework/manifest.html>)，放置项目公共资源脚本的 [app.ux 文件](</vela/quickapp/zh/guide/framework/ux.html>)，以及多个描述页面的 [ux 文件](</vela/quickapp/zh/guide/framework/ux.html>)。应用的源码统一放在 `src/` 目录下，典型结构如下：

```
src/
├── manifest.json
├── app.ux
├── pages
│   ├── index
|   |   └── index.ux
│   └── detail
|       └── detail.ux
├── i18n
|   ├── defaults.json
|   ├── zh-CN.json
|   └── en-US.json
└── common
    ├── style.css
    ├── utils.js
    └── logo.png
```

提示

完整的项目目录结构（含 build、dist、sign 等）请参考[项目概览](</vela/quickapp/zh/guide/start/project-overview.html>)。

## ux 模板

一个页面通常由三部分组成：页面结构、样式和逻辑交互。这三部分可以放在一个 ux 文件中，也可以作为独立的文件。

如果放在一个 ux 文件中，则需要包含 `template`、`style` 和 `script` 三个标签：

```html
<template>
  <div class="page">
    <text class="title">欢迎打开{{title}}</text>
    <input class="btn" type="button" value="跳转到详情页" onclick="routeDetail">
  </div>
</template>

<style>
  .btn {
    width: 400px;
    height: 60px;
    background-color: #09ba07;
    color: #ffffff;
  }
</style>

<script>
  import router from '@system.router'

  export default {
    private: {
      title: '示例页面'
    },
    routeDetail() {
      router.push({
        uri: '/pages/detail'
      })
    }
  }
</script>
```

如果将页面结构、样式和逻辑交互拆分为独立文件，目录结构如下：

```bash
├── pages
│   └── detail
|       ├── detail.ux
|       ├── detail.css
|       └── detail.js
```

说明

拆分为独立文件后，ux 文件中不能包含 `template` 标签。

## 文件存储

在应用平台中按分区存储文件，目前支持以下分区：

  1. **Cache** ：用于存储缓存文件，如通过 fetch 接口下载的文件。该分区中的文件可能因存储空间不足被系统删除。
  2. **Files** ：用于存储较小的永久文件，由应用自行管理。
  3. **Mass** ：用于存储较大的文件，但该分区不保证一直可用。
  4. **Temp** ：从外部映射的临时文件，只读，只能通过特定 API 获取（如 file.readText）。应用重启后无法访问，需重新获取。

另外，应用资源也作为一个特殊的只读分区进行处理。

## URI

URI 用于标识应用资源和文件，[组件](</vela/quickapp/zh/components/>)和[接口](</vela/quickapp/zh/features/>)通过 URI 来访问应用资源和文件。

资源类型 | URI | 只读 | 示例 | 说明
---|---|---|---|---
应用资源 | /path | 是 | /Common/header.png | -
Cache | internal://cache/path | 否 | internal://cache/fetch-123456.png | -
Files | internal://files/path | 否 | internal://files/image/demo.png | -
Mass | internal://mass/path | 否 | internal://mass/video/demo.mp4 | -
Temp | internal://tmp/path | 是 | internal://tmp/xxxxx | 由系统动态生成 

URI 允许的字符是 `0-9a-zA-Z_-./%:`（不包含引号），URI 中不能出现 `..`，目录由斜线 `/` 分隔。

internal URI 表示应用私有文件，无需指定应用标识，同一个 internal URI 对于不同应用会指向不同的文件。

## 资源和文件访问规则

应用资源路径分为绝对路径和相对路径：以 `/` 开头的为绝对路径（如 `/Common/a.png`），否则为相对路径（如 `a.png`、`../Common/a.png`）。

应用资源文件分为代码文件（.js/.css/.ux）和资源文件（图片、视频等），访问规则如下：

  1. 导入其他代码文件时，使用相对路径，如：`../Common/component.ux`；
  2. 引用资源文件时，一般使用相对路径，如：`./abc.png`；
  3. 当代码文件被其他文件导入时，如果两者不在同一目录，被导入文件中引用的资源必须使用绝对路径（因为编译时被导入文件会被复制到导入文件所在目录，相对路径会失效）。例如 `a.css` 被 `b.ux` 导入，若不在同一目录，`a.css` 中必须写 `/Common/abc.png`；
  4. 在 CSS 中使用 `url(PATH)` 访问资源文件，如：`url(/Common/abc.png)`。
