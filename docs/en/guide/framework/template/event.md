<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/template/event.html -->

# Event Binding

## Format
```html
< text onclick = " press " > </ text >
```

can be abbreviated as:
```html
< text @click = " press " > </ text >
```

**fn** : `fn` is the name of the event callback function (with corresponding function implementation in `<script>`). In the above example, `press` is the event callback function.

## Passing Parameters

### Constants
```html
< template > < div class = " page " > < text for = " {{list}} " onclick = " handle ($idx , $item) " > {{$item}} </ text > </ div > </ template > < script > export default { private : { list : [ 1 , 2 , 3 , 4 , 5 ] } , handle (idx , item , $evt) { // Clicking the first element console.log (idx) // 0 console.log (item) // 1 console.log ($evt) // { pageX: 4, pageY: 246, clientX: 4, clientY: 246, offsetX: 4, offsetY: 246 } } } </ script >
```

### Variables

Data variables defined in `<script>` for the page (no need to write `this` before them).
```html
< template > < div class = " page " > < text for = " {{list}} " onclick = " handle (total , $item) " > {{$item}} </ text > </ div > </ template > < script > export default { private : { list : [ 1 , 2 , 3 , 4 , 5 ] , total : 0 } , handle (total , num , $evt) { console.log (total) console.log (num) console.log ($evt) } } </ script >
```

WARNING

When the callback function is called, an `evt` parameter will be automatically added at the end of the parameter list. You can access the context data related to the callback event through the `evt` parameter.
