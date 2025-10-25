<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/general/methods.html -->

# Common Methods

Common methods are methods that can be called by all components. After a component marks the id attribute with an id, the developer can obtain the dom node via `this.$element('idName')` and then call the common methods.

The dom object obtained through `this.$element` provides two APIs for calling:

### getBoundingClientRect(Object object)2+

Returns the size of the element and its position relative to the viewport. It must be called after the `onShow` lifecycle of the page.

#### Parameters

Object object

Property | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
success | function |  | No | Callback function for successful API calls  
fail | function |  | No | Callback function for failed API calls  
complete | function |  | No | Callback function for completed API calls (executed for both success and failure)  
  
#### Description of object.success callback function parameters

Object rect

Property | Type | Description  
---|:---:|---  
left | number | Left boundary coordinate of the element  
right | number | Right boundary coordinate of the element  
top | number | Top boundary coordinate of the element  
bottom | number | Bottom boundary coordinate of the element  
width | number | Width of the element  
height | number | Height of the element  
  
#### Code Example
```html
< template > < div > < div id = " box1 " class = " box-normal " > </ div > < div id = " box2 " class = " box-normal " > </ div > </ div > </ template > < script > export default { onShow () { this . $element ('box1') . getBoundingClientRect ({ success : function (data) { const { top , bottom , left , right , width , height } = data ; console.log (data) ; } , fail : (errorData , errorCode) => { console.log (` Error reason: ${ JSON.stringify (errorData) } , Error code: ${ errorCode } `) } , complete : function () { console.info ('complete') } }) } } </ script >
```

### focus(Object object)

A method to make a component gain or lose focus.

#### Parameters

Property | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
focus | boolean | true | No | Makes the component gain or lose focus. Focusing can trigger the `focus` pseudo-class effect (the `focus` pseudo-class style is not yet supported)  
  
#### Code Example
```html
< script > // Focus effect this . $element ('box1') . focus () ; // Focus effect this . $element ('box2') . focus ({ focus : true }) ; // Blur effect this . $element ('box3') . focus ({ focus : false }) ; </ script >
```
