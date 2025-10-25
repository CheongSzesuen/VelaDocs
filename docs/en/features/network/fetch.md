<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/network/fetch.html -->

# Data Request

## Interface Declaration
```json
{ "name" : "system.fetch" }
```

## Import Module
```javascript
import fetch from '@system.fetch' // or const fetch = require('@system.fetch')
```

## Interface Definition

### fetch.fetch(OBJECT)

Fetch network data.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
url | String | Yes | Resource URL  
data | String/Object/ArrayBuffer | No | Request parameters, can be a string, or a JS object, arraybuffer object. Refer to the `data and Content-Type relationship` section  
header | Object | No | Request header, all its properties will be set to the request's header part. User-Agent setting example: {"Accept-Encoding": "gzip, deflate","Accept-Language": "zh-CN,en-US;q=0.8,en;q=0.6"}  
method | String | No | Default is GET, can be: OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT  
responseType | String | No | Supported return types are text, json, file, arraybuffer. Default is determined by the Content-Type in the server's response header. See `success return value` for details  
success | Function | No | Callback function for successful return  
fail | Function | No | Callback function for failure, may fail due to permission issues  
complete | Function | No | Callback function for completion (called whether successful or failed)  
  
#### Relationship between data and Content-Type

data | Content-Type | Description  
---|:---:|---  
String | Not set | Content-Type defaults to text/plain, data value is used as the request body  
String | Any Type | data value is used as the request body  
Object | Not set | Content-Type defaults to application/x-www-form-urlencoded, data is encoded and concatenated according to URL rules as the request body  
Object | application/x-www-form-urlencoded | data is encoded and concatenated according to URL rules as the request body  
Object | Any type other than application/x-www-form-urlencoded | -  
ArrayBuffer | Not set | Content-Type defaults to application/octet-stream, data value is used as the request body  
ArrayBuffer | Any Type | data value is used as the request body  
  
#### success Return Value:

Parameter Name | Type | Description  
---|:---:|---  
code | Integer | Server status code  
data | String/Object /ArrayBuffer | Refer to the `responseType and data relationship in success` section  
headers | Object | All headers from the server response  
  
#### Relationship between responseType and data in success:

responseType | data | Description  
---|:---:|---  
None | String | If the server's response header type is text/* or application/json, application/javascript, application/xml, the value is the text content; otherwise, it's the URI of a temporary file. For temporary image or video files, you can set the image to the image component  
text | String | Returns plain text  
json | Object | Returns a JS object  
file | String | Returns the URI of a temporary file  
arraybuffer | ArrayBuffer | Returns an ArrayBuffer object  
  
#### Example:
```javascript
fetch.fetch({ url : 'http://www.example.com' , responseType : 'text' , success : function(response){ console.log(` the status code of the response: ${ response.code } `)console.log(` the data of the response: ${ response.data } `)console.log(` the headers of the response: ${ JSON.stringify(response.headers)} `)} , fail : function(data , code){ console.log(` handling fail, errMsg = ${ data } `)console.log(` handling fail, errCode = ${ code } `)} })// We can also handle callbacks using promises fetch.fetch({ url : 'http://www.example.com' , responseType : 'text' }). then(res => { const result = res.data console.log(` the status code of the response: ${ result.code } `)console.log(` the data of the response: ${ result.data } `)console.log(` the headers of the response: ${ JSON.stringify(result.headers)} `)}). catch(error => { console.log(` handling fail, errMsg = ${ error.data } `)console.log(` handling fail, errCode = ${ error.code } `)})
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Supported  
Xiaomi Mi Band 8 Pro | Not supported  
Xiaomi Watch S3 | Supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG Blood Pressure Recorder | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported
