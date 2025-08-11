<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/script/ -->

# # script 脚本

ux 文件中用来定义页面的逻辑代码，包括数据对象、生命周期接口、自定义方法、通用方法等。

## # 语法

支持 ES5 / ES6 语法

### # 模块声明

可以通过 import 引入功能模块，在代码中调用模块方法（具体参看接口部分文档说明）：

``` import fetch from '@system.fetch' ```

### # 代码引用

JS 代码引用推荐使用`import`来导入，例如：

``` import utils from '../common/utils.js' ```

注意

JS 应用环境不是 node 环境，不要引用 node 原生模块，如 `import fs from 'fs'`。

## # 页面数据对象

页面文件中可以定义页面级的数据对象，用于在模板中绑定和在页面方法中操作。例如：

``` <template> <div> <text>{{a}}</text> </div> </template> <script> export default { // 页面的数据对象，影响传入数据的覆盖机制：private内定义的属性不允许被覆盖 private: { a: 1 } } </script> ```

其他详细说明参见[页面数据对象](</vela/quickapp/zh/guide/framework/script/page-data.html>)。

## # 生命周期接口

应用和页面都有预定义的一系列生命周期，可在脚本中声明若干生命周期钩子函数，在执行到该特定生命周期阶段时，会调用这些钩子函数，例如：

``` // 会在应用/页面被初始化的时候执行这个函数 onInit() { console.log('page initialized！') } ```

其他详细说明参见[生命周期](</vela/quickapp/zh/guide/framework/script/lifecycle.html>)。

## # 自定义方法

开发者可以在应用/页面 ux 文件中按需声明自定义方法，包括一些工具方法、事件回调方法等，例如：

``` onBtnClick(){ console.log('button clicked!') } ```

## # 全局对象和方法

开发者在应用ux文件(`app.ux`)中声明的属性和方法，可以在任意页面中通过`this.$app.$def`进行方法，详情参考[全局对象和方法](</vela/quickapp/zh/guide/framework/script/global-data-method.html>)。

## # 通用方法

框架提供了一些预定义的通用方法供页面/组件调用，详情参考[通用方法](</vela/quickapp/zh/components/general/methods.html>)。
