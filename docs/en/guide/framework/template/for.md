<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/template/for.html -->

# Loop Directives

## List Rendering

To implement list rendering, we use the `for` directive. The `for` directive is used to loop through and output an array of data.

TIP

The `for directive` renders a list based on the source data array. The supported syntax is as follows (where `{{}}` can be omitted):

  * `for="{{list}}"` `list` is the source data array, and the default array element name is `$item`;
  * `for="{{value in list}}"` `value` is a custom array element name, and the default array element index name is `$idx`;
  * `for="{{(index, value) in list}}"` `index` is a custom array element index name, and `value` is a custom array element name.

TIP

The `tid attribute` of the `for directive` is used to specify the unique ID of array elements. If not specified, the array index (`$idx`) is used as the unique ID by default. The purpose of the `tid attribute` is to enable element node reuse and optimize the redraw efficiency of the `for` loop.

**Example** :
```html
< template > < div class = " page " > <!-- Method 1: Default $item represents the array element, $idx represents the array index --> < div class = " row " for = " {{list}} " tid = " uniqueId " > < text > {{$idx}}.{{$item.name}} </ text > </ div > <!-- Method 2: Custom element variable name --> < div class = " row " for = " value in list " tid = " uniqueId " > < text > {{$idx}}.{{value.name}} </ text > </ div > <!-- Method 3: Custom element and index variable names --> < div class = " row " for = " (personIndex, personItem) in list " tid = " uniqueId " > < text > {{personIndex}}.{{personItem.name}} </ text > </ div > </ div > </ template > < style > .page { flex-direction : column ; } .row { width : 85% ; margin-top : 10px ; margin-bottom : 10px ; } </ style > < script > export default { private : { list : [ { name : 'aa' , uniqueId : 1 } , { name : 'bb' , uniqueId : 2 } , { name : 'cc' , uniqueId : 3 } ] } , onInit () { console.info ('Directive for') } } </ script >
```

In the example code, the structure of `div.row` will be generated multiple times based on the definition of the `list` data in the script when rendering the page.

`tid="uniqueId"` refers to a property name of the array element, which does not necessarily have to be called `uniqueId`. It is similar to React's `key={item.uniqueId}` or Vue's `:key="item.uniqueId"`, used to optimize rendering speed.

When data is modified, DOM elements whose data has not changed will not be re-rendered; only DOM elements whose data has changed will be re-rendered. Therefore, we must ensure that the `uniqueId` property value is unique for each array element.

Note

  1. The `for` directive can only loop through arrays, not objects.

  2. The behavior of the `for` directive inside a `block` tag is different from its behavior in other tags. The `block` tag does not insert additional DOM nodes during rendering but instead loops through its internal DOM structure. Other tags will loop and generate themselves.

  3. When the `for` directive and the `if` directive coexist on the same tag, the `if` directive takes precedence over the `for` directive. To help newcomers who haven't read the documentation quickly get started with the project, it is not recommended to have these two directives coexist on the same tag.

  4. When custom variables represent the array index and array element of the `for` directive, the variable names cannot start with `$` or `_`.

  5. When using the `tid attribute`, note the following:

     * The data property specified by the `tid attribute` must exist; otherwise, it may cause runtime exceptions.
     * The data property specified by the `tid attribute` must be unique; otherwise, it may cause performance issues.
     * The `tid attribute` currently does not support expressions.

