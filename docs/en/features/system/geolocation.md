<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/geolocation.html -->

# Geolocation

## Interface Declaration
```json
{ "name" : "system.geolocation" }
```

## Import Module
```javascript
import geolocation from '@system.geolocation' // or const geolocation = require('@system.geolocation')
```

## Interface Definition

### geolocation.getLocation(OBJECT)

Obtain the geolocation

#### Permission Requirements

Precise device location

Developers need to configure permissions in manifest.json:
```json
{ "permissions" : [ { "name" : "hapjs.permission.LOCATION" } ] }
```

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
timeout | Number | No | Set timeout in ms. Default is 30000  
success | Function | Yes | Success callback  
fail | Function | No | Failure callback, possibly due to lack of permissions  
complete | Function | No | Callback after execution ends  
  
#### Return Values for success:

Parameter Name | Type | Description  
---|:---:|---  
longitude | Number | Longitude, floating-point number  
latitude | Number | Latitude, floating-point number  
altitude | Number | Altitude/height in meters, floating-point number  
speed | Number | Speed in m/s, floating-point number  
accuracy | Number | Accuracy, positive integer  
accuracyInfo | { horizontal: Number, vertical: Number } | Accuracy information, including horizontal and vertical precision  
  
#### Error Codes for fail:

Error Code | Description  
---|---  
203 | Function not supported  
204 | Timeout occurred  
  
#### Example:
```javascript
geolocation.getLocation({ success : function(data){ console.log(` handling success: longitude = ${ data.longitude } , latitude = ${ data.latitude } , speed = ${ data.speed } , altitude = ${ data.altitude } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } , errorMsg= ${ data } `)} })
```

### geolocation.subscribe(OBJECT)

Listen for geolocation changes. If called multiple times, only the last call takes effect.

#### Permission Requirements

Precise device location

Developers need to configure permissions in manifest.json:
```json
{ "permissions" : [ { "name" : "hapjs.permission.LOCATION" } ] }
```

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
callback | Function | Yes | Called back whenever location changes  
fail | Function | No | Failure callback  
  
#### Return Values for callback:

Parameter Name | Type | Description  
---|:---:|---  
longitude | Number | Longitude, floating-point number  
latitude | Number | Latitude, floating-point number  
altitude | Number | Altitude/height in meters, floating-point number  
speed | Number | Speed in m/s, floating-point number  
accuracy | Number | Accuracy, positive integer  
  
#### Error Codes for fail:

Error Code | Description  
---|---  
203 | Function not supported  
  
#### Example:
```javascript
geolocation.subscribe({ callback : function(data){ console.log(` handling success: longitude = ${ data.longitude } , latitude = ${ data.latitude } , speed = ${ data.speed } , altitude = ${ data.altitude } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } , errorMsg= ${ data } `)} })
```

### geolocation.unsubscribe()

Cancel listening for geolocation changes

#### Permission Requirements

Precise device location

Developers need to configure permissions in manifest.json:
```json
{ "permissions" : [ { "name" : "hapjs.permission.LOCATION" } ] }
```

#### Parameters:

None

#### Example:
```javascript
geolocation.unsubscribe()
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Not supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Watch S3 | Supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG Blood Pressure Monitor | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported
