<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/style/media-query.html -->

# Media Queries 2+

With media queries, developers can adjust the styles of a JS application based on the values or presence of various device features and parameters.

Media queries are part of responsive design. Similar to CSS, you can use the @media at-rule to conditionally apply part of a stylesheet based on the results of a media query; you can also use @import to conditionally apply an entire stylesheet.

Minimum version of aiot-toolkit: 1.1.3

## Syntax

Each media query statement consists of an optional media type and any number of media feature expressions. Multiple media query statements can be combined using various logical operators. Media query statements are case-insensitive.

There are two ways to perform media queries:

### Introducing media queries using the @media approach

```css
@media [media type] [and|not|only] [(media feature)] {
  CSS-Code;
}
```

### Examples

  * @media (max-width: 30) { ... } // Level 3 syntax.
  * @media (width <= 30) { ... } // Level 4 syntax, clearer and more concise than level 3.
  * @media screen and (min-width: 400) and (max-width: 700) { ... } // Multi-condition syntax.
  * @media (400 <= width <= 700) { ... } // Multi-condition level 4 syntax.

### Introducing media queries using the @import approach 3+

```css
@import './css_file_name.css' [media type] [and|not|only] [(media feature) ];
```

## Media Types

Media types describe the general category of the device. Except when using the not or only logical operators, where the media type must be specified, the media type is optional. The following media types are currently supported in JS applications:

Media Type | Description  
---|---  
screen | Primarily used for screens.  
  
## Media Features

Media feature expressions are entirely optional and are responsible for testing whether these features or characteristics are present and what their values are.

Each media feature expression must be enclosed in parentheses.

The following media features are currently supported in JS applications:

Type | Description | Units Required for Query | Supported Units  
---|:---:|---|---  
height[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Defines the height of the visible area of the page on the output device | No | dp  
min-height[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Defines the minimum height of the visible area of the page on the output device | No | dp  
max-height[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Defines the maximum height of the visible area of the page on the output device | No | dp  
width[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Defines the width of the visible area of the page on the output device | No | dp  
min-width[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Defines the minimum width of the visible area of the page on the output device | No | dp  
max-width[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Defines the maximum width of the visible area of the page on the output device | No | dp  
aspect-ratio[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Defines the aspect ratio of the visible area of the page on the output device. The ratio value should be in the format x/y, e.g., 1/2 | No | None  
min-aspect-ratio[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Defines the minimum aspect ratio of the visible area of the page on the output device. Parameter requirements are the same as above. | No | None  
max-aspect-ratio[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Defines the maximum aspect ratio of the visible area of the page on the output device. Parameter requirements are the same as above. | No | None  
device-type[3+](</vela/quickapp/zh/guide/version/APILevel3>) | Optional values for device-type are: watch, band, smartspeaker. Default value: watch | No | None  
shape[2+](</vela/quickapp/zh/guide/version/APILevel2>) | Screen shape. Optional values: circle, rect, pill-shaped[3+](</vela/quickapp/zh/guide/version/APILevel3>) | No | None  
  
### Notes

  1. In the media feature list, media features marked as "without units in query," such as width and height, should not include length units in the query, and the length unit can only be dp.

dp value = physical resolution / device pixel ratio (DPR)

Example: A device with a resolution of 480*480 and a DPR of 2 has a screen width of 480 pixels = 240dp.

Reference data for various devices:

Device Type | Device Model | Screen Shape | Screen Size | Resolution | PPI | DPR | Horizontal DP Value  
---|:---:|---|:---:|---|:---:|---|---  
Watch | Xiaomi Watch S1 Pro | Circle | 1.47 inches | 480x480 | 326 | 2.0 | 240  
Watch | Xiaomi Watch H1 | Circle | 1.43 inches | 466x466 | 326 | 2.0 | 233  
Watch | Xiaomi Watch S3 | Circle | 1.43 inches | 466x466 | 326 | 2.0 | 233  
Watch | Xiaomi Watch S4 sport | Circle | 1.43 inches | 466x466 | 326 | 2.0 | 233  
Watch | Xiaomi Watch S4 | Circle | 1.43 inches | 466x466 | 326 | 2.0 | 233  
Watch | REDMI Watch 5 | Rectangle | 2.07 inches | 432x514 | 324 | 2.0 | 216  
Band | Xiaomi Band 8 Pro | Rectangle | 1.74 inches | 336x480 | 336 | 2.1 | 168  
Band | Xiaomi Band 9 | Pill-shaped | 1.62 inches | 192x490 | 325 | 2.0 | 96  
Band | Xiaomi Band 9 Pro | Rectangle | 1.74 inches | 336x480 | 336 | 2.1 | 168  
Band | Xiaomi Band 10 | Pill-shaped | 1.725 inches | 212x520 | 326 | 2.0 | 106  
  
Example code:

```css
// The following media query will take effect on devices with a screen width between 80dp and 160dp.
@media (min-width: 80) and (max-width: 160) {
  .box {
    background-color: green;
  }
}

// The following media query will take effect on devices with a screen width between 160dp and 200dp.
@media (min-width: 160) and (max-width: 200) {
  .box {
    background-color: yellow;
  }
}

// The following media query will take effect on devices with a screen width between 200dp and 300dp.
@media (min-width: 200) and (max-width: 300) {
  .box {
    background-color: red;
  }
}
```

## Logical Operators 3+

Developers can use logical operators to combine multiple media feature queries and write complex media queries.

Type | Description  
---|---  
and | The and operator combines multiple media features into a single media query. The query is true only if all linked features return true.  
not | The not operator negates the media query. If the query does not return false, it returns true. If used in a comma-separated list, it only negates the specific query it applies to. If the not operator is used, an explicit media type must be specified. Example: not screen and (min-width: 400) and (max-width: 700). Note: The not keyword cannot be used to negate a single feature expression; it applies to the entire media query.  
only | The only operator is used to apply styles only when the entire query matches. Watch applications will ignore the only keyword when processing keywords starting with only. If the only operator is used, a media type must be specified. Example: only screen and (min-width: 400) and (max-width: 700).  
, (comma) | The comma has the same effect as the or logical operator. When using comma-separated media queries, if any of the media queries return true, the styles are valid. Example: (width >= 192), (height >= 490).  
or | The or operator combines multiple media feature comparison statements into a single media query. The query is true if any of the media feature comparison statements return true. Example: (min-width: 400) or (max-width: 700).  
<= | Less than or equal to. Example: (400 <= width).  
>= | Greater than or equal to. Example: (500 >= height).  
< | Less than. Example: (400 < width).  
> | Greater than. Example: (500 > height).  
  
## Example Code

  * Query for devices with a circular or pill-shaped screen:

```css
  .box {
    width: 100px;
    height: 100px;
    background-color: black;
  }

  @media (shape: circle) or (shape: pill-shaped) {
    .box {
      background-color: green;
    }
  }
```
  * Query for devices that are watches and have a circular screen:

```css
  .box {
    width: 100px;
    height: 100px;
    background-color: black;
  }

  @media (device-type: watch) and (shape: circle) {
    .box {
      background-color: green;
    }
  }
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Not supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Band 9 / 9 Pro | Supports 2+ features  
Xiaomi Watch S3 | Supports 2+ features  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG Blood Pressure Monitor | Not supported  
Xiaomi Band 10 | Supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported  
REDMI Watch 6 | Supported
