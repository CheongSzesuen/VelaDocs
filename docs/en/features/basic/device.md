<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/basic/device.html -->

# Device Information

## Interface Declaration
```json
{ "name" : "system.device" }
```

## Importing the Module
```javascript
import device from '@system.device' // or const device = require('@system.device')
```

## Interface Definitions

### device.getInfo(OBJECT)

Obtains device information.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback invoked when the execution is complete  
  
#### Return Value of success:

Parameter | Type | Description  
---|:---:|---  
brand | string | Device brand  
manufacturer | string | Device manufacturer  
model | string | Device model  
product | string | Device code name  
osType | string | Operating system name  
osVersionName | string | Operating system version name  
osVersionCode | number | Operating system version number  
platformVersionName | string | Runtime platform version name  
platformVersionCode | number | Runtime platform version number  
language | string | System language  
region | string | System region  
APILevel[2+](</vela/quickapp/zh/guide/version/APILevel2>) | number | Framework API version  
screenWidth | number | Screen width  
screenHeight | number | Screen height  
screenDensity[3+](</vela/quickapp/zh/guide/version/APILevel3>) | number | Screen density, that is, the device pixel ratio (DPR), which is the ratio of the device's physical pixels to logical pixels (DP). The calculation formula is: DPR = device PPI / 160, where PPI (pixels per inch) indicates the number of pixels per inch.  
screenShape | string | Screen shape. The value can be: rect (rectangular screen), circle (circular screen), or pill-shaped[3+](</vela/quickapp/zh/guide/version/APILevel3>) (capsule-shaped screen).  
deviceType[2+](</vela/quickapp/zh/guide/version/APILevel2>) | string | Device type. The value can be: watch, band, or smartspeaker.  
  
#### Example:
```javascript
device.getInfo({ success : function(ret){ console.log(` handling success， brand = ${ ret.brand } `)} })
```

### device.getDeviceId(OBJECT)

Obtains the unique device identifier.

#### Permission Requirements

Obtaining device information

Developers need to configure the permission in manifest.json:
```json
{ "permissions" : [ { "name" : "hapjs.permission.DEVICE_INFO" } ] }
```

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback invoked when the execution is complete  
  
#### Return Value of success:

Parameter | Type | Description  
---|:---:|---  
deviceId | String | Unique device identifier  
  
#### Example:
```javascript
device.getDeviceId({ success : function(data){ console.log(` handling success: ${ data.deviceId } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} , })
```

### device.getSerial(OBJECT)

Obtains the device serial number.

#### Permission Requirements

Obtaining device information

Developers need to configure the permission in manifest.json:
```json
{ "permissions" : [ { "name" : "hapjs.permission.DEVICE_INFO" } ] }
```

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback invoked when the execution is complete  
  
#### Return Value of success:

Parameter | Type | Description  
---|:---:|---  
serial | String | Device serial number
```javascript
device.getSerial({ success :(data)=> { console.log(` handling success: ${ data.serial } `)} , fail :(data , code)=> { console.log(` handling fail, code = ${ code } `)} })
```

### device.getTotalStorage(OBJECT)

Obtains the total size of the storage space.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback invoked when the execution is complete  
  
#### Return Value of success:

Parameter | Type | Description  
---|:---:|---  
totalStorage | Number | Total size of the storage space, in bytes
```javascript
device.getTotalStorage({ success :(data)=> { console.log(` handling success: ${ data.totalStorage } `)} , fail :(data , code)=> { console.log(` handling fail, code = ${ code } `)} })
```

### device.getAvailableStorage(OBJECT)

Obtains the available size of the storage space.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback invoked when the execution is complete  
  
#### Return Value of success:

Parameter | Type | Description  
---|:---:|---  
availableStorage | Number | Available size of the storage space, in bytes
```javascript
device.getAvailableStorage({ success :(data)=> { console.log(` handling success: ${ data.availableStorage } `)} , fail :(data , code)=> { console.log(` handling fail, code = ${ code } `)} })
```
