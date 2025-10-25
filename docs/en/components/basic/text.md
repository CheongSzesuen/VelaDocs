<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/basic/text.html -->

# text

## Overview

The text content is written in the label content area, supporting escape characters `"\"`.

## Child Components

Only `<span>` is supported.

## Attributes

[General attributes](</vela/quickapp/en/components/general/properties.html>) are supported.

## Styles

[General styles](</vela/quickapp/en/components/general/style.html>) are supported.

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
lines | `<number>` | -1 | No | Number of text lines, -1 means unlimited lines.  
color | `<color>` | rgba(0, 0, 0, 0.54) | No | Text color.  
font-size | `<length>` | 30px | No | Text size.  
font-style | normal | italic | normal | No |   
font-weight | normal | bold | `<number>` | normal | No | The current platform only supports two effects: `normal` and `bold`. When the value is a number, if it is below `550`, it is the former; otherwise, it is the latter.  
text-decoration | underline | line-through | none | none | No |   
text-align | left | center | right | left | No |   
text-indent | `<length>` | `<percentage>` |:---:| No | Specifies the indentation of the first line of the text block.  
line-height | `<length>` |:---:| No | Text line height.  
text-overflow | clip | ellipsis | clip | No | Takes effect when the number of lines is set.  
  
**Examples**

  * Single-line ellipsis
```css
text { width : 150px ; lines : 1 ; text-overflow : ellipsis ; }
```

![](../../images/text-overflow.png)

  * Multi-line ellipsis, taking two lines as an example
```css
text { width : 100px ; lines : 2 ; text-overflow : ellipsis ; }
```

![](../../images/text-overflow-2.png)

## Events

[General events](</vela/quickapp/en/components/general/events.html>) are supported.

## Sample Code
```html
< template > < div > < text > This is a piece of text. </ text > </ div > </ template >
```

![](../../images/text-example.png)
