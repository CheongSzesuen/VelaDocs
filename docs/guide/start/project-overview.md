<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/start/project-overview.html -->

# 项目结构

这个章节将基于[安装环境](</vela/quickapp/zh/guide/start/use-ide.html>)中初始化的项目， 来讲解 Vela JS 应用项目中的各部分的作用。

## 目录结构

Vela JS 应用项目由配置文件（manifest.json）、模板代码（ux文件）、 样式代码（css文件）、逻辑代码（js文件）以及资源文件（图片、音频等）组成。

典型的项目目录结构如下：
```bash
├── manifest.json ├── app.ux ├── pages │ ├── index | | └── index.ux │ └── detail | └── detail.ux ├── i18n | ├── defaults.json | ├── zh-CN.json | └── en-US.json └── common ├── style.css ├── utils.js └── logo.png
```

## 配置文件

项目根目录中的`manifest.json`文件为项目的配置文件，应用信息、使用到的系统接口以及页面路由等信息需要在这个配置文件中声明。

详细配置字段说明可以参考[项目配置](</vela/quickapp/zh/guide/framework/manifest.html>)。

## ux模板

一个页面通常都由三部分组成：页面结构、样式和逻辑交互。这三部分，可以放在一个ux文件中，也可以作为独立的文件。

如果放在一个ux文件中，则ux文件需要包含三标签：`template`、`style`和`script`。

示例：
```html
< template > < div class = " page " > < text class = " title " > 欢迎打开{{title}} </ text > < input class = " btn " type = " button " value = " 跳转到详情页 " onclick = " routeDetail " > </ div > </ template > < style > .btn { width : 400px ; height : 60px ; background-color : #09ba07 ; color : #ffffff ; } </ style > < script > import router from '@system.router' export default { // 页面数据对象 private : { title : '示例页面' } , // 按钮点击后的回调 routeDetail () { router.push ({ uri : '/pages/detail' }) } } </ script >
```

如果将页面结构、样式和逻辑交互分开作为独立的文件，可以使用如下目录结构：
```bash
├── .. . ├── pages │ ├── .. . │ └── detail | ├── detail.ux | ├── detail.css | └── detail.js ├── .. .
```

说明

如果作为独立的文件，将ux/css/js文件分开后，ux文件中不能包含`template`标签。

## app.ux

`app.ux`用于定义App的生命周期、全局数据或者全局方法。

详细使用方法可以参考[app.ux](</vela/quickapp/zh/guide/framework/ux.html#appux>)。

## common

`common`文件夹主要用来存放公共的资源，比如图片、音频和公共样式等。

## i18n

`i18n`文件夹用来存放多语言配置文件。
