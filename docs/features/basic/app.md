<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/basic/app.html -->

# 应用上下文 app

## 接口声明

无需声明

## 导入模块
```javascript
import app from '@system.app' // 或 const app = require('@system.app')
```

## 接口定义

### app.getInfo()

获取当前应用信息

#### 参数：

无

#### 返回值：

参数名 | 类型 | 说明  
---|:---:|---  
packageName | String | 应用包名  
icon | String | 应用图标路径  
name | String | 应用名称  
versionName | String | 应用版本名称  
versionCode | Integer | 应用版本号  
logLevel | String | log 级别  
source | Object | 应用来源  
  
#### source

参数名 | 类型 | 说明  
---|:---:|---  
packageName | String | 来源 app 的包名，一级来源  
type | String | 来源类型，二级来源，值为 shortcut、push、url、barcode、nfc、bluetooth、other  
  
#### 示例：
```javascript
console.log(JSON.stringify(app.getInfo()))
```

```json
// console 值打印 { // 应用包名 "packageName" : "com.example.demo" , // 应用名称 "name" : "demo" , // 应用版本名称 "versionName" : "1.0.0" , // 应用版本号 "versionCode" : 1 , // 应用图片 "icon" : "/common/logo.png" , // log 级别 "logLevel" : "debug" , // 应用来源 "source" : { // 来源app的包名 "packageName" : "" , // 来源类型 "type" : "shortcut" } }
```

### app.terminate()

退出当前应用

#### 参数：

无

#### 返回值：

无

#### 示例：
```javascript
app.terminate()
```

### app.canIUse()3+

#### 参数：

类型 | 描述  
---|---  
String | 要查询的能力，格式见下方  
  
#### 返回值：

类型 | 描述  
---|---  
Boolean | 查询的能力是否支持  
  
### 入参格式

#### 查询接口
```javascript
// 查询feature下的方法是否支持 '@${featureName}.${method}' // 查询某个feature是否支持 '@${featureName}'
```

**示例**
```javascript
import app from '@system.app' ; if(app.canIUse('@system.router.push')) { // 可以使用方法@system.router.push } if(app.canIUse('@system.router')) { // 可以使用@system.router接口 }
```

#### 查询组件

type取值可以是`'attr'`、`'style'`、`'method'`，分别对应组件的属性、样式、方法。
```javascript
// 查询组件下的属性、样式、方法是否支持 ` ${ componentName } . ${ type } . ${ name } ` // 查询组件是否支持 ` ${ componentName } `
```

**示例**
```javascript
import app from '@system.app' ; if(app.canIUse('scroll')) { // 可以使用scroll组件 } if(app.canIUse('scroll.attr.scroll-x')) { // 可以使用scroll组件的scroll-x属性 }
```
