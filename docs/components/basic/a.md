<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/basic/a.html -->

# # a

## # 概述

超链接（默认不带下划线）

## # 子组件

仅支持[`<span>`](</vela/quickapp/zh/components/basic/span.html>)

## # 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
href | `string` | - | 否 | 支持的格式参见[页面路由](</vela/quickapp/zh/features/basic/router.html>)中的 uri 参数。  
额外的：  
href 还可以通过“?param1=value1”的方式添加参数，参数可以在页面中通过`this.param1`的方式使用。使用`this.param1`变量时，需要在目标页面中在 `public`（应用外传参）或 `protected`（应用内传参）下定义 key 名相同的属性  
示例：  
`<a href="/about?param1=value1">关于</a>`  
  
## # 样式

支持[text样式](</vela/quickapp/zh/components/basic/text.html>)

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

## # 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

## # 示例代码

``` <template> <div> <a class="link" href="/home">goHome</a> <a href="/home"> <span class="link">使用span子组件</span> </a> </div> </template> ```

← [ span ](</vela/quickapp/zh/components/basic/span.html>) [ image ](</vela/quickapp/zh/components/basic/image.html>) → 

快速导航

概述

子组件

属性

样式

事件

示例代码
