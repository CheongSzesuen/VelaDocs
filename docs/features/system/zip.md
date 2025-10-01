<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/zip.html -->

# 解压缩 zip

## 接口声明
```json
{ "name" : "system.zip" }
```

## 导入模块
```javascript
import zip from '@system.zip' // 或 const zip = require('@system.zip')
```

## 接口定义

### zip.decompress(OBJECT)

解压文件

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
srcUri | String | 是 | 源文件的 uri，不能是 tmp 类型的 uri  
dstUri | String | 是 | 目标目录的 uri，不能是应用资源路径和 tmp 类型的 uri  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### success 返回值：

无

#### fail 返回值：

错误码 | 说明  
---|---  
202 | 参数错误  
300 | I/O 错误  
  
#### 示例：
```javascript
zip.decompress({ srcUri : 'internal://cache/test.zip' , dstUri : 'internal://files/unzip/' , success : function() { console.log(` handling success `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```
