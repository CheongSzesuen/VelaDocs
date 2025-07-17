<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/basic/marquee.html -->

# # marquee

## # 概述

跑马灯，用来插入一段滚动的文字，默认为单行。

## # 子组件

不支持

## # 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
scrollamount | `<number>` | 6 | 否 | 设置每次滚动时移动的长度，单位：px  
loop | `<number>` | -1 | 否 | 设置 marquee 滚动的次数。如果未指定值，默认值为 −1，表示 marquee 将连续滚动  
direction | `<string>` | left | 否 | 文字滚动方向，支持 left，right  
text-offset | `<number>` | - | 否 | 设置跑马灯首尾相接时，上一段的尾和下一段的头之间的距离，属性值为大于 0 的整数，单位：px  
  
## # 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
color | `<color>` | rgba(0, 0, 0, 0.54) | 否 | 文本颜色  
font-size | `<length>` | 30px | 否 | 文本尺寸  
  
## # 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

名称 | 参数 | 描述  
---|---|---  
bounce | - | 当 marquee 滚动到结尾时触发  
finish | - | 当 marquee 完成设置的 loop 次数时触发，loop > 0 时有效  
start | - | 当 marquee 开始滚动时触发  
  
## # 方法

名称 | 参数 | 描述  
---|---|---  
start | - | 开始滚动 marquee  
stop | - | 停止滚动 marquee  
  
## # 示例代码

``` <template> <div> <marquee id="marquee" scrollamount={{6}} loop={{-1}}> scrollamount控制滚动速度，默认值为6（6像素/秒） </marquee> </div> </template> <script> export default { onReady() { this.$element('marquee').start() } } </script> ```

![](../../images/marquee.2b33a67c.gif)

← [ progress ](</vela/quickapp/zh/components/basic/progress.html>) [ chart ](</vela/quickapp/zh/components/basic/chart.html>) → 

快速导航

概述

子组件

属性

样式

事件

方法

示例代码
