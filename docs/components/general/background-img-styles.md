<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/general/background-img-styles.html -->

# 背景图样式

当需要往页面组件内添加一个图片作为组件背景的时候，开发者可以对这个图片背景的大小、重复放置的模式、放置位置进行调整。

## background-size 属性

该属性定义了背景图片的大小。

参数的个数可以是一个或两个。

有效参数列表如下：

参数 | 描述  
---|---  
`contain` | 等比例缩放背景图片以完全装入容器，可能容器部分显示空白（仅作为单一参数）  
`cover` | 等比例缩放背景图片以完全覆盖容器，可能背景图片部分不可见（仅作为单一参数）  
`auto` | 表示保持原图的尺寸不变。注意，此时原图的尺寸单位为物理分辨率，与手机屏幕分辨率单位一致，非JS 应用内的`1px`长  
`<length>` | 描述图片的具体尺寸，单位：px或dp，不支持浮点计算设置浮点值会被向下取整  
`<percent>` | 描述图片的尺寸占容器对应方向尺寸的百分比，不支持浮点计算设置浮点值会被向下取整  
  
当参数为两个的时候，第一个参数默认解析为水平轴的宽，第二个参数默认解析为竖直轴的高，如果只有一个参数，则将`auto`补充为第二个参数，然后按照双参数的规则解析。

无效参数统一解析为默认值`auto`，即原图尺寸。

**示例**
```html
< template > < div class = " page " > < text > 图片大小 128 * 128 </ text > < text > 背景容器 300 * 200 </ text > < image src = " ../../common/logo.png " > < div class = " imgBg " > </ div > </ div > </ template > < style > .page { flex-direction : column ; align-items : center ; background-color : #000 ; } text { color : #fff ; font-size : 24px ; } .imgBg { width : 300px ; height : 200px ; margin-top : 20px ; border : 2px solid yellowgreen ; background-color : yellowgreen ; background-image : url ('../../common/logo.png') ; background-size : 300px 200px ; background-repeat : no-repeat ; // 暂未支持，以防支持之后样式显示异常建议加上 } </ style >
```

**效果**

![](../../images/background-size.83a0d7ab.jpeg)

## background-repeat 属性（暂未实现）

该属性定义了背景图片在组件中的重复方式，背景图片可以沿着水平轴、竖直轴、两个轴重复，或者不重复。

参数的个数为一个。

有效参数列表如下：

参数 | 描述  
---|---  
`repeat` | 在水平轴和竖直轴上同时重复绘制图片  
`repeat-x` | 只在水平轴上重复绘制  
`repeat-y` | 只在竖直轴上重复绘制  
`no-repeat` | 不会重复绘制图片  
  
无效参数会被解析为默认值，即`repeat`。

**示例**
```html
< div class = " container " > < div class = " img " > </ div > </ div > < style > .container { width : 365px ; height : 365px ; background-color : #c7c7c7 ; } .img { width : 100% ; height : 100% ; background-image : url ('../common/logo.png') ; /* 等比例缩放背景图片到宽度为组件宽的一半 */ background-size : 50% ; /* 在水平方向和竖直方向上重复绘制 */ background-repeat : repeat ; /* 背景图片处于组件中央 */ background-position : center ; } </ style >
```

```css
.img { width : 100% ; height : 100% ; background-image : url ('../common/logo.png') ; /* 等比例缩放背景图片到宽度为100px */ background-size : 100px ; /* 背景图片不重复绘制 */ background-repeat : no-repeat ; /* 背景图片距离组件左边缘20px，和上下边缘的距离比为3:7 */ background-position : left 20px top 30% ; }
```

## background-position 属性

该属性定义了背景图片在组件中的位置。

它可以使用1-4个值进行定义。如果使用两个非关键字值，第一个值表示水平位置，第二个值表示垂直位置。如果仅指定一个值，则第二个值默认是 center。如果使用三个或四个值，则长度百分比值是前面关键字值的偏移量。

**一个值的语法：**

值可能是：

  * 关键字 `center`，用来居中背景图片。
  * 关键字 `top`、`left`、`bottom`、`right` 中的一个。用来指定把背景图放在哪一个边界。另一个维度被设置成50%，所以背景图在此维度居中显示。
  * `<length>` 或 `<percentage>`。指定相对于左边界的 x 坐标，y 坐标被设置成 50%，背景图在y轴居中。

**两个值的语法：**

一个定义 x 坐标，另一个定义 y 坐标。每个值可以是：

  * 关键字 `top`、`left`、`bottom`、`right` 中的一个。如果这里给出 `left` 或 `right`，那么这个值定义 x 轴位置，另一个值定义 y 轴位置。如果这里给出 `top` 或 `bottom`，那么这个值定义 y 轴位置，另一个值定义 x 轴位置。
  * `<length>` 或 `<percentage>`。如果另一个值是 `left` 或 `right`，则该值定义相对于顶部边界的 Y。如果另一个值是 `top` 或 `bottom`，则该值定义相对于左边界的 X。如果两个值都是 `<length>` 或 `<percentage>` 值，则第一个定义 X，第二个定义 Y。

_**注意：**_ 如果一个值是 `top` 或 `bottom`，那么另一个值不可能是 `top` 或 `bottom`。如果一个值是 `left` 或 `right`，那么另一个值不可能是 `left` 或 `right`。也就是说，例如，`top top` 和 `left right` 是无效的。

_**排序：**_ 配对关键字时，位置并不重要，写成 `top left` 或 `left top` 其产生的效果是相同的。 使用 `<length>` 或 `<percentage>` 与关键字配对时顺序非常重要，定义 X 的值放在前面，然后是定义 Y 的值， `right 20px` 和 `20px right` 的效果是不相同的，前者有效但后者无效。`left 20%` 或 `20% bottom` 是有效的，因为 X 和 Y 值已明确定义且位置正确。

_**默认值**_ 是 `left top` 或者 `0% 0%`。

**三个值的语法：**

两个值是关键字值，第三个是前面值的偏移量：

  * 第一个值是关键字 `top`、`left`、`bottom`、`right`，或者 `center`。如果设置为 `left` 或 `right`，则定义了 X。如果设置为 `top` 或 `bottom`，则定义了 Y，另一个关键字值定义了 X。
  * `<length>` 或 `<percentage>`，如果是第二个值，则是第一个值的偏移量。如果是第三个值，则是第二个值的偏移量。
  * 单个长度或百分比值是其前面的关键字值的偏移量。一个关键字与两个 `<length>` 或 `<percentage>` 值的组合无效。

**四个值的语法：**

第一个和第三个值是定义 X 和 Y 的关键字值。第二个和第四个值是前面 X 和 Y 关键字值的偏移量：

  * 第一个值和第三个值是关键字值 `top`、`left`、`bottom`、 `right` 之一。如果设置为 `left` 或 `right`，则定义了 X。如果设置为 `top` 或 `bottom`，则定义了 Y，另一个关键字值定义了 X。
  * 第二个和第四个值是 `<length>` 或 `<percentage>`。第二个值是第一个关键字的偏移量。第四个值是第二个关键字的偏移量。

无效参数全部解析为默认值（0px, 0px），即图片显示在组件的左上角。

**示例**
```html
< template > < div class = " page " > < text > 图片大小 128 * 128 </ text > < text > 背景容器 300 * 200 </ text > < image src = " ../../common/logo.png " > < div class = " imgBg " > </ div > </ div > </ template > < style > .page { flex-direction : column ; align-items : center ; background-color : #000 ; } text { color : #fff ; font-size : 24px ; } .imgBg { width : 300px ; height : 200px ; margin-top : 20px ; border : 2px solid yellowgreen ; background-color : yellowgreen ; background-image : url ('../../common/logo.png') ; background-size : cover ; background-position : right bottom ; background-repeat : no-repeat ; // 暂未支持，以防支持之后样式显示异常建议加上 } </ style >
```

**效果**

![](../../images/background-position.195a1e2b.jpeg)

## 支持明细

设备产品 | 说明  
---|---  
小米 S1 Pro 运动健康手表 | 不支持  
小米手环 8 Pro | 不支持  
Xiaomi Watch S3 | 不支持  
Redmi Watch 4 | 不支持  
小米腕部心电血压记录仪 | 不支持  
Xiaomi Watch S4 | 支持  
REDMI Watch 5 | 支持
