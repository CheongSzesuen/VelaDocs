<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/network/request.html -->

# Download request

## Interface statement

```json
{ "name": "system.request" }
```

## Import module

```javascript
import request from '@system.request' 
// or 
const request = require('@system.request')
```

## Interface definition

### request.download(OBJECT)

Download files

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
url | String | Yes | Resource URL  
header | String | No | Request header. All properties will be set in the request header.  
filename | String | No | Download file name. Default is obtained from the network request or URL.  
success | Function | No | Callback for successful response  
fail | Function | No | Callback for failed response  
complete | Function | No | Callback for completion (called on both success and failure)  
  
#### success return value:

Parameter | Type | Description  
---|:---:|---  
token | String | Download token, used to get the download status  
  
#### Example:

```javascript
request.download({
  url: 'http://www.example.com',
  success: function(data) {
    console.log(`handling success${data.token}`)
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

### request.onDownloadComplete(OBJECT)

Listen for download tasks

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
token | String | Yes | Token returned by the download interface  
success | Function | No | Callback for successful response  
fail | Function | No | Callback for failed response  
complete | Function | No | Callback for completion (called on both success and failure)  
  
#### success return value:

Parameter | Type | Description  
---|:---:|---  
uri | String | URI of the downloaded file (by default, this file is in the app's cache directory. If the file type is an image or video and needs to be viewed in the gallery or other apps, it should be moved to a public directory using methods from the media interface)  
  
#### fail error codes:

Error code | Description  
---|---  
1000 | Download failed  
1001 | Download task does not exist  
  
#### Example:

```javascript
request.onDownloadComplete({
  token: '123',
  success: function(data) {
    console.log(`handling success${data.uri}`)
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

## Support details

Device | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Band 9 / 9 Pro | Not supported  
Xiaomi Watch S3 | Supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG and Blood Pressure Recorder | Not supported  
Xiaomi Band 10 | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported  
REDMI Watch 6 | Supported
