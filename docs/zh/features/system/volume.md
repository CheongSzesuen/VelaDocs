<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/volume.html -->

# 系统音量 volume

## 接口声明
```json
{ "name" : "system.volume" }
```

## 导入模块
```javascript
import volume from '@system.volume' // 或 const volume = require('@system.volume')
```

## 接口定义

### volume.getMediaValue (OBJECT)

获取当前多媒体音量

#### 参数

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### success 返回值：

参数值 | 类型 | 说明  
---|:---:|---  
value | Number | 系统媒体当前音量，0.0-1.0 之间  
  
#### 示例
```javascript
volume.getMediaValue({ success : function(data){ console.log(` handling success: ${ data.value } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### volume.setMediaValue (OBJECT)

设置当前多媒体音量

#### 参数

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
value | Number | 是 | 设置的音量，0.0-1.0 之间  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### fail 返回值：

[支持通用错误码](</vela/quickapp/zh/features/grammar.html#通用错误码>)

#### 示例
```javascript
volume.setMediaValue({ value : 0.5 , success : function() { console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

## 事件

### volume.onMediaValueChanged

多媒体音量发生变化事触发

#### 回调Object参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
value | Number | 是 | 系统媒体当前音量，范围：0.0-1.0 之间  
  
#### 示例
```javascript
volume.onMediaValueChanged = function(res){ console.log('volume media value changed:' , res.value)}
```
