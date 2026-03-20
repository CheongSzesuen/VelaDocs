<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/battery.html -->

# Power Information battery

## Interface Declaration

```json
{ "name": "system.battery" }
```

## Import Module

```javascript
import battery from '@system.battery' 
// or 
const battery = require('@system.battery')
```

## Interface Definition

### battery.getStatus(OBJECT)

Obtain the power information of the current device.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Callback for success  
fail | Function | No | Callback for failure  
complete | Function | No | Callback after execution completion  
  
#### Return Values for success:

Parameter Name | Type | Description  
---|:---:|---  
charging | Boolean | Whether it is currently charging  
level | Number | Current power level, ranging from 0.0 to 1.0  
  
#### Example

```javascript
battery.getStatus({
  success: function(data) {
      console.log(`handling success: ${data.level}`)
  },
  fail: function(data, code) {
      console.log(`handling fail, code = ${code}`)
  }
})
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports and Health Watch | Not supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Band 9 / 9 Pro | Not supported  
Xiaomi Watch S3 | Not supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG Blood Pressure Monitor | Not supported  
Xiaomi Band 10 | Supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported  
REDMI Watch 6 | Supported
