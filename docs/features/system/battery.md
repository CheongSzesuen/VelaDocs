<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/battery.html -->

# 电量信息 battery

## 接口声明
```json
{ "name" : "system.battery" }
```

## 导入模块
```javascript
import battery from '@system.battery' // 或 const battery = require('@system.battery')
```

## 接口定义

### battery.getStatus(OBJECT)

获取当前设备的电量信息

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### success 返回值：

参数名 | 类型 | 说明  
---|:---:|---  
charging | Boolean | 是否正在充电  
level | Number | 当前电量，0.0 - 1.0 之间  
  
#### 示例
```javascript
battery.getStatus({ success : function(data){ console.log(` handling success: ${ data.level } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

## 支持明细

设备产品 | 说明  
---|---  
小米 S1 Pro 运动健康手表 | 不支持  
小米手环 8 Pro | 不支持  
Xiaomi Watch S3 | 不支持  
Redmi Watch 4 | 不支持  
小米腕部心电血压记录仪 | 不支持  
Xiaomi Watch S4 | 支持  
REDMI Watch 5 | 支持
