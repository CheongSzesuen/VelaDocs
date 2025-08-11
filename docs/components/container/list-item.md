<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/container/list-item.html -->

# # list-item

## # 概述

[`<list>`](</vela/quickapp/zh/components/container/list.html>)的子组件，用来展示列表具体 item，宽度默认充满 list 组件。

## # 子组件

支持

## # 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
type | `<string>` | - | 是 | list-item 类型，值为自定义的字符串，如'loadMore'。**相同的 type 的 list-item 必须具备完全一致的 DOM 结构** 。因此，在 list-item 内部需谨慎使用 if 和 for，因为 if 和 for 可能造成相同的 type 的 list-item 的 DOM 结构不一致，从而引发错误  
  
## # 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

为了达到组件复用、优化性能的目的，请显示指定宽度和高度。

## # 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

## # 示例代码

``` <template> <div class="page"> <list class="list"> <list-item for="{{productList}}" class="item" type="list-item"> <text>{{$item.name}}: {{$item.price}}</text> </list-item> </list> </div> </template> <script> export default { data: { productList: [ { name: '衣服', price: '100' }, { name: '裤子', price: '200' } ], } } </script> <style> .page { padding: 30px; background-color: white; } .list { width: 100%; height: 100%; } .item { height: 40px; } </style> ```

### # 效果展示

![](../../data:image/png;base64,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)
