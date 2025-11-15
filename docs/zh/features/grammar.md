<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/grammar.html -->

# 通用语法

框架提供各种接口来获取应用的基本信息或者调用系统能力，每个接口包含若干 api 来执行具体的任务。接口使用前需要进行接口声明、模块导入，然后才能调用该接口下定义的若干 api。

## 接口声明

在 manifest.json 文件的 features 字段下进行声明，例如：
```javascript
[ { "name" : "system.network" } ]
```

## 导入模块

使用接口前，需要在代码里导入接口模块，例如：
```javascript
import network from '@system.network' // 或 const network = require('@system.network')
```

## 接口 api 调用

接口提供的 api 的调用方式大概有以下几种：

  * 同步 api
  * 异步 api
  * 订阅类 api

### 同步 api 调用

如果 api 没有返回值，一般会定义成同步 api，直接调用即可，例如：
```javascript
audio.play()
```

### 异步 api 调用

如果 api 有返回值，一般会定义成异步 api 的形式，这类 api 除了普通参数，还有“success \ fail \ complete“这三个通用参数——分别是 api 执行“成功 \ 失败 \ 完成“后的回调方法，调用时可以传入这三个参数来获取 api 执行成功的返回值或进行执行失败 \ 完成后的处理，这三个通用参数的说明如下：

名称 | 方法参数 | 参数类型 | 参数值 | 说明  
---|:---:|---|:---:|---  
success | data | any | api 执行的返回值，详见接口使用文档 | api 执行成功后触发  
fail | data | any | api 执行错误信息内容，一般是字符串，也可能是其他类型，详见接口使用文档 | api 执行失败后触发  
| code | number | api 执行错误码，详见通用错误码 |   
complete |:---:| - |:---:| api 执行完成后触发  
  
代码示例：
```javascript
storage.get({ key : 'A1' , success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### 订阅 / 取消订阅 api

订阅类 api 不会立即返回结果，这类 api 需要开发者传入回调函数作为参数，该回调函数会在 api 完成时或者事件变化时被触发，可以执行多次。该通用回调函数参数说明如下：

名称 | 方法参数 | 参数类型 | 参数值 | 说明  
---|:---:|---|:---:|---  
success | data | any | api 执行的返回值，详见接口使用文档 | api 调用成功或事件变更时触发，可能会触发多次  
fail | data | any | 错误信息内容，一般是字符串，也可能是其他类型，详见接口使用文档 | api 执行失败时触发。一旦触发该回调函数，success不会再次被调用，接口调用结束  
| code | number | api 执行错误码，详见通用错误码 |   
  
代码示例：
```javascript
geolocation.subscribe({ success : function(data){ console.log(` handling success: longitude = ${ data.longitude } , latitude = ${ data.latitude } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

## 通用错误码

所有接口的 api 在执行出现错误时，会返回统一定义的通用错误码或者 api 自己定义的特殊错误码。这里对通用错误码进行说明如下：

code | 定义  
---|---  
200 | 系统通用错误，所有系统未知异常发生时抛出。比如框架申请内存空间失败等  
201 | 用户拒绝  
202 | 参数错误，调用时未按照 api 定义进行正确的传参  
203 | 该功能不支持  
204 | 请求超时  
205 | 重复提交  
207 | 用户拒绝并选择不再询问  
300 | I/O 错误
