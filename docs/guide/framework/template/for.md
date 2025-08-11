<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/template/for.html -->

# 循环指令

## 列表渲染

如果要实现列表渲染，我们会用到 for 指令。for 指令用于循环输出一个数组类型的数据。

提示

`for指令`根据源数据数组渲染列表，支持的写法如下（其中`{{}}`可以省略）：

  * `for="{{list}}"` `list`为源数据数组，默认的数组元素名为`$item`；
  * `for="{{value in list}}"` `value`为自定义的数组元素名，默认的数组元素索引名为`$idx`；
  * `for="{{(index, value) in list}}"` `index`为自定义的数组元素索引名，`value`为自定义的数组元素名。

提示

`for指令`的`tid属性`用于指定数组元素的唯一 Id，若未指定，默认使用数组索引(`$idx`)作为唯一 Id。`tid属性`的作用在于元素节点重用，优化 for 循环的重绘效率

**示例如下：**
```html
< template > < div class = " page " > <!-- 方式1：默认$item代表数组中的元素, $idx代表数组中的索引 --> < div class = " row " for = " {{list}} " tid = " uniqueId " > < text > {{$idx}}.{{$item.name}} </ text > </ div > <!-- 方式2：自定义元素变量名称 --> < div class = " row " for = " value in list " tid = " uniqueId " > < text > {{$idx}}.{{value.name}} </ text > </ div > <!-- 方式3：自定义元素、索引的变量名称 --> < div class = " row " for = " (personIndex, personItem) in list " tid = " uniqueId " > < text > {{personIndex}}.{{personItem.name}} </ text > </ div > </ div > </ template > < style > .page { flex-direction : column ; } .row { width : 85% ; margin-top : 10px ; margin-bottom : 10px ; } </ style > < script > export default { private : { list : [ { name : 'aa' , uniqueId : 1 } , { name : 'bb' , uniqueId : 2 } , { name : 'cc' , uniqueId : 3 } ] } , onInit () { console.info ('指令for') } } </ script >
```

示例代码中，在渲染页面时，`div.row`的结构，会根据 script 中的数据 list 的定义，被循环的生成多个。

`tid="uniqueId"`，数组元素的某个属性名，不一定叫`uniqueId`。它类似于React的`key={item.uniqueId}`或vue的`:key="item.uniqueId"`，用于优化渲染速度。

当数据修改时，数据不改变的dom不会被重新渲染，已经改变的数据所在的dom才会被重新渲染，因此我们必须保证`uniqueId`这个属性值在每个数组元素都不一样。

注意

  1. for 指令只能循环数组，不能循环对象。

  2. for 指令在 block 标签的行为与它在其他标签的行为不一样，block 标签在渲染时不会额外插入DOM节点，而是会循环其内部的DOM结构，其他标签则会循环生成其自身。

  3. 当 for 指令与 if 指令共存于一个标签时， if 指令的优先级优于 for 指令。为了方便未看文档的新人快速上手项目，不建议这两个指令共存于同一个标签。

  4. 自定义变量表示 for 指令的数组索引和数组元素时，变量名不可以用`$`或`_`开头。

  5. 使用`tid属性`时应注意：

     * `tid属性`指定的数据属性必须存在，否则可能导致运行异常；
     * `tid属性`指定的数据属性要保证唯一，否则可能导致性能问题；
     * `tid属性`目前不支持表达式。

