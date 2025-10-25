<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/basic/chart.html -->

# chart

## 概述

图表组件，用于呈现线形图、柱状图界面。

## 子组件

不支持

## 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
type | `<string>` | line | 否 | 设置图表类型（不支持动态修改），可选项有：bar（柱状图） \ line（线形图）  
options | ChartOptions |:---:| 是 | 图表参数设置，柱状图和线形图必须设置参数。可以设置x轴、y轴的最小值、最大值、刻度数、是否显示、线条宽度、是否平滑等。（不支持动态修改）  
datasets | Array<ChartDataset> |:---:| 是 | 数据集合，柱状图和线形图必须设置，可以设置多条数据集及其背景色  
  
### ChartOptions 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
xAxis | ChartAxis | line | 是 | x轴参数设置。可以设置x轴最小值、最大值、刻度数以及是否显示  
yAxis | ChartAxis |:---:| 是 | y轴参数设置。可以设置y轴最小值、最大值、刻度数以及是否显示  
series | ChartSeries |:---:| 否 | 数据序列参数设置。可以设置 1）线的样式，如线宽、是否平滑；2）设置线最前端位置白点的样式和大小（仅线形图支持）  
  
### ChartDataset 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
strokeColor | `<color>` | #ff6384 | 否 | 线条颜色。（仅线形图支持）  
fillColor | `<color>` | #ff6384 | 否 | 填充颜色。线形图表示填充的渐变颜色  
data | Array<`<number`> |:---:| 是 | 设置绘制线或柱中的点集  
gradient | `<boolean>` | false | 否 | 设置是否显示填充渐变颜色。（仅线形图支持）  
  
### ChartAxis 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
min | `<number>` | 0 | 否 | 轴的最小值。（不支持负数。仅线形图支持）  
max | `<number>` | dataset 数据个数-1 | 否 | 轴的最大值。（不支持负数。仅线形图支持）  
axisTick | `<number>` | 10 | 否 | 轴显示的刻度数量。（仅支持1~20，且具体显示的效果与如下计算值有关（图的宽度所占的像素/（max-min））。因轻量级智能穿戴为整型运行，在除不尽的情况下会有误差产生，具体的表现形式是x轴末尾可能会空出一段。在柱状图中，每组数据显示的柱子数量与刻度数量一致，且柱子显示在刻度处。）  
display | `<boolean>` | false | 否 | 是否显示轴  
color | `<color>` | #c0c0c0 | 否 | 轴颜色  
  
### ChartSeries 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
lineStyle | ChartLineStyle |:---:| 否 | 线样式设置，如线宽、是否平滑  
loop | ChartLoop |:---:| 否 | 设置屏幕显示满时，是否需要重头开始绘制  
  
### ChartLineStyle 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
width | `<length>` | 2px | 否 | 线宽设置  
  
### ChartLoop 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
margin | `<length>` | 1px | 否 | 擦除点的个数（最新绘制的点与最老的点之间的横向距离）。注意：轻量设备margin和topPoint/bottomPoint/headPoint同时使用时，有概率出现point正好位于擦除区域的情况，导致point不可见，因此不建议同时使用  
  
## 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

## 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

## 示例代码

### 线形图
```html
< template > < chart type = " line " options = " {{lineOpts}} " datasets = " {{lineData}} " > </ chart > </ template > < script > export default { data : { lineData : [ { strokeColor : '#f07826' , data : [ 763 , 550 , 551 , 554 , 731 , 654 , 525 , 696 , 595 , 628 ] , } , { strokeColor : '#cce5ff' , fillColor : '#cce5ff' , data : [ 535 , 776 , 615 , 444 , 694 , 785 , 677 , 609 , 562 , 410 ] , } , { strokeColor : '#ff88bb' , data : [ 673 , 500 , 574 , 483 , 702 , 583 , 437 , 506 , 693 , 657 ] } , ] , lineOpts : { xAxis : { min : 0 , max : 10 , display : true , axisTick : 10 } , yAxis : { min : 400 , max : 900 , display : true , } } } } </ script >
```

![](../../images/line-chart.png)

### 柱状图
```html
< template > < chart type = " bar " options = " {{barOpts}} " datasets = " {{barData}} " > </ chart > </ template > < script > export default { data : { barData : [ { fillColor : '#f07826' , data : [ 763 , 550 , 551 , 554 , 731 , 654 , 525 ] } , { fillColor : '#cce5ff' , data : [ 535 , 776 , 615 , 444 , 694 , 785 , 677 ] } ] , barOpts : { xAxis : { min : 0 , max : 7 , display : false , axisTick : 7 } , yAxis : { min : 0 , max : 800 , display : false , } } } } </ script >
```

![](../../images/bar-chart.png)
