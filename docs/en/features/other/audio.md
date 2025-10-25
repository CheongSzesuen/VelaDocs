<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/other/audio.html -->

# Audio

## Interface Declaration
```json
{ "name" : "system.audio" }
```

## Importing the Module
```javascript
import audio from '@system.audio' // or const audio = require('@system.audio')
```

## Methods

### audio.play()

Starts audio playback.

#### Parameters

None

#### Example:
```javascript
audio.play()
```

### audio.pause()

Pauses audio playback.

#### Parameters

None

#### Example:
```javascript
audio.pause()
```

### audio.stop()

Stops audio playback. Playback can be restarted with play.

#### Parameters

None

#### Example:
```javascript
audio.stop()
```

### audio.getPlayState(OBJECT)

Retrieves the current playback state data.

#### Parameters

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### success Return Value:

Parameter Value | Type | Description  
---|:---:|---  
state | String | Playback state: 'play', 'pause', 'stop'  
src | String | URI of the currently playing audio media; empty string when stopped  
currentTime | Number | Current progress of the audio in seconds; -1 when stopped  
percent | Number | Current playback progress percentage (0-100)  
autoplay | Boolen | Whether the audio is autoplaying  
loop | Boolen | Whether the audio is looping  
volume | Number | Audio volume (default: system media volume; range: [0.0,1.0])  
muted | Boolen | Whether the audio is muted  
duration | Number | Duration of the audio in seconds; NaN if unknown  
  
#### Example:
```javascript
audio.getPlayState({ success : function(data){ console.log(` handling success: state: ${ data.state } ,src: ${ data.src } ,currentTime: ${ data.currentTime } ,autoplay: ${ data.autoplay } ,loop: ${ data.loop } ,volume: ${ data.volume } ,muted: ${ data.muted } ,notificationVisible: ${ data.notificationVisible } `)} , fail : function(data , code){ console.log('handling fail, code=' \+ code)} })
```

## Properties

Name | Type | Readable | Writable | Required | Description  
---|:---:|---|:---:|---|---  
src | String | Yes | Yes | Yes | URI of the audio media to play  
currentTime | Number | Yes | Yes | No | Current progress of the audio in seconds; setting this adjusts playback position  
duration | Number | Yes | No | No | Duration of the audio in seconds; NaN if unknown  
autoplay | Boolean | Yes | Yes | No | Whether the audio autoplays (default: false)  
loop | Boolean | Yes | Yes | No | Whether the audio loops (default: false)  
volume | Number | Yes | Yes | No | Audio volume (default: system media volume; range: [0.0,1.0])  
muted | Boolean | Yes | Yes | No | Whether the audio is muted (default: false)  
streamType | String | Yes | No | No | Audio stream type: 'music' (speaker) or 'voicecall' (earpiece; not supported on watches/bands); default: 'music'  
meta | Object<{title: string, artist: string, album: string}> | No | Yes | No | Audio metadata including title, artist, and album  
  
#### Example:
```javascript
// let currentTime = audio.currentTime audio.currentTime = 5
```

## Events

Name | Description  
---|---  
play | Triggered after play() is called or when autoplay is true. Passive trigger examples: 1. Bluetooth headset control to play audio  
pause | Triggered after pause() is called. Passive trigger examples: 1. Audio focus lost (e.g., incoming call); 2. Bluetooth headset control to pause audio  
stop | Triggered after stop() is called. Passive trigger example: 1. Playing audio during a call  
loadeddata | Triggered when audio data is first loaded  
ended | Triggered when playback ends  
durationchange | Triggered when the duration changes  
error | Triggered when a playback error occurs  
  
#### Example:
```javascript
audio.onplay = function() { console.log(` audio starts to play `)} audio.onplay = null
```
