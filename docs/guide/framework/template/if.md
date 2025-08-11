<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/template/if.html -->

# # 条件指令

## # if指令

if 条件指令，是指 if/elif/else 这 3 个相关指令，用于控制是否增加或者删除组件；

**if/elif/else 节点必须是相邻的兄弟节点** 。

``` <template> <div> <text if="{{display}}">Hello-1</text> <text elif="{{display}}">Hello-2</text> <text else>Hello-3</text> </div> </template> <script> export default { // 页面级组件的数据模型，影响传入数据的覆盖机制：private内定义的属性不允许被覆盖 private: { display: false } } </script> ```

## # show指令

show 指令，是指是否显示组件，用于控制组件的显示状态，并不会从 DOM 结构中删除；

show等同于 visible=none，主要用于在原生组件上声明；

``` <template> <text show="{{visible}}">Hello</text> </template> <script> export default { // 页面级组件的数据模型，影响传入数据的覆盖机制：private内定义的属性不允许被覆盖 private: { visible: false } } </script> ```

## # if与show区别

  * 当 if/elif 指令的值为 false 时，节点会从页面中移除，当 if/elif 指令值为 true，组件动态插入 DOM 结构中；

  * 当 show 指令的值为 true 时，节点可见，当其值为 false 时，组件不可见，但节点仍会保留在页面 DOM 结构中。

