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

Obtain the geolocation.

#### Permission Requirements

Precise device positioning.

Developers need to configure permissions in manifest.json:
```json
{ "permissions" : [ { "name" : "hapjs.permission.LOCATION" } ] }
```

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
timeout | Number | No | Set the timeout period in milliseconds. The default value is 30000.  
success | Function | Yes | Callback function for success.  
fail | Function | No | Callback function for failure, possibly due to lack of permissions.  
complete | Function | No | Callback function after execution is complete.  
  
#### Return Values for success:

Parameter Name | Type | Description  
---|:---:|---  
longitude | Number | Longitude, floating-point number.  
latitude | Number | Latitude, floating-point number.  
altitude | Number | Altitude/height in meters, floating-point number.  
speed | Number | Speed value in meters per second, floating-point number.  
accuracy | Number | Accuracy, positive integer value.  
accuracyInfo | { horizontal: Number, vertical: Number } | Accuracy information, including horizontal and vertical accuracy.  
  
#### Error Codes Returned by fail:

Error Code | Description  
---|---  
203 | This function is not supported.  
204 | Timeout occurred.  
  
#### Example:
```javascript
geolocation.getLocation({ success : function(data){ console.log(` handling success: longitude = ${ data.longitude } , latitude = ${ data.latitude } , speed = ${ data.speed } , altitude = ${ data.altitude } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } , errorMsg= ${ data } `)} })
```

### geolocation.subscribe(OBJECT)

Listen for geolocation changes. If called multiple times, only the last call takes effect.

#### Permission Requirements

Precise device positioning.

Developers need to configure permissions in manifest.json:
```json
{ "permissions" : [ { "name" : "hapjs.permission.LOCATION" } ] }
```

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
callback | Function | Yes | Callback function invoked each time the location information changes.  
fail | Function | No | Callback function for failure.  
  
#### Return Values for callback:

Parameter Name | Type | Description  
---|:---:|---  
longitude | Number | Longitude, floating-point number.  
latitude | Number | Latitude, floating-point number.  
altitude | Number | Altitude/height in meters, floating-point number.  
speed | Number | Speed value in meters per second, floating-point number.  
accuracy | Number | Accuracy, positive integer value.  
  
#### Error Codes Returned by fail:

Error Code | Description  
---|---  
203 | This function is not supported.  
  
#### Example:
```javascript
geolocation.subscribe({ callback : function(data){ console.log(` handling success: longitude = ${ data.longitude } , latitude = ${ data.latitude } , speed = ${ data.speed } , altitude = ${ data.altitude } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } , errorMsg= ${ data } `)} })
```

### geolocation.unsubscribe()

Cancel listening for geolocation changes.

#### Permission Requirements

Precise device positioning.

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
Xiaomi S1 Pro Sports and Health Watch | Not supported  
Xiaomi Smart Band 8 Pro | Not supported  
Xiaomi Smart Band 9 / 9 Pro | Not supported  
Xiaomi Watch S3 | Supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG Blood Pressure Monitor | Not supported  
Xiaomi Smart Band 10 | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported  
REDMI Watch 6 | Supported
