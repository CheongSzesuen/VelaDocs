<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/network/request.html -->

# Download

## Interface Declaration
```json
{ "name" : "system.request" }
```

## Import Module
```javascript
import request from '@system.request' // or const request = require('@system.request')
```

## Interface Definition

### request.download(OBJECT)

Download files

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
url | String | Yes | Resource URL  
header | String | No | Request header, all properties will be set to the header part of the request  
filename | String | No | Download filename. Default is obtained from the network request or URL  
success | Function | No | Callback function for successful response  
fail | Function | No | Callback function for failed response  
complete | Function | No | Callback function for completion (called on both success and failure)  
  
#### success Return Value:

Parameter | Type | Description  
---|:---:|---  
token | String | Download token, used to get the download status  
  
#### Example:
```javascript
request.download({ url : 'http://www.example.com' , success : function(data){ console.log(` handling success ${ data.token } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### request.onDownloadComplete(OBJECT)

Listen for download tasks

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
token | String | Yes | Token returned by the download interface  
success | Function | No | Callback function for successful response  
fail | Function | No | Callback function for failed response  
complete | Function | No | Callback function for completion (called on both success and failure)  
  
#### success Return Value:

Parameter | Type | Description  
---|:---:|---  
uri | String | URI of the downloaded file (by default, this file is in the application cache directory. If the file type is an image or video and it is required for the user to view it in applications like the gallery, the file needs to be transferred to a public directory. This can be achieved using the methods in the media interface)  
  
#### fail Error Codes:

Error Code | Description  
---|---  
1000 | Download failed  
1001 | Download task does not exist  
  
#### Example:
```javascript
request.onDownloadComplete({ token : '123' , success : function(data){ console.log(` handling success ${ data.uri } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Watch S3 | Supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG Blood Pressure Recorder | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported
