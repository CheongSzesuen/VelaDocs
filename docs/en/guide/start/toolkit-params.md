<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/start/toolkit-params.html -->

# Build Parameters

The build tool offers various build capabilities that developers can configure based on project requirements. Please **note** that build parameters are only available in the `build`, `server`, and `release` commands.

## How to Set Build Parameters

There are typically two ways to set build parameters, taking the extraction of a separate source-map file as an example:

  * Include build parameters in the command line
```shell
aiot build \--devtool = source-map
```

  * Create a configuration file named quickapp.config.js in the project root directory and configure the cli property;
```js
module.exports = { cli : { devtool : "source-map" , } , } ;
```

## View All Supported Build Parameters
```shell
npx aiot build -h
```

## Common Build Parameters

Parameter Name | Value Type | Description | Default  
---|:---:|---|---  
\--devtool | `string` | The output format of the sourcemap. For parameter values and their meanings, refer to [webpack/devtool (opens new window)](<https://www.webpackjs.com/configuration/devtool/#root>)   
Example: `aiot server --devtool=source-map` | none  
\--enable-jsc | `boolean` | Whether to convert js files to jsc files to improve runtime performance   
Example: `aiot server --enable-jsc` | false  
\--enable-protobuf | `boolean` | Whether to enable protobuf binary packaging to improve runtime performance   
Example: `aiot server --enable-protobuf` | false  
\--enable-custom-component | `boolean` | Whether to support custom components   
Example: `aiot server --enable-custom-component` | false
