<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/record.html -->

# Audio recording

## Interface declaration

```json
{ "name": "system.record" }
```

## Import module

```javascript
import record from '@system.record' 
// or 
const record = require('@system.record')
```

## Interface definition

### record.start(OBJECT)

Starts audio recording.

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
duration | Number | No | Audio recording duration in ms. If a valid value is specified for duration, the recording stops when the specified duration is reached.
sampleRate | Number | No | Sampling rate. The supported sampling rate ranges vary for different audio formats. The default value is 8000. It is recommended to use 8000/16000/32000/44100/48000.
numberOfChannels | Number | No | Number of audio recording channels. Valid values: 1/2
encodeBitRate | Number | No | Encoding bitrate. The value of encoding bitrate depends on the sampling rate and audio format.
format | String | No | Audio format. Valid values: pcm/opus/wav. Default value: pcm
success | Function | No | Callback invoked when the operation succeeds.
fail | Function | No | Callback invoked when the operation fails.
complete | Function | No | Callback invoked when the operation completes, either successfully or unsuccessfully. 

#### Return value of success:

Parameter | Type | Description
---|---|---
uri | String | Storage path of the audio recording file, which is in the cache directory of the application. 

#### Error codes for fail:

Error code | Description
---|---
205 | Audio recording is in progress.
202 | Incorrect parameter. 

#### Example:

```javascript
record.start({
  duration: 10000,
  sampleRate: 8000,
  numberOfChannels: 1,
  encodeBitRate: 128000,
  format: 'pcm',
  success: function(data) {
    console.log(`handling success: ${data.uri}`)
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}, errorMsg=${data}`)
  },
  complete: function () {
    console.log(`handling complete`)
  }
})
```

### record.stop()

Stops audio recording.

#### Parameters:

None

#### Example:

```javascript
record.stop()
```

## Support details

Device product | Description
---|---
Xiaomi S1 Pro Sports & Health Watch | Not supported
Xiaomi Smart Band 8 Pro | Not supported
Xiaomi Smart Band 9 / 9 Pro | Not supported
Xiaomi Watch S3 | Not supported
Redmi Watch 4 | Not supported
Xiaomi ECG & Blood Pressure Wristband | Not supported
Xiaomi Smart Band 10 | Not supported
Xiaomi Watch S4 | Not supported
REDMI Watch 5 | Not supported
REDMI Watch 6 | Not supported
