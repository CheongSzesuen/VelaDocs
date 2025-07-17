<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/record.html -->

# # 录音 record

## # 接口声明

``` { "name": "system.record" } ```

## # 导入模块

``` import record from '@system.record' // 或 const record = require('@system.record') ```

## # 接口定义

### # record.start(OBJECT)

开始录音

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
duration | Number | 否 | 录音时长，单位为 ms。如果 duration 为有效值将在达到指定值时停止录音  
sampleRate | Number | 否 | 采样率。不同的音频格式所支持的采样率范围不同。默认设置为 8000，建议使用 8000/16000/32000/44100/48000  
numberOfChannels | Number | 否 | 录音通道数，有效值 1/2  
encodeBitRate | Number | 否 | 编码码率。编码码率的取值与采样率和音频格式有关  
format | String | 否 | 音频格式，有效值 pcm/opus/wav。缺省为 pcm  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### # success 返回值：

参数名 | 类型 | 说明  
---|---|---  
uri | String | 录音文件的存储路径，在应用的缓存目录中  
  
#### # fail 返回错误码：

错误码 | 说明  
---|---  
205 | 录音已在进行中  
202 | 参数错误  
  
#### # 示例：

``` record.start({ duration: 10000, sampleRate: 8000, numberOfChannels: 1, encodeBitRate: 128000, format: 'pcm', success: function(data) { console.log(`handling success: ${data.uri}`) }, fail: function(data, code) { console.log(`handling fail, code = ${code}, errorMsg=${data}`) }, complete: function () { console.log(`handling complete`) } }) ```

### # record.stop()

停止录音

#### # 参数：

无

#### # 示例：

``` record.stop() ```

← [ 屏幕亮度 brightness ](</vela/quickapp/zh/features/system/brightness.html>) [ 地理位置 geolocation ](</vela/quickapp/zh/features/system/geolocation.html>) → 

快速导航

接口声明

导入模块

接口定义

record.start(OBJECT)

record.stop()
