<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/other/audio.html -->

# 音频 audio

## 接口声明
```json
{ "name" : "system.audio" }
```

## 导入模块
```javascript
import audio from '@system.audio' // 或 const audio = require('@system.audio')
```

## 方法

### audio.play()

开始播放音频

#### 参数

无

#### 示例：
```javascript
audio.play()
```

### audio.pause()

暂停播放音频

#### 参数

无

#### 示例：
```javascript
audio.pause()
```

### audio.stop()

停止音频播放，可以通过 play 重新播放音频

#### 参数

无

#### 示例：
```javascript
audio.stop()
```

### audio.getPlayState(OBJECT)

获取当前播放状态数据

#### 参数

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### success 返回值：

参数值 | 类型 | 说明  
---|:---:|---  
state | String | 播放状态,分别为'play'，'pause'，'stop'  
src | String | 当前播放的音频媒体 uri，停止时返回空字符串  
currentTime | Number | 当前音频的当前进度，单位秒，停止时返回-1  
percent | Number | 当前播放进度百分比，范围0-100  
autoplay | Boolen | 当前音频是否在自动播放  
loop | Boolen | 当前音频是否在循环播放  
volume | Number | 当前音频的音量，默认当前系统媒体音量，音量变化范围[0.0,1.0]  
muted | Boolen | 当前音频是否在静音播放  
duration | Number | 音频的播放时长，单位秒，未知返回 NaN  
  
#### 示例：
```javascript
audio.getPlayState({ success : function(data){ console.log(` handling success: state: ${ data.state } ,src: ${ data.src } ,currentTime: ${ data.currentTime } ,autoplay: ${ data.autoplay } ,loop: ${ data.loop } ,volume: ${ data.volume } ,muted: ${ data.muted } ,notificationVisible: ${ data.notificationVisible } `)} , fail : function(data , code){ console.log('handling fail, code=' \+ code)} })
```

## 属性

名称 | 参数类型 | 是否可读 | 是否可写 | 必填 | 描述  
---|:---:|---|:---:|---|---  
src | String | 是 | 是 | 是 | 播放的音频媒体 uri  
currentTime | Number | 是 | 是 | 否 | 音频的当前进度，单位秒，对值设置可以调整播放进度  
duration | Number | 是 | 否 | 否 | 音频的播放时长，单位秒，未知返回 NaN  
autoplay | Boolean | 是 | 是 | 否 | 音频是否自动播放，默认 false  
loop | Boolean | 是 | 是 | 否 | 音频是否循环播放，默认 false  
volume | Number | 是 | 是 | 否 | 音频的音量，默认当前系统媒体音量，音量变化范围[0.0,1.0]  
muted | Boolean | 是 | 是 | 否 | 音频是否静音，默认 false  
streamType | String | 是 | 否 | 否 | 使用音频的类型，可能的值有 music、voicecall，值为 music 时使用扬声器播放，voicecall 时使用听筒播放（手表、手环设备不支持此配置），默认为 music  
meta | Object<{title: string, artist: string, album: string}> | 否 | 是 | 否 | 音频元数据信息，包括歌名、歌手、专辑名  
  
#### 示例：
```javascript
// let currentTime = audio.currentTime audio.currentTime = 5
```

## 事件

名称 | 描述  
---|---  
play | 在调用 play 方法后或者 autoplay 为 true 时的回调事件。被动触发场景举例：1. 蓝牙耳机控制播放音频  
pause | 在调用 pause 方法后的回调事件。被动触发场景举例：1. 音频焦点被抢占，例如：播放音频时收到来电；2. 蓝牙耳机控制暂停音频  
stop | 在调用 stop 方法后的回调事件。被动触发场景举例：1. 正在打电话时播放音频  
loadeddata | 第一次获取到音频数据的回调事件  
ended | 播放结束时的回调事件  
durationchange | 播放时长变化时的回调事件  
error | 播放发生错误时的回调事件  
  
#### 示例：
```javascript
audio.onplay = function() { console.log(` audio starts to play `)} audio.onplay = null
```
