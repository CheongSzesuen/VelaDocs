<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/battery.html -->

# Battery Information

## Interface Declaration
```json
{ "name" : "system.battery" }
```

## Import Module
```javascript
import battery from '@system.battery' // or const battery = require('@system.battery')
```

## Interface Definition

### battery.getStatus(OBJECT)

Obtain the battery information of the current device.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution ends  
  
#### Return Values for success:

Parameter Name | Type | Description  
---|:---:|---  
charging | Boolean | Whether it is currently charging  
level | Number | Current battery level, between 0.0 and 1.0  
  
#### Example
```javascript
battery.getStatus({ success : function(data){ console.log(` handling success: ${ data.level } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Not supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Watch S3 | Not supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG and Blood Pressure Recorder | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported
