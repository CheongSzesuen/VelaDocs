<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/start/project-overview.html -->

# Project Structure

This chapter explains the role of each part in a Vela JS application project based on the project initialized in [Environment Setup](</vela/quickapp/en/guide/start/use-ide.html>).

## Directory Structure

A Vela JS application project consists of configuration files (manifest.json), template code (ux files), style code (css files), logic code (js files), and resource files (images, audio, etc.).

A typical project directory structure is as follows:

```bash
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

## Configuration File

The `manifest.json` file in the project root directory is the configuration file for the project. Information such as application information, system interfaces used, and page routes need to be declared in this configuration file.

For detailed configuration field descriptions, refer to [Project Configuration](</vela/quickapp/zh/guide/framework/manifest.html>).

## ux Template

A page usually consists of three parts: page structure, style, and logic interaction. These three parts can be placed in a single ux file or as separate files.

If placed in a single ux file, the ux file needs to include three tags: `template`, `style`, and `script`.

Example:

```html
<template>
  <div class="page">
    <text class="title">Welcome to {{title}}</text>
    <input class="btn" type="button" value="Jump to detail page" onclick="routeDetail">
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
    // Page data object
    private: {
      title: 'Example Page'
    },
    // Callback after button click
    routeDetail() {
      router.push({
        uri: '/pages/detail'
      })
    }
  }
</script>
```

If the page structure, style, and logic interaction are separated into independent files, the following directory structure can be used:

```bash
├── ...
├── pages
│   ├── ...
│   └── detail
|       ├── detail.ux
|       ├── detail.css
|       └── detail.js
├── ...
```

Note

If separated into independent files (ux/css/js), the ux file cannot contain the `template` tag.

## app.ux

`app.ux` is used to define the App's lifecycle, global data, or global methods.

For detailed usage methods, refer to [app.ux](</vela/quickapp/zh/guide/framework/ux.html#appux>).

## common

The `common` folder is mainly used to store public resources such as images, audio, and public styles.

## i18n

The `i18n` folder is used to store multilingual configuration files.
