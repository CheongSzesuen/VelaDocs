<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/network/fetch.html -->

# Data Request fetch

## Interface Declaration

```json
{ "name": "system.fetch" }
```

## Import Module

```javascript
import fetch from '@system.fetch' 
// or 
const fetch = require('@system.fetch')
```

## Interface Definition

### fetch.fetch(OBJECT)

Obtains network data.

#### Parameters:

Parameter Name | Type | Required | Description
---|---|---|---
url | String | Yes | Resource URL
data | String/Object/ArrayBuffer | No | Request parameters, which can be a string, a JS object, or an arraybuffer object. Refer to the `data and Content-Type Relationship` section
header | Object | No | Request header. All its properties will be set to the request header part. Example of User-Agent setting: {"Accept-Encoding": "gzip, deflate","Accept-Language": "zh-CN,en-US;q=0.8,en;q=0.6"}
method | String | No | Default is GET. Options: OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT
responseType | String | No | Supported return types: text, json, file, arraybuffer. Default is determined by the Content-Type in the server response header. Refer to `success Return Value` for details
success | Function | No | Callback function for successful return
fail | Function | No | Callback function for failure, may fail due to permission issues
complete | Function | No | Callback function for completion (executed whether the call succeeds or fails) 

#### data and Content-Type Relationship

data | Content-Type | Description
---|---|---
String | Not set | Content-Type defaults to text/plain, data value is used as the request body
String | Any Type | data value is used as the request body
Object | Not set | Content-Type defaults to application/x-www-form-urlencoded, data is encoded and concatenated according to URL rules as the request body
Object | application/x-www-form-urlencoded | data is encoded and concatenated according to URL rules as the request body
Object | Any type other than application/x-www-form-urlencoded | -
ArrayBuffer | Not set | Content-Type defaults to application/octet-stream, data value is used as the request body
ArrayBuffer | Any Type | data value is used as the request body 

#### success Return Value:

Parameter Name | Type | Description
---|---|---
code | Integer | Server status code
data | String/Object /ArrayBuffer | Refer to the `responseType and data Relationship in success` section
headers | Object | All headers from the server response 

#### responseType and data Relationship in success:

responseType | data | Description
---|---|---
None | String | If the type in the server response header is text/* or application/json, application/javascript, application/xml, the value is the text content; otherwise, it is the URI of a temporary file. For temporary image or video files, the image can be set to the image component
text | String | Returns plain text
json | Object | Returns a JS object
file | String | Returns the URI of a temporary file
arraybuffer | ArrayBuffer | Returns an ArrayBuffer object 

#### Example:

```javascript
fetch.fetch({
  url: 'http://www.example.com',
  responseType: 'text',
  success: function(response) {
    console.log(`the status code of the response: ${response.code}`)
    console.log(`the data of the response: ${response.data}`)
    console.log(
      `the headers of the response: ${JSON.stringify(response.headers)}`
    )
  },
  fail: function(data, code) {
    console.log(`handling fail, errMsg = ${data}`)
    console.log(`handling fail, errCode = ${code}`)
  }
})

// We can also handle callbacks using promises
fetch
  .fetch({
    url: 'http://www.example.com',
    responseType: 'text'
  })
  .then(res => {
    const result = res.data

    console.log(`the status code of the response: ${result.code}`)
    console.log(`the data of the response: ${result.data}`)
    console.log(
      `the headers of the response: ${JSON.stringify(result.headers)}`
    )
  })
  .catch(error => {
    console.log(`handling fail, errMsg = ${error.data}`)
    console.log(`handling fail, errCode = ${error.code}`)
  })
```

## Support Details

Device Product | Description
---|---
Xiaomi S1 Pro Sports & Health Watch | Supported
Xiaomi Band 8 Pro | Not supported
Xiaomi Band 9 / 9 Pro | Not supported
Xiaomi Watch S3 | Supported
Redmi Watch 4 | Not supported
Xiaomi Wrist ECG & Blood Pressure Recorder | Not supported
Xiaomi Band 10 | Not supported
Xiaomi Watch S4 | Supported
REDMI Watch 5 | Supported
REDMI Watch 6 | Supported
