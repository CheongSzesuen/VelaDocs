<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/network.html -->

# Network Information

## Interface Declaration
```json
{ "name" : "system.network" }
```

## Import Module
```javascript
import network from '@system.network' // or const network = require('@system.network')
```

## Interface Definition

### network.getType(OBJECT)

Obtain the network type.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Callback for success  
fail | Function | No | Callback for failure, possibly due to lack of permissions  
complete | Function | No | Callback after execution completion  
  
#### Return Value of success:

Parameter Name | Type | Description  
---|:---:|---  
type | String | Network type, possible values: 2g, 3g, 4g, wifi, none, 5g, bluetooth, others  
  
#### Example:
```javascript
network.getType({ success : function(data){ console.log(` handling success: ${ data.type } `)} })
```

### network.subscribe(OBJECT)

Listen for changes in the network type. If called multiple times, only the last call will take effect.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
callback | Function | No | Callback triggered each time the network changes  
fail | Function | No | Callback for failure, possibly due to lack of permissions  
  
#### Return Value of callback:

Parameter Name | Type | Description  
---|:---:|---  
type | String | Network type, possible values: 2g, 3g, 4g, wifi, none, 5g, bluetooth, others. Note: A network type other than none does not guarantee that the device can access the target server. A request interface is required for verification.  
  
#### Example:
```javascript
network.subscribe({ callback : function(data){ console.log('handling callback')} })
```

### network.unsubscribe()

Cancel listening for changes in the network type.

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
Xiaomi Band 8 Pro | Not Supported  
Xiaomi Watch S3 | Supported  
Redmi Watch 4 | Not Supported  
Xiaomi Wrist ECG and Blood Pressure Monitor | Not Supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported
