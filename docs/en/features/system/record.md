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

Parameter Name | Type | Required | Default Value | Description
---|---|---|---|---
duration | Number | No | 0 | Recording duration in milliseconds (ms). If duration is a valid value, recording will stop when the specified value is reached. By default, recording starts without a timed termination and needs to be stopped by calling the stop method. If the recording is interrupted during the process, the recording result will be returned immediately.
sampleRate | Number | No | 8000 | Sampling rate. Different audio formats support different ranges of sampling rates. The default is set to 8000. Recommended values are 8000/16000/32000/44100/48000.
numberOfChannels | Number | No | 1 | Number of recording channels, valid values are 1/2.
encodeBitRate | Number | No | 128000 | Encoding bit rate. The value of the encoding bit rate is related to the sampling rate and audio format. Refer to the bit rate values in the table below. Entering an incorrect value will result in the use of a calculated bit rate value based on the sampling rate and number of channels.
frameSize | Number | No | - | Frame size of PCM audio data in bytes. After recording content of the specified frame size, the recorded file content will be returned through the onframerecorded callback. If not specified, no callback will be triggered. Note: The size of the callback frame data may not be exactly the set frameSize and may be adjusted to a suitable value. When this parameter is set, the success callback will not return a uri. When an illegal value (e.g., a number less than or equal to zero) is passed, the success callback will return the uri normally, and the onframerecorded event will not be triggered.
format | String | No | pcm | Audio format, valid values are pcm/opus/wav. The default is pcm.
success | Function | No | - | Callback function for successful completion of recording.
fail | Function | No | - | Callback function for failure during recording.
complete | Function | No | - | Callback function after recording ends. 

#### PCM/WAV Bit Rate Reference

For pcm/wav recording scenarios, if an incorrect bit rate is entered, the encoder will calculate the bit rate based on the sampling rate and number of channels.

Sampling Rate (Hz) | Number of Channels | Bit Rate (bp/s)
---|---|---
8000 | 1 | 128000
8000 | 2 | 256000
16000 | 1 | 256000
16000 | 2 | 512000
32000 | 1 | 512000
32000 | 2 | 1024000
44100 | 1 | 705600
44100 | 2 | 1411200
48000 | 1 | 768000
48000 | 2 | 1536000 

#### Opus Bit Rate Reference

When recording in opus format, the bit rate ranges in the table below correspond to specific sampling rates and numbers of channels, providing the best encoding compression ratio algorithm efficiency. When the set bit rate is not within this range, recording can still proceed normally, but the compression ratio and algorithm efficiency will not be optimal.

Sampling Rate (Hz) | Number of Channels | Bit Rate (bp/s)
---|---|---
8000 | 1 | 8363 ~ 12800
8000 | 2 | 13892 ~ 19200
12000 | 1 | 11975 ~ 20400
12000 | 2 | 25427 ~ 34400
16000 | 1 | 14221 ~ 22800
16000 | 2 | 31651 ~ 44000
24000 | 1 | 24892 ~ 34000
24000 | 2 | 47685 ~ 64800
48000 | 1 | 50077 ~ 67200
48000 | 2 | 98554 ~ 103600 

#### Return Values for success:

Parameter Name | Type | Description
---|---|---
uri | String | Storage path of the recorded audio file, located in the application's cache directory. 

#### Error Codes for fail:

Error Code | Description
---|---
200 | Insufficient system space
205 | Recording is already in progress
202 | Parameter error 

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

## Events

### record.onframerecorded

Listen for events of files that have been recorded with the specified frame size. This event will be called back if frameSize is set.

#### Callback Object Parameters:

Parameter Name | Type | Description
---|---|---
frameBuffer | Uint8Array | Recorded audio data frame. Typically, the audio data frame size is the specified bufferSize, but if the specified bufferSize is too small, it will be automatically adjusted to a suitable size.
isLastFrame | boolean | Whether it is the last frame of data. 

#### Example:

```javascript
record.onframerecorded = function (res) {
  // Get audio data: res.frameBuffer
  // Whether it is the last frame: res.isLastFrame
  console.log('==== onframerecorded', res)
}
```

Notes:

  1. When the recording is interrupted, the current recording will end, and the success callback will be called with the recorded file address, and the complete callback will be called to end the previous recording.
  2. The current frameSize is limited by the size of a single data transmission in the underlying socket, with a maximum effective range of 4096. Setting a value larger than this range will take effect as the maximum value.
  3. During the recording process, the following operations may occur: SCO calls, ringing tones, alarm clocks, enforced emergency sounds, notification messages, or starting another recording. These operations will seize the audio focus and interrupt the current recording, changing its state to stop. The interrupted recording will call the success callback and return the recorded uri (for file recording) as well as the complete callback. For streaming recording, the onframerecorded event will report the last frame to complete the recording.
  4. Currently, the BES layer of the product has gain processing for recordings with a sampling rate of 16000 and a single channel, resulting in a louder audio volume compared to other configurations.

## Support Details

Device Product | Description
---|---
Xiaomi S1 Pro Sports & Health Watch | Not supported
Xiaomi Band 8 Pro | Not supported
Xiaomi Band 9 / 9 Pro | Not supported
Xiaomi Watch S3 | Not supported
Redmi Watch 4 | Not supported
Xiaomi ECG & Blood Pressure Wristband | Not supported
Xiaomi Smart Band 10 | Not supported
Xiaomi Watch S4 | Not supported
REDMI Watch 5 | Not supported
REDMI Watch 6 | Not supported
Xiaomi Watch S5 | Supported
