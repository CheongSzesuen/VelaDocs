<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/container/div.html -->

# # div

## # 概述

基础容器，用作页面结构的根节点或将内容进行分组。

## # 子组件

支持

## # 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

## # 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

## # 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

## # 示例代码

``` <template> <div class="page"> <div style="flex-direction: row;"> <text class="item color-1">1</text> <text class="item color-2">2</text> <text class="item color-3">3</text> </div> </div> </template> <style> .page { margin: 20px; flex-direction: column; background-color: white; } .item { height: 100px; width: 100px; text-align: center; margin-right: 10px; } .color-1 { background-color: #09ba07; } .color-2 { background-color: #f76160; } .color-3 { background-color: #0faeff; } </style> ```

![](../../data:image/png;base64,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)

← [ 通用方法 ](</vela/quickapp/zh/components/general/methods.html>) [ list ](</vela/quickapp/zh/components/container/list.html>) → 

快速导航

概述

子组件

属性

样式

事件

示例代码
