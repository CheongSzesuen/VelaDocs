<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/basic/span.html -->

# span

## Overview

Formatted text, which can only be used as a subcomponent of [`<text>`](</vela/quickapp/en/components/basic/text.html>), [`<a>`](</vela/quickapp/en/components/basic/a.html>), and `<span>`.

## Subcomponents

Only `<span>` is supported.

## Attributes

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
id | `<string>` |:---:| No | Unique identifier  
style | `<string>` |:---:| No | Style declaration  
class | `<string>` |:---:| No | Reference stylesheet  
for | `<array>` |:---:| No | Loop through the current tag based on the data list  
if | `<boolean>` |:---:| No | Add or remove the current tag based on the data boolean value  
  
## Styles

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
color | `<color>` | rgba(0, 0, 0, 0.54) | No | Text color  
font-size | `<length>` | 30px | No | Text size  
font-style | normal | italic | normal | No | -  
font-weight | normal | bold | `<number>` | normal | No | The current platform only supports `normal` and `bold` effects. When the value is a number, values below `550` are considered as the former, otherwise as the latter.  
text-decoration | underline | line-through | none | none | No | -  
  
## Events

Not supported.

## Example Code
```html
< template > < div > < text > < span > I am span, </ span > < span style = " color : #f76160 " > I am span, </ span > < span style = " color : #f76160 ; text-decoration : underline ; " > I am span, </ span > </ text > </ div > </ template >
```

![](../../images/span.png)
