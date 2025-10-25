<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/tools/ -->

# 关于AIoT-IDE

`AIoT-IDE` 是用于开发`Xiaomi Vela JS 应用`的官方集成开发环境。建立在 [Visual Studio Code (opens new window)](<https://code.visualstudio.com/>)（以下简称 VS Code）的基础上，它继承了 VS Code 的全部功能，比如**代码编辑** 、**插件集成** 、**主题定制** 及个性化设置。此外，`AIoT-IDE` 还引入了一系列专门针对 `Xiaomi Vela JS 应用` 应用开发的增强功能，它们包括但不限于：

  * 智能编码提示
  * Vela JS应用调试
  * 实时编译预览
  * Vela JS应用 打包发布
  * Vela JS应用 真机调试

本章主要介绍 `AIoT-IDE` 的核心功能。如需下载安装请查看，请直接访问 [安装环境](</vela/quickapp/zh/guide/start/use-ide.html>) 章节。

## 项目结构

只有当`AIoT-IDE`打开`Xiaomi Vela JS 应用`，才能使用应用开发的增强功能。

一个最基本的`Xiaomi Vela JS 应用`由描述项目信息配置文件`mainfest.json`和放置项目公交资源的`app.ux`文件，不同描述页面的ux文件。
```bash
├── manifest.json ├── app.ux ├── pages │ ├── index | | └── index.ux │ └── detail | └── detail.ux ├── i18n | ├── defaults.json | ├── zh-CN.json | └── en-US.json └── common ├── style.css ├── utils.js └── logo.png
```

当`AIoT-IDE`打开一个项目时会判断当前项目的**根目录** 或者**src目录** 下是否有`mainfest.json`文件，如果有则会读取`mainfest.json`中的**deviceTypeList** ，通过**deviceTypeList** 字段的内容判断当前项目是什么类型的`Xiaomi Vela JS应用`。
