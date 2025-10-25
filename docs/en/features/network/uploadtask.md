<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/network/uploadtask.html -->

# Upload3+

## Interface Declaration
```json
{ "name" : "system.uploadtask" }
```

## Import Module
```javascript
import uploadtask from '@system.uploadtask' // or const uploadtask = require('@system.uploadtask')
```

## Interface Definition

### Methods

### UploadTask uploadtask.uploadFile(OBJECT)

Creates an upload request. Each successful call to uploadtask.uploadFile returns an UploadTask instance for the current request.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
url | String | Yes | Developer server interface address  
filePath | String | Yes | Path to the file resource to upload (local path)  
name | String | Yes | Key corresponding to the file. The developer can use this key to obtain the binary content of the file on the server side.  
header | Object | No | Request header. All its properties will be set in the header part of the request.  
formData | Object | No | Additional form data in the HTTP request  
timeout | Number | No | Timeout duration in milliseconds  
success | Function | No | Callback function for successful return  
fail | Function | No | Callback function for failure  
complete | Function | No | Callback function for completion (called on both success and failure)  
  
#### success Return Value:

Parameter Name | Type | Description  
---|:---:|---  
statusCode | Integer | Server status code  
data | String | Data returned by the developer server  
headers | Object | All headers from the server response  
  
# UploadTask

## Methods

### UploadTask.abort()

Interrupts the upload task.

### UploadTask.onProgressUpdate(callback)

Listens for upload progress change events.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
callback | Function | Yes | Callback function for upload progress change events  
  
#### callback Return Value:

Parameter Name | Type | Description  
---|:---:|---  
progress | Number | Upload progress percentage  
totalBytesSent | Number | Length of data already uploaded, in Bytes  
totalBytesExpectedToSend | Number | Expected total length of data to upload, in Bytes  
  
### UploadTask.offProgressUpdate(function callback)

Cancels listening for upload progress change events. callback is optional. If not provided, all upload progress change events listened to via onProgressUpdate will be canceled.

#### Example:
```javascript
const retUploadTask = uploadtask.uploadFile({ url : 'http://www.example.com' , filePath : "internal://mass/download/test.png" , name : "testImg" , success : function(res){ console.log("Upload success.resp = " \+ JSON.stringify(res)) } , fail : function(data , code){ console.log(` handling fail, errMsg = ${ data)} `)console.log(` handling fail, errCode = ${ code } `)} })// Interrupt the request task retUploadTask.abort() // Listen for upload progress events retUploadTask.onProgressUpdate(res => { console.log(` listening upload progress update event, progressUpdate data = ${ JSON.stringify(res)} `)})// Cancel listening for upload progress events retUploadTask.offProgressUpdate()
```

Cancel a specific upload progress event
```javascript
function cb(res){ console.log(` listening for upload progress update event 1, progressUpdate data = ${ JSON.stringify(res)} `)} // This listener will be canceled retUploadTask.onProgressUpdate(cb)// event2 listener remains valid and will not be canceled retUploadTask.onProgressUpdate((res)=> { console.log(` listening for upload progress update event 2, progressUpdate data = ${ JSON.stringify(res)} `)})retUploadTask.offProgressUpdate(cb)
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Not supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Watch S3 | Supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG and Blood Pressure Recorder | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported
