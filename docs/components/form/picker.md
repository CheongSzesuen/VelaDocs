<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/form/picker.html -->

# # picker

## # 概述

滚动选择器，目前支持两种选择器，普通选择器，时间选择器。默认为普通选择器。 

## # 子组件

不支持

## # 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

**普通选择器**

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
type | text | - | 是 | 不支持动态修改  
range | `<array>` | - | 否 | 选择器的取值范围  
selected | `<number>` | 0 | 否 | 选择器的默认取值，取值为 range 的索引  
  
**时间选择器**

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
type | time | - | 是 | 不支持动态修改  
selected | `<string>` | 当前时间 | 否 | 选择器的默认取值，格式为 hh:mm  
  
## # 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
color | `<color>` | 主题色 | 否 | 候选项字体颜色  
font-size | `<length>` | 30px | 否 | 候选项字体尺寸，单位px  
selected-color | `<length>` | #ffffff | 否 | 选中项字体颜色  
selected-font-size | `<length>` | 20px | 否 | 选中项字体尺寸，单位px  
selected-background-color | `<color>` | - | 否 | 选中项背景颜色  
  
## # 事件

**普通选择器**

名称 | 参数 | 描述  
---|---|---  
change | {newValue:newValue, newSelected:newSelected} | 滚动选择器选择值后确定时触发（newSelected 为索引）  
  
**时间选择器**

名称 | 参数 | 描述  
---|---|---  
change | {hour:hour, minute:minute} | 滚动选择器选择值后确定时触发  
  
## # 示例代码

``` <template> <div class="page"> <text class="title">普通picker</text> <picker class="picker" type="text" range="{{pickerList}}" selected="1" onchange="onPickerChange"> </picker> <text class="value">选择的值：{{v1}}</text> <text class="title">时间picker</text> <picker class="picker" type="time" selected="12:00" onchange="onTimePickerChange"> </picker> <text class="value">选择的值：{{v2}}</text> </div> </template> <script> export default { private: { pickerList: ['apple', 'peach', 'pear', 'banana'], v1: 'peach', v2: '12:00' }, onPickerChange(e) { this.v1 = e.newValue; }, onTimePickerChange(e) { this.v2 = e.hour + ':' + e.minute; } } </script> <style> .page { flex-direction: column; padding: 30px; background-color: #ffffff; } .title { font-weight: bold; color: #000; } .value { margin-top: 5px; margin-bottom: 30px; color: #090; } .picker { font-size: 25px; color: #000; selected-font-size: 30px; selected-color: #09f; selected-background-color: #ccc; } </style> ```

![](../../images/picker.5b1be30e.gif)
