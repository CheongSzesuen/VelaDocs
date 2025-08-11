<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/other/prompt.html -->

# 弹窗 prompt

## 接口声明
```json
{ "name" : "system.prompt" }
```

## 导入模块
```javascript
import prompt from '@system.prompt' // 或 const prompt = require('@system.prompt')
```

## 接口定义

### prompt.showToast(OBJECT)

显示 Toast 提示信息

#### 参数

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
message | String | 是 | 显示的文本信息  
duration | Number | 否 | 显示持续时间，单位ms，默认值1500，建议区间：1500-10000  
  
#### 示例：
```javascript
prompt.showToast({ message : 'Message Info' , duration : 2000 })
```
