<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/basic/a.html -->

# a

## Overview

Hyperlink (no underline by default)

## Child Components

Only [`<span>`](</vela/quickapp/en/components/basic/span.html>) is supported.

## Attributes

Supports [universal attributes](</vela/quickapp/en/components/general/properties.html>)

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
href | `string` |:---:| No | For supported formats, see the uri parameter in [page routing](</vela/quickapp/en/features/basic/router.html>).  
Additional:  
href can also add parameters in the format of "?param1=value1", and the parameters can be used in the page via `this.param1`. When using the `this.param1` variable, you need to define a property with the same key name under `public` (passing parameters outside the app) or `protected` (passing parameters inside the app) in the target page.  
Example:  
`<a href="/about?param1=value1">About</a>`  
  
## Styles

Supports [text styles](</vela/quickapp/en/components/basic/text.html>)

Supports [universal styles](</vela/quickapp/en/components/general/style.html>)

## Events

Supports [universal events](</vela/quickapp/en/components/general/events.html>)

## Example Code
```html
< template > < div > < a class = " link " href = " /home " > goHome </ a > < a href = " /home " > < span class = " link " > Using span child component </ span > </ a > </ div > </ template >
```
