<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/record.html -->

# 录音 record

## 接口声明

```json
{ "name": "system.record" }
```

## 导入模块

```javascript
import record from '@system.record' 
// 或 
const record = require('@system.record')
```

## 接口定义

### record.start(OBJECT)

开始录音

#### 参数：

参数名 | 类型 | 必填 | 默认值 | 说明
---|---|---|---|---
duration | Number | 否 | 0 | 录音时长，单位为 ms。如果 duration 为有效值将在达到指定值时停止录音，默认为0开始录音不做定时终止，需要通过调用stop方法终止录音。若录音过程中被打断会立刻返回录音结果。
sampleRate | Number | 否 | 8000 | 采样率。不同的音频格式所支持的采样率范围不同。默认设置为 8000，建议使用 8000/16000/32000/44100/48000
numberOfChannels | Number | 否 | 1 | 录音通道数，有效值 1/2
encodeBitRate | Number | 否 | 128000 | 编码码率。编码码率的取值与采样率和音频格式有关，参考下表中比特率数值，输入错误的值会使用根据采样率及通道数计算出的比特率值。
frameSize | Number | 否 | - | PCM音频数据帧大小，单位 Byte。传入 frameSize 后，每录制指定帧大小的内容后，会通过 onframerecorded 回调录制的文件内容，不指定则不会回调。注意：回调帧数据大小不一定是设置的frameSize，有可能会调整为一个合适的值；设置此参数时，success回调将不返回uri；传入非法值（例如：小于等于零的数）时，success 回调的uri正常返回，onframerecorded事件将不会触发
format | String | 否 | pcm | 音频格式，有效值 pcm/opus/wav。缺省为 pcm
success | Function | 否 | - | 录音完成成功回调
fail | Function | 否 | - | 录音过程中失败回调
complete | Function | 否 | - | 录音结束后的回调 

#### PCM / WAV 比特率参考

对于pcm/wav录音场景，如果输入的是错误的比特率，编码器会根据采样率和通道数计算出比特率。

采样率 (Hz) | 声道数 | 比特率 (bp/s)
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

#### Opus 比特率参考

当使用opus格式录音时，下面表中的比特率范围对应着特定的采样率和声道数，这样的编码压缩比算法效率是最好的。当设置的比特率不在此范围时，也可以正常录音，但压缩比和算法效率不是最佳。

采样率 (Hz) | 声道数 | 比特率 (bp/s)
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

#### success 返回值：

参数名 | 类型 | 说明
---|---|---
uri | String | 录音文件的存储路径，在应用的缓存目录中 

#### fail 返回错误码：

错误码 | 说明
---|---
200 | 系统空间不足
205 | 录音已在进行中
202 | 参数错误 

#### 示例：

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

停止录音

#### 参数：

无

#### 示例：

```javascript
record.stop()
```

## 事件

### record.onframerecorded

监听已录制完指定帧大小的文件事件。如果设置了 frameSize，则会回调此事件。

#### 回调Object参数：

参数名 | 类型 | 说明
---|---|---
frameBuffer | Uint8Array | 录制的音频数据帧。通常音频数据帧大小为指定的 bufferSize，但是如果指定的 bufferSize 太小则会自动调整为一个合适的大小。
isLastFrame | boolean | 是否是最后一帧数据。 

#### 示例：

```javascript
record.onframerecorded = function (res) {
  // 获取音频数据：res.frameBuffer
  // 是否是最后一帧：res.isLastFrame
  console.log('==== onframerecorded', res)
}
```

注意：

  1. 当录音被打断时，结束当前录制并调用成功回调录制文件地址，调用完成回调结束前次录制；
  2. 当前frameSize大小受限于底层socket单次数据传输的大小，有效范围最大值为4096，设置大于此范围按最大值生效；
  3. 当正在进行录音过程中，有如下操作：SCO电话、Ring铃声、Alarm闹钟、Enforced求救音、Notify通知消息、开启另外一个录音，这些操作会抢夺音频焦点打断当前录音，使其状态变更为stop。被打断的录音会调用success并返回录制uri（文件录音）以及complete回调，流式录音onframerecorded会上报最后一帧完成录制。
  4. 目前产品上bes层针对采样率16000单声道的录制有增益处理，录制出的音频音量比其他配置音量大。

## 支持明细

设备产品 | 说明
---|---
小米 S1 Pro 运动健康手表 | 不支持
小米手环 8 Pro | 不支持
小米手环 9 / 9 Pro | 不支持
Xiaomi Watch S3 | 不支持
Redmi Watch 4 | 不支持
小米腕部心电血压记录仪 | 不支持
小米手环 10 | 不支持
Xiaomi Watch S4 | 不支持
REDMI Watch 5 | 不支持
REDMI Watch 6 | 不支持
Xiaomi Watch S5 | 支持
