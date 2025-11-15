<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/other/dynamic-component.html -->

# 动态组件

提示

通过本节，你将学会如何使用动态组件，减少模板的代码量，提高代码的可读性。

当页面中引入多个组件并需要动态切换组件时，绝大数情况下推荐在模板上使用 `if` 等指令进行逻辑判断，改变视图结构。

**示例如下：**
```html
< import src = " ./part1.ux " name = " part1 " > </ import > < import src = " ./part2.ux " name = " part2 " > </ import > < import src = " ./part3.ux " name = " part3 " > </ import > < template > < div > < part1 if = " {{status === 1}} " > </ part1 > < part2 elif = " {{status === 2}} " > </ part2 > < part3 else > </ part3 > </ div > </ template > < script > export default { data () { return { status : 1 } } } </ script >
```

但当组件较多时，模板的代码量会变得很大，不利于维护。此时可以使用 **动态组件** 来减少模板的代码量，通过在 `<component>` 元素加一个特殊的 `is` 属性来实现，`is` 的值表示组件名，只需修改 `is` 属性即可切换组件。

**示例如下：**
```html
< import src = " ./part1.ux " name = " part1 " > </ import > < import src = " ./part2.ux " name = " part2 " > </ import > < import src = " ./part3.ux " name = " part3 " > </ import > < import src = " ./part4.ux " name = " part4 " > </ import > < import src = " ./part5.ux " name = " part5 " > </ import > < import src = " ./part6.ux " name = " part6 " > </ import > < template > < div > < component is = " {{'part' + status}} " > </ component > </ div > </ template > < script > export default { data () { return { status : 1 } } } </ script >
```
