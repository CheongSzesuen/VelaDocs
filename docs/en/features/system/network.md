<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/network.html -->

# Network Information network

## Interface Declaration

```json
{ "name": "system.network" }
```

## Import Module

```javascript
import network from '@system.network' 
// or 
const network = require('@system.network')
```

## Interface Definition

### network.getType(OBJECT)

Obtain the network type.

#### Parameters:

Parameter Name | Type | Required | Description
---|---|---|---
success | Function | No | Callback for success
fail | Function | No | Callback for failure, possibly due to lack of permissions
complete | Function | No | Callback after execution ends 

#### Object Value Returned by success:

Parameter Name | Type | Description
---|---|---
type | String | Network type, with possible values of 2g, 3g, 4g, wifi, none, 5g, bluetooth, others 

#### Example:

```javascript
network.getType({
  success: function(data) {
    console.log(`handling success: ${data.type}`)
  }
})
```

### network.subscribe(OBJECT)

Listen for changes in network type. If called multiple times, only the last call will take effect.

#### Parameters:

Parameter Name | Type | Required | Description
---|---|---|---
callback | Function | No | Callback triggered each time the network changes
fail | Function | No | Callback for failure, possibly due to lack of permissions 

#### Object Value Returned by callback:

Parameter Name | Type | Description
---|---|---
type | String | Network type, with possible values of 2g, 3g, 4g, wifi, none, 5g, bluetooth, others. Note: A network type other than none does not guarantee that the device can definitely access the target server; a request interface is required for judgment. 

#### Example:

```javascript
network.subscribe({
  callback: function(data) {
    console.log(`handling callback ${data.type}`)
  }
})
```

### network.unsubscribe()

Cancel listening for changes in network type.

#### Parameters:

None

#### Example:

```javascript
network.unsubscribe()
```

## Support Details

Device Product | Description
---|---
Xiaomi S1 Pro Sports and Health Watch | Supported
Xiaomi Band 8 Pro | Not supported
Xiaomi Band 9 / 9 Pro | Not supported
Xiaomi Watch S3 | Supported
Redmi Watch 4 | Not supported
Xiaomi Wrist ECG Blood Pressure Monitor | Not supported
Xiaomi Band 10 | Not supported
Xiaomi Watch S4 | Supported
REDMI Watch 5 | Supported
REDMI Watch 6 | Supported
Xiaomi Watch S5 | Supported
