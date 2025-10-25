<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/other/hap-schema.html -->

# hap 链接

hap链接 指在router模块中支持的以hap://开头的uri，使用场景见[页面路由](</vela/quickapp/zh/features/basic/router.html>)。

目前支持的 hap 链接以`hap://app/`开头，支持打开指定的JS 应用，格式如下：

`hap://app/<package>/[path][?key=value]`

参数说明：

  * package: 应用包名，必选
  * path: 应用内页面的 path，可选，默认为首页
  * key-value: 希望传给页面的参数，可选，可以有多个

