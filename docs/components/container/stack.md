<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/container/stack.html -->

# # stack

## # 概述

基本容器，子组件排列方式为层叠排列，每个直接子组件按照先后顺序依次堆叠，覆盖前一个子组件。

## # 子组件

支持

## # 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

## # 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

## # 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

## # 示例代码

``` <template> <div class="page"> <stack class="stack"> <div class="box box1"></div> <div class="box box2"></div> <div class="box box3"></div> <div class="box box4"></div> </stack> </div> </template> <style> .page { padding: 30px; background-color: white; } .box { border-radius: 8px; width: 100px; height: 100px; } .box1 { width: 200px; height: 200px; background-color: #3f56ea; } .box2 { left: 20px; top: 20px; background-color: #00bfc9; } .box3 { left: 50px; top: 50px; background-color: #47cc47; } .box4 { left: 80px; top: 80px; background-color: #FF6A00; } </style> ```

![](../../data:image/png;base64,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)
