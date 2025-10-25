<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/multi-screens/conditional-compilation.html -->

# Conditional Compilation

Conditional compilation based on device features is a technique that determines which code should be included in an application during the compilation process based on characteristics such as device type and screen shape. This feature is suitable for cross-device application development, where different devices may require different code logic and interface layouts. Currently, the file types that support conditional compilation are: ux, js.

## Process

  1. Install conditional-compilation-webpack-plugin
```bash
npm install conditional-compilation-webpack-plugin -D
```

  2. Install cross-env
```bash
npm install cross-env -D
```

  3. Add a quickapp.config.js file in the project root directory and refer to the following configuration
```javascript
const ConditionalCompilationWebpackPlugin = require("conditional-compilation-webpack-plugin")module.exports = { plugins : [ new ConditionalCompilationWebpackPlugin() ] }
```

  4. Add scripts in package.json according to device features
```javascript
"scripts" : { "build:circle" : "cross-env DEVICE_TYPE=WATCH SHAPE=CIRCLE aiot build --enable-custom-component" , "build:rect" : "cross-env DEVICE_TYPE=WATCH SHAPE=RECT aiot build --enable-custom-component" }
```

  5. Use conditional compilation in code, refer to the following code
```html
< template > < div class = " home-page " > <!-- if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'CIRCLE' --> < input class = " btn bg-red " type = " button " value = " handleSet " @click = " handleSet " /> <!-- endif --> <!-- if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'RECT' --> < input class = " btn bg-blue " type = " button " value = " handleSet " @click = " handleSet " /> <!-- endif --> </ div > </ template > < script > export default { handleSet () { // if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'CIRCLE' console.log ('handleSet shape = circle') // endif // if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'RECT' console.log ('handleSet shape = rect') // endif } } ; </ script > < style > .home-page { align-items : flex-start ; justify-content : flex-start ; padding : 60px ; position : relative ; } .btn { height : 60px ; width : 360px ; text-align : center ; border-radius : 5px ; margin-bottom : 30px ; color : #ffffff ; font-size : 30px ; background-color : #0faeff ; } /* if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'CIRCLE' */ .bg-red { background-color : red ; } /* endif */ /* if true: process.env.DEVICE_TYPE === 'WATCH' && process.env.SHAPE === 'RECT' */ .bg-blue { background-color : blue ; } /* endif */ </ style >
```

  6. Execute the configured compilation command
```bash
npm run build:circle or npm run build:rect
```
