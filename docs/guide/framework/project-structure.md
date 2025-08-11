<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/project-structure.html -->

# # 项目结构

## # 应用资源

一个应用包含：描述项目配置信息的[manifest 文件](</vela/quickapp/zh/guide/framework/manifest.html>)，放置项目公共资源脚本的[app.ux 文件](</vela/quickapp/zh/guide/framework/ux.html>)，多个描述页面的[ux 文件](</vela/quickapp/zh/guide/framework/ux.html>)，典型示例如下：

应用根目录：

``` ├── manifest.json ├── app.ux ├── pages │ ├── index | | └── index.ux │ └── detail | └── detail.ux ├── i18n | ├── defaults.json | ├── zh-CN.json | └── en-US.json └── common ├── style.css ├── utils.js └── logo.png ```

## # ux模板

一个页面通常都由三部分组成：页面结构、样式和逻辑交互。这三部分，可以放在一个ux文件中，也可以作为独立的文件。

如果放在一个ux文件中，则ux文件需要包含三标签：`template`、`style`和`script`。

示例：

``` <template> <div class="page"> <text class="title">欢迎打开{{title}}</text> <input class="btn" type="button" value="跳转到详情页" onclick="routeDetail"> </div> </template> <style> .btn { width: 400px; height: 60px; background-color: #09ba07; color: #ffffff; } </style> <script> import router from '@system.router' export default { // 页面数据对象 private: { title: '示例页面' }, // 按钮点击后的回调 routeDetail() { router.push({ uri: '/pages/detail' }) } } </script> ```

如果将页面结构、样式和逻辑交互分开作为独立的文件，可以使用如下目录结构：

``` ├── ... ├── pages │ ├── ... │ └── detail | ├── detail.ux | ├── detail.css | └── detail.js ├── ... ```

说明

如果作为独立的文件，将ux/css/js文件分开后，ux文件中不能包含`template`标签。

## # 文件存储

在应用平台中是按分区来存储文件的，目前支持以下分区：

  1. Cache，一般用于存储缓存文件，比如通过 fetch 接口下载的文件会存储在该分区中，该分区中的文件可能因存储空间不够被系统删除；
  2. Files，一般用于存储比较小的永久文件，该分区中的文件由应用自己管理；
  3. Mass，一般用于存储比较大的文件，但该分区并不保证一直可用；
  4. Temp，表示从外部映射过来的临时文件，出于安全性考虑，临时文件是只读的，并且只能通过调用特定的 API 获取，比如 file.readText 方法。另外临时文件的访问是临时的，应用重启后无法访问到临时文件，需要通过特定 API 重新获取。

另外应用资源也作为一个特殊的只读分区进行处理。

## # URI

URI 用于标识应用资源和文件，[组件](</vela/quickapp/zh/components/>)和[接口](</vela/quickapp/zh/features/>)通过 URI 来访问应用资源和文件。

资源类型 | URI | 只读 | 示例 | 说明  
---|---|---|---|---  
应用资源 | /path | 是 | /Common/header.png | -  
Cache | internal://cache/path | 否 | internal://cache/fetch-123456.png | -  
Files | internal://files/path | 否 | internal://files/image/demo.png | -  
Mass | internal://mass/path | 否 | internal://mass/video/demo.mp4 | -  
Temp | internal://tmp/path | 是 | internal://tmp/xxxxx | 由系统动态生成  
  
URI 允许的字符是`0-9a-zA-Z_-./%:`(不包含引号)，URI 中不能出现`..`，URI 支持目录结构，目录由斜线'/'分隔。

internal URI 表示的是应用私有文件，即在指定 internal URI 时，无需指定应用标识，同一个 internal URI 对于不同的应用会指向不同的文件。

## # 资源和文件访问规则

应用资源路径分为绝对路径和相对路径，以"/"开头的路径表示绝对路径，比如 /Common/a.png，不以"/"开头的路径是相对路径，比如 a.png 和 ../Common/a.png 等。

应用资源文件分为代码文件和资源文件，代码文件是指 .js/.css/.ux 等包含代码的文件，其他文件则是资源文件，这类文件一般只当作数据来使用，比如图片、视频等。

  1. 在代码文件中，导入其他代码文件时，使用相对路径，比如：../Common/component.ux；
  2. 在代码文件中，引用资源文件(如：图片、视频等)时，一般情况下使用相对路径，比如：./abc.png；
  3. 当代码文件需要被导入时，如果导入文件与被导入文件在同一个目录，被导入文件引用资源文件时可以使用相对路径，但如果不在同一目录，必须使用绝对路径，因为被导入文件编译时会被复制到导入文件中，编译后目录会发生变化。比如 a.css 文件被 b.ux 导入，如果 a.css 与 b.ux 在同一个目录，a.css 引用资源文件时可以写相对路径：abc.png，如果不在同一个目录，必须写绝对路径：/Common/abc.png，再比如当 a.ux 文件被 b.ux 文件导入时，如果 a.ux 与 b.ux 在同一个目录，a.ux 引用资源文件时可以写相对路径：a.png，如果不在同一个目录，a.ux 引用资源必须写绝对路径：/Common/abc.png；
  4. 在 CSS 中，与前端开发一致，使用 url(PATH)的方式访问资源文件，如：url(/Common/abc.png)。

