<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/template/event.html -->

# # 事件绑定

## # 格式

``` <text onclick="press"></text> ```

可以简写为：

``` <text @click="press"></text> ```

**fn** ：`fn`为事件回调函数名（在`<script>`中有对应的函数实现），上例中`press`为事件回调函数。

## # 传参

### # 常量

``` <template> <div class="page"> <text for="{{list}}" onclick="handle($idx,$item)">{{$item}}</text> </div> </template> <script> export default { private: { list:[1,2,3,4,5] }, handle(idx,item,$evt) { // 点击第一个元素 console.log(idx) // 0 console.log(item) // 1 console.log($evt) // { pageX: 4, pageY: 246, clientX: 4, clientY: 246, offsetX: 4, offsetY: 246 } } } </script> ```

### # 变量

`<script>`中定义的页面的数据变量（前面不用写`this`）。

``` <template> <div class="page"> <text for="{{list}}" onclick="handle(total,$item)"> {{$item}}</text> </div> </template> <script> export default { private: { list:[1,2,3,4,5], total:0 }, handle(total,num,$evt){ console.log(total) console.log(num) console.log($evt) } } </script> ```

注意

回调函数被调用时，会在参数列表末尾自动添加一个`evt`参数，通过`evt`参数访问回调事件相关上下文数据。

← [ Props ](</vela/quickapp/zh/guide/framework/template/Props.html>) [ 循环指令 ](</vela/quickapp/zh/guide/framework/template/for.html>) → 

快速导航

格式

传参

常量

变量
