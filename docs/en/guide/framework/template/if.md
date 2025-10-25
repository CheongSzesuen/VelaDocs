<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/template/if.html -->

# Conditional Directives

## if Directive

The if conditional directive refers to the three related directives: if/elif/else, which are used to control whether components are added or removed.

**The if/elif/else nodes must be adjacent sibling nodes.**
```html
< template > < div > < text if = " {{display}} " > Hello-1 </ text > < text elif = " {{display}} " > Hello-2 </ text > < text else > Hello-3 </ text > </ div > </ template > < script > export default { // The data model for page-level components, affecting the override mechanism of incoming data: properties defined in private are not allowed to be overridden private : { display : false } } </ script >
```

## show Directive

The show directive refers to whether a component is displayed, controlling the visibility state of the component without removing it from the DOM structure.

show is equivalent to visible=none, mainly used for declaration on native components.
```html
< template > < text show = " {{visible}} " > Hello </ text > </ template > < script > export default { // The data model for page-level components, affecting the override mechanism of incoming data: properties defined in private are not allowed to be overridden private : { visible : false } } </ script >
```

## Differences Between if and show

  * When the value of the if/elif directive is false, the node is removed from the page. When the value is true, the component is dynamically inserted into the DOM structure.

  * When the value of the show directive is true, the node is visible. When the value is false, the component is invisible, but the node remains in the page's DOM structure.

