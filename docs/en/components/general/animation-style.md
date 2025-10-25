<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/general/animation-style.html -->

# Animation Styles

The Vela JS application supports developers in creating animations by providing animation style properties for the `transform`, `transform-origin`, `animation`, and `transition` classes, with parameter formats aligned with CSS for easier developer adaptation.

For `transform`, refer to this [documentation (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform>).

For `transform-origin`, refer to this [documentation (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform-origin>).

For `animation`, refer to this [documentation (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation>).

For `transition`, refer to this [documentation (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition>).

## Animation Style List

Name | Type | Default Value | Description  
---|:---:|---|---  
transform | `<string>` |:---:| See transform operations below  
transform-origin | `<string>` |:---:| See transform-origin operations below  
animation-name | `<string>` |:---:| Corresponds to the name of @keyframes, see @keyframes properties below  
animation-delay | `<time>` | 0 | Currently supported units: [s(seconds) | ms(milliseconds)]  
animation-duration | `<time>` | 0 | Currently supported units: [s(seconds) | ms(milliseconds)]  
animation-iteration-count | `<integer>` | `infinite` | 1 | Defines the number of animation plays, can be set to `infinite` for unlimited plays  
animation-timing-function | linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier(`<number>`, `<number>`, `<number>`, `<number>`) | step-start | step-end | steps(number_of_steps[, step-direction]?) | ease | -  
transition-property | `<string>` | all | Specifies the generic style property name for executing the transition effect, see details  
transition-duration | `<time>` | 0s | Specifies the execution time of the transition  
transition-timing-function | linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier(`<number>`, `<number>`, `<number>`, `<number>`) | step-start | step-end | steps(number_of_steps[, step-direction]?) | ease | Specifies the timing function for transition execution. The parameter interpretation is the same as for animation  
transition-delay | `<time>` | 0s | Specifies the time when the transition starts executing, i.e., how long after changing the element's property value the transition effect begins  
  
**Note** :

  * animation-timing-function types:

cubic-bezier(`<number>`, `<number>`, `<number>`, `<number>`) | step-start | step-end | steps(number_of_steps[, step-direction]?) where:

steps(number_of_steps, step-direction)

Name | Type | Default Value  | Required  | Description  
---|:---:|---|:---:|---  
number_of_steps | `<integer>` |:---:| Yes | Positive integer representing equal interval steps  
step-direction | jump-start | jump-end | jump-none | jump-both | start | end | end | No | Keyword indicating left-continuous or right-continuous function  
  
  * cubic-bezier(x1, y1, x2, y2):

Parameters x1, y1, x2, y2 are `<number>` type values representing the horizontal and vertical coordinates of points P1 and P2 in the currently defined cubic Bezier curve. x1 and x2 must be within the [0, 1] range; otherwise, the current value is invalid.

## Transform Operations

Apply 2D transformations to elements. This property allows us to rotate, scale, and move elements.

Supported style property list:

Name | Type  
---|---  
translate | `<length>` | `<percent>`  
translateX | `<length>` | `<percent>`  
translateY | `<length>` | `<percent>`  
scale | `<number>`  
scaleX | `<number>`  
scaleY | `<number>`  
rotate | `<deg>`  
  
## Transform-Origin Operations

Change the origin point of an element's deformation, currently supporting changes to the element's X and Y axes.

**Note** :

  * This property must be used with the transform property first.

Example code:
```css
/* Using % values */ div { transform : rotate (30deg) ; transform-origin : 20% 40% ; } /* Using px values */ div { transform : rotate (30deg) ; transform-origin : 100px 100px ; }
```

## Animation-Name Property

Specifies a series of animations to be adopted. Each property value name represents a keyframe sequence defined by the @keyframes property. This property supports applying single or multiple animations (`1070+`) in components. When applying multiple animations, they start simultaneously.

Example code:
```js
/* Single animation */ animation \- name : Color ; animation \- name : translate ; animation \- name : rotate ; /* Multiple animations 1070+ */ animation \- name : Color , Opacity ; animation \- name : Width , translate , rotate ;
```

## @keyframes Property

Name | Type | Default Value | Description  
---|:---:|---|---  
background-color | `<color>` |:---:| -  
background-position | `<length>` |`<percentage>`| left | right | top | bottom | center | 0px 0px | Describes the position where the background image is drawn in the container, supports 1-4 parameters, see [Background Image Styles](</vela/quickapp/en/components/general/background-img-styles.html>) for details  
opacity | `<number>` |:---:| -  
width/height | `<length>` |:---:| Percentage not currently supported  
transform | `<string>` |:---:| Allows rotating, scaling, and moving elements  
  
**Note** :

Currently does not support omitting the starting value (0%) or ending value (100%); both must be explicitly specified.

## Transition Animation

Transition animation is another way to implement animations. Transition animations can define transition effects for elements when switching between different states, such as state changes implemented through JavaScript.

### Transition Usage Example

There are four style properties: transition-property, transition-duration, transition-timing-function, and transition-delay, written directly in the style. Example usage:
```html
< template > < div class = " page " > < div class = " div {{otherClass}} " > </ div > </ div > </ template > < script > export default { data : { otherClass : "" } , onShow () { const that = this setTimeout (() => { that.otherClass = "new-width" } , 1000) ; } } ; </ script > < style > .page { padding : 60px ; align-items : center ; } .div { width : 100px ; height : 200px ; background-color : red ; transition-property : width ; transition-duration : 2000ms ; transition-timing-function : ease-in ; transition-delay : 500ms ; } .new-width { width : 300px ; } </ style >
```

The four style properties above can be abbreviated into one, indicating that after triggering a width change in the div, it will change to the new width value in an accelerated manner over 0.5s, with the transition animation lasting 2s:
```css
.div { transition : width 2000ms ease-in 500ms ; }
```

### Generic Style Properties Supported by transition-property

The list of generic style properties supported by transition-property in JS applications:

Style Name | Remarks  
---|---  
width | √  
height | √  
opacity | √  
visibility | √  
color | Not currently supported  
transform-origin | Not currently supported  
transform | Not currently supported  
padding | Not currently supported  
padding-[left|top|right|bottom] | Not currently supported  
margin | Not currently supported  
margin-[left|top|right|bottom] | Not currently supported  
border | Not currently supported  
border-[left|top|right|bottom] | Not currently supported  
border-width | √  
border-[left|top|right|bottom]-width | Not currently supported  
border-color | √  
border-[left|top|right|bottom]-color | Not currently supported  
border-radius | Not currently supported  
border-[top|bottom]-[left|right]-radius | Not currently supported  
background | Not currently supported  
background-color | √  
background-size | Not currently supported  
background-position | √  
flex | Not currently supported  
flex-grow | Not currently supported  
flex-shrink | Not currently supported  
flex-basis | Not currently supported  
[left|top|right|bottom] | Not currently supported
