<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/record.html -->

# Record

## Interface Declaration
```json
{ "name" : "system.record" }
```

## Importing the Module
```javascript
import record from '@system.record' // or const record = require('@system.record')
```

## Interface Definition

### record.start(OBJECT)

Starts recording

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
duration | Number | No | Recording duration in ms. If duration is a valid value, recording will stop when the specified value is reached  
sampleRate | Number | No | Sampling rate. The supported sampling rate ranges vary for different audio formats. The default is 8000, and it is recommended to use 8000/16000/32000/44100/48000  
numberOfChannels | Number | No | Number of recording channels, valid values are 1/2  
encodeBitRate | Number | No | Encoding bitrate. The encoding bitrate value depends on the sampling rate and audio format  
format | String | No | Audio format, valid values are pcm/opus/wav. Defaults to pcm  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution is completed  
  
#### success Return Value:

Parameter Name | Type | Description  
---|:---:|---  
uri | String | Storage path of the recording file, located in the application's cache directory  
  
#### fail Return Error Codes:

Error Code | Description  
---|---  
205 | Recording is already in progress  
202 | Parameter error  
  
#### Example:
```javascript
record.start({ duration : 10000 , sampleRate : 8000 , numberOfChannels : 1 , encodeBitRate : 128000 , format : 'pcm' , success : function(data){ console.log(` handling success: ${ data.uri } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } , errorMsg= ${ data } `)} , complete : function() { console.log(` handling complete `)} })
```

### record.stop()

Stops recording

#### Parameters:

None

#### Example:
```javascript
record.stop()
```
