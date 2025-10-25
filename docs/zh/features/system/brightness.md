<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/brightness.html -->

# 屏幕亮度 brightness

## 接口声明
```json
{ "name" : "system.brightness" }
```

## 导入模块
```javascript
import brightness from '@system.brightness' // 或 const brightness = require('@system.brightness')
```

## 接口定义

### brightness.getValue(OBJECT)

获得当前屏幕亮度值

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### success 返回值：

参数值 | 类型 | 说明  
---|:---:|---  
value | Integer | 屏幕亮度，取值范围 0-255  
  
#### 示例：
```javascript
brightness.getValue({ success : function(data){ console.log(` handling success, value = ${ data.value } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### brightness.setValue(OBJECT)

设置当前屏幕亮度值

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
value | Integer | 是 | 屏幕亮度，取值范围 0-255  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### 示例：
```javascript
brightness.setValue({ value : 100 , success : function() { console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### brightness.getMode(OBJECT)

获得当前屏幕亮度模式

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### success 返回值：

参数值 | 类型 | 说明  
---|:---:|---  
mode | Integer | 0 为手动调节屏幕亮度，1 为自动调节屏幕亮度  
  
#### 示例：
```javascript
brightness.getMode({ success : function(data){ console.log(` handling success, mode = ${ data.mode } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### brightness.setMode(OBJECT)

设置当前屏幕亮度模式

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
mode | Integer | 是 | 0 为手动调节屏幕亮度，1 为自动调节屏幕亮度  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### 示例：
```javascript
brightness.setMode({ mode : 1 , success : function() { console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### brightness.setKeepScreenOn(OBJECT)

设置是否保持常亮状态

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
keepScreenOn | Boolean | 是 | 是否保持屏幕常亮  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### 示例：
```javascript
brightness.setKeepScreenOn({ keepScreenOn : true , success : function() { console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```
