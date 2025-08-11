<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/start/toolkit-params.html -->

# 编译参数

编译工具提供了多种编译能力，开发者可以根据项目需求进行设置。请**注意** ，编译参数仅在 `build`、`server`、`release` 命令中可用

## 如何设置编译参数

通常有两种方式设置编译参数，以抽取单独的 source-map 文件为例：

  * 在命令行携带编译参数
```shell
aiot build \--devtool = source-map
```

  * 在项目根目录新建配置文件 quickapp.config.js，并配置 cli 属性；
```js
module.exports = { cli : { devtool : "source-map" , } , } ;
```

## 查看当前工具支持的全部编译参数
```shell
npx aiot build -h
```

## 常见编译参数

参数名 | 值类型 | 描述 | 默认值  
---|:---:|---|---  
\--devtool | `string` | sourcemap 的输出形式， 参数值及含义可以参考 [webpack/devtool (opens new window)](<https://www.webpackjs.com/configuration/devtool/#root>)   
示例：`aiot server --devtool=source-map` | none  
\--enable-jsc | `boolean` | 是否将 js 文件将转换为 jsc 文件，以提高运行性能   
示例：`aiot server --enable-jsc` | false  
\--enable-protobuf | `boolean` | 是否启用 protobuf 的二进制打包，以提高运行性能   
示例：`aiot server --enable-protobuf` | false  
\--enable-custom-component | `boolean` | 是否支持自定义组件   
示例：`aiot server --enable-custom-component` | false
