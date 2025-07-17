<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/multi-screens/conditional-compilation.html -->

# # 条件编译

基于设备特性的条件编译是一种在编译过程中根据设备类型和屏幕形状等特征来决定哪些代码应该被包含在应用程序中的技术。这项功能适用于跨设备应用开发，其中不同的设备可能需要不同的代码逻辑和界面布局。目前支持条件编译的文件类型有：ux、js。

## # 流程

  1. 安装 conditional-compilation-webpack-plugin

``` npm install conditional-compilation-webpack-plugin -D ```

  2. 安装 cross-env

``` npm install cross-env -D ```

  3. 在项目根目录中增加 quickapp.config.js 文件，并参考如下配置

``` const ConditionalCompilationWebpackPlugin = require("conditional-compilation-webpack-plugin") module.exports = { plugins: [new ConditionalCompilationWebpackPlugin()] } ```

  4. 根据设备特征，在 package.json 中添加脚本

``` "scripts": { "build:circle": "cross-env DEVICE_TYPE=WATCH SHAPE=CIRCLE aiot build --enable-custom-component", "build:rect": "cross-env DEVICE_TYPE=WATCH SHAPE=RECT aiot build --enable-custom-component" } ```

  5. 在代码中使用条件编译，参考如下代码

``` <template> <div class="home-page"> <!-- if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'CIRCLE' --> <input class="btn bg-red" type="button" value="handleSet" @click="handleSet" /> <!-- endif --> <!-- if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'RECT' --> <input class="btn bg-blue" type="button" value="handleSet" @click="handleSet" /> <!-- endif --> </div> </template> <script> export default { handleSet() { // if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'CIRCLE' console.log('handleSet shape = circle') // endif // if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'RECT' console.log('handleSet shape = rect') // endif } }; </script> <style> .home-page { align-items: flex-start; justify-content: flex-start; padding: 60px; position: relative; } .btn { height: 60px; width: 360px; text-align: center; border-radius: 5px; margin-bottom: 30px; color: #ffffff; font-size: 30px; background-color: #0faeff; } /* if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'CIRCLE' */ .bg-red { background-color: red; } /* endif */ /* if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'RECT' */ .bg-blue { background-color: blue; } /* endif */ </style> ```

  6. 执行配置好的编译命令

``` npm run build:circle 或 npm run build:rect ```

← [ 代码示例 ](</vela/quickapp/zh/guide/multi-screens/samples.html>) [ 拓展组件 ](</vela/quickapp/zh/guide/developer-materials/extension-components.html>) → 

快速导航

流程
