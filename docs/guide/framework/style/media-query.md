<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/style/media-query.html -->

# # 媒体查询[2+](</vela/quickapp/zh/guide/version/APILevel2>)

通过媒体查询(media query)，开发者可以根据各种设备特征和参数的值或者是否存在来调整JS 应用的样式。

媒体查询是响应式设计的一部分。和 css 类似，可使用 @media at-rule 根据媒体查询的结果，有条件地应用样式表的一部分；也可使用 @import 有条件地应用整个样式表。

aiot-toolkit最低版本：1.1.3

## # 语法

每条媒体查询语句都由一个可选的媒体类型和任意数量的媒体特性表达式构成，可以使用多种逻辑操作符合并多条媒体查询语句，媒体查询语句不区分大小写。

有两种方法可以执行媒体查询：

### # @media 方式引入媒体查询

``` @media [media type] [and|not|only] [(media feature)] { CSS-Code; } ```

### # 举例

  * @media (max-width: 30) { ... } // level3的写法。
  * @media (width <= 30) { ... } // level4的写法，比level3更清晰简洁。
  * @media screen and (min-width: 400) and (max-width: 700) { ... } // 多条件写法。
  * @media (400 <= width <= 700) { ... } // 多条件level4写法。

### # @import 方式引入媒体查询[3+](</vela/quickapp/zh/guide/version/APILevel3>)

``` @import './css_file_name.css' [media type] [and|not|only] [(media feature) ]; ```

## # 媒体类型

媒体类型（Media types）描述设备的类别。除了在使用 not 或 only 逻辑操作符必须一并填上媒体类型；其他时候，媒体类型是可选择是否填入的。目前JS 应用支持的媒体类型如下：

媒体类型 | 简介  
---|---  
screen | 主要用于屏幕。  
  
## # 媒体特性

媒体特性表达式是完全可选的，它负责测试这些特性或特征是否存在、值为多少。

每条媒体特性表达式都必须用括号括起来。

目前JS 应用支持的媒体特性如下：

类型 | 描述 | 查询时是否需带单位 | 支持单位  
---|---|---|---  
height[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 定义输出设备中的页面可视区域高度 | 否 | dp  
min-height[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 定义输出设备中的页面可视区域最小高度 | 否 | dp  
max-height[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 定义输出设备中的页面可视区域最大高度 | 否 | dp  
width[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 定义输出设备中的页面可视区域宽度 | 否 | dp  
min-width[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 定义输出设备中的页面可视区域最小宽度 | 否 | dp  
max-width[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 定义输出设备中的页面可视区域最大宽度 | 否 | dp  
aspect-ratio[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 定义输出设备中的页面可见区域宽高比，比例值需要按照 x / y 的格式，例如 1 / 2 | 否 | 无  
min-aspect-ratio[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 定义输出设备中的页面可见区域最小宽高比，参数要求同上 | 否 | 无  
max-aspect-ratio[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 定义输出设备中的页面可见区域最大宽高比，参数要求同上 | 否 | 无  
device-type[3+](</vela/quickapp/zh/guide/version/APILevel3>) | device-type 的可选值为：watch、band、smartspeaker，默认值：watch | 否 | 无  
shape[2+](</vela/quickapp/zh/guide/version/APILevel2>) | 屏幕形状，可选值：circle、rect、pill-shaped[3+](</vela/quickapp/zh/guide/version/APILevel3>) | 否 | 无  
  
### # 注意

1.在媒体特性列表中，标记了“查询时不带单位”的媒体特性，如 width、height 的查询，都不带长度单位，且长度单位只能为dp

dp 数值 = 物理分辨率 / 设备像素比(device pixel ratio)

举例：一个设备分辨率为 480*480，设备像素比 = 2，屏幕宽度 = 480 像素 = 240dp

各设备数据参考

设备类型 | 设备型号 | 屏幕形状 | 屏幕尺寸 | 分辨率 | PPI | DPR | 水平DP值  
---|---|---|---|---|---|---|---  
手表 | Xiaomi Watch S1 Pro | 圆形 | 1.47英寸 | 480x480 | 326 | 2.0 | 240  
手表 | Xiaomi Watch H1 | 圆形 | 1.43英寸 | 466x466 | 326 | 2.0 | 233  
手表 | Xiaomi Watch S3 | 圆形 | 1.43英寸 | 466x466 | 326 | 2.0 | 233  
手环 | 小米手环8 Pro | 矩形 | 1.74英寸 | 336x480 | 336 | 2.1 | 168  
手环 | 小米手环9 | 胶囊形 | 1.62英寸 | 192x490 | 325 | 2.0 | 96  
  
示例代码：

``` //以下media query会在小米手环9生效，小米手环9的分辨率为：192*490，水平dp值为：96 @media (min-width: 80) and (max-width: 160) { .box { background-color: green; } } //以下media query会在小米手环8 Pro生效，小米手环8 Pro的分辨率为：336*480，水平dp值为：168 @media (min-width: 160) and (max-width: 200) { .box { background-color: yellow; } } //以下media query会在Xiaomi Watch S3手表生效，Xiaomi Watch S3手表的分辨率为：466*466，水平dp值为：233 @media (min-width: 200) and (max-width: 300) { .box { background-color: red; } } ```

## # 逻辑操作符[3+](</vela/quickapp/zh/guide/version/APILevel3>)

开发者可以使用逻辑操作符组合多个媒体特性的查询条件，编写复杂的媒体查询。

类型 | 描述  
---|---  
and | and 运算符用于将多个媒体特性组合到一个单独的媒体查询中，要求每个链接的特性返回 true，则此时查询为真  
not | not 运算符用于否定媒体查询，如果查询不返回 false，则返回 true。如果出现在逗号分隔的列表中，它只会否定应用它的特定查询。如果使用 not 运算符，则必须指定显式媒体类型。例如：not screen and (min-width: 400) and (max-width: 700)注：not 关键字不能用于否定单个功能表达式，它会作用于整个媒体查询  
only | only 运算符仅用于整个查询匹配应用样式，手表应用处理以 only 开头的关键词时将会忽略 only。如果使用 only 运算符，必须指定媒体类型。例如：only screen and (min-width: 400) and (max-width: 700)  
,(逗号) | 逗号分隔效果等同于 or 逻辑操作符。当使用逗号分隔的媒体查询时，如果任何一个媒体查询返回真，样式就是有效的。例如：(width >= 192), (height >= 490)  
or | or 运算符用于将多个媒体特性比较语句组合到一个媒体查询语句中，只要有其中一条媒体特性比较语句返回 true，查询成立。例如：(min-width: 400) or (max-width: 700)  
<= | 小于等于。例如： (400 <= width)  
>= | 大于等于。例如： (500 >= height)  
< | 小于。例如： (400 < width)  
> | 大于。例如： (500 > height)  
  
## # 示例代码

  * 查询形状为圆形或胶囊形

``` .box { width: 100px; height: 100px; background-color: black; } @media (shape: circle) or (shape: pill-shaped) { .box { background-color: green; } } ```

  * 同时查询设备类型为手表，屏幕形状为圆形

``` .box { width: 100px; height: 100px; background-color: black; } @media (device-type: watch) and (shape: circle) { .box { background-color: green; } } ```

## # 支持明细

设备产品 | 说明  
---|---  
小米 S1 Pro 运动健康手表 | 不支持  
小米手环 8 Pro | 不支持  
Xiaomi Watch S3 | 支持2+特性  
Redmi Watch 4 | 不支持  
小米腕部心电血压记录仪 | 不支持  
Xiaomi Watch S4 | 支持  
REDMI Watch 5 | 支持
