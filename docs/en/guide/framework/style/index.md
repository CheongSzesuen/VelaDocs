<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/style/ -->

# Style

The style is used to describe the component style of the template and determine how the component should be displayed.

The style layout adopts the CSS Flexbox style, which expands and modifies CSS for some native components.

To solve the screen adaptation problem, all size-related styles (such as width and font-size) are based on the reference width (default 480px) and scaled according to the actual screen width. For example, width:100px is actually 200px on a 960px width screen.

## File Import

Two ways to import external files are supported:
```html
<!-- Import external file to replace internal style --> < style src = " ./style.css " > </ style > <!-- Merge external file --> < style > @import './style.css' ; .a { } </ style >
```

## Internal Template Style

The style and class attributes are supported to control the component style:
```html
<!-- Inline style --> < div style = " color : red ; margin : 10px ; " /> <!-- Class declaration --> < div class = " normal append " />
```

## Selectors

Supported selectors include:

Selector | Example | Description  
---|:---:|---  
.class | .intro | Select all components with class="intro"  
#id | #firstname | Select the component with id="firstname"  
tag | div | Select all div components  
, | .a, .b | Select all components with class="a" and class="b"
```html
< style > /* Single selector */ text { } .class-abc { } #idAbc { } /* Multiple selectors with the same style */ .font-text, .font-comma { } </ style >
```

## Selector Priority

The priority calculation of the current style selector is consistent with the browser, which is a subset of browser CSS rendering (only supports: inline, id, class, tag).

Multiple CSS declarations can match the same element, such as div. The overall priority of CSS declarations applied to this element is: inline > #id > .class > tag. These four categories match multiple CSS declarations of the element, such as: `<div id="sample" style="width: 200px;" class="class-div"></div>`. The priority is compared based on the sum of the weight values of each selector. The priority weight values of selectors are as follows:

  * `ID selector` (e.g., #hello) has a weight value of 10000

  * `Class selector` (e.g., .example) has a weight value of 100

  * `Type selector` (e.g., h1) has a weight value of 1

The CSS priority calculation document can also be viewed in the [MDN documentation (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/Specificity>) for beginners.

## Style Precompilation

Currently, JS applications support precompilation of `less` and `sass`. For specific tutorials, please refer to [here](</vela/quickapp/en/guide/framework/style/page-style-and-layout.html#引入-less-scss-预编译>).
```html
<!-- Import external file to replace internal style --> < style lang = " less " src = " ./lessFile.less " > </ style > <!-- Merge external file --> < style lang = " less " > @import './lessFile.less' ; .less-font-text, .less-font-comma { font-size : 60px ; } </ style >
```
