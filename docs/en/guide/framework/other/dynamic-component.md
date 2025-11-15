<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/other/dynamic-component.html -->

# Dynamic Component

TIP

In this section, you will learn how to use dynamic components to reduce the amount of template code and improve code readability.

When multiple components are introduced on a page and need to be dynamically switched, it is highly recommended to use directives such as `if` on the template for logical judgment and change the view structure in most cases.

**Example** :
```html
< import src = " ./part1.ux " name = " part1 " > </ import > < import src = " ./part2.ux " name = " part2 " > </ import > < import src = " ./part3.ux " name = " part3 " > </ import > < template > < div > < part1 if = " {{status === 1}} " > </ part1 > < part2 elif = " {{status === 2}} " > </ part2 > < part3 else > </ part3 > </ div > </ template > < script > export default { data () { return { status : 1 } } } </ script >
```

However, when there are many components, the amount of template code will become large, which is not conducive to maintenance. At this time, you can use **dynamic components** to reduce the amount of template code. This can be achieved by adding a special `is` attribute to the `<component>` element. The value of `is` represents the component name, and you can switch components by simply modifying the `is` attribute.

**Example** :
```html
< import src = " ./part1.ux " name = " part1 " > </ import > < import src = " ./part2.ux " name = " part2 " > </ import > < import src = " ./part3.ux " name = " part3 " > </ import > < import src = " ./part4.ux " name = " part4 " > </ import > < import src = " ./part5.ux " name = " part5 " > </ import > < import src = " ./part6.ux " name = " part6 " > </ import > < template > < div > < component is = " {{'part' + status}} " > </ component > </ div > </ template > < script > export default { data () { return { status : 1 } } } </ script >
```
