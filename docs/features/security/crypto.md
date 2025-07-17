<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/security/crypto.html -->

# # 密码算法 crypto

## # 接口声明

``` { "name": "system.crypto" } ```

## # 导入模块

``` import crypto from '@system.crypto' // 或 const crypto = require('@system.crypto') ```

## # 接口定义

### # crypto.hashDigest(OBJECT)

创建数据的哈希摘要

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
data | String/Uint8Array | 否 | 待计算内容，和uri二者必须有一个  
uri | String | 否 | 待计算文件地址，和data二者必须有一个  
algo | String | 否 | 算法 默认： SHA256   
可选：MD5， SHA1，SHA256，SHA512  
  
#### # 返回值：

类型 | 说明  
---|---  
String | 经过计算生成的摘要内容  
  
#### # 示例：

``` const digest = crypto.hashDigest({ data: 'hello', algo: 'MD5' }) ```

### # crypto.hmacDigest(OBJECT)

创建加密 HMAC 摘要

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
data | String | 是 | 待计算数据  
algo | String | 否 | 算法 默认： SHA256   
可选：MD5， SHA1，SHA256，SHA512  
key | String | 是 | 密钥  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 完成回调  
  
#### # success 返回值 Object：

参数值 | 类型 | 说明  
---|---|---  
data | String | 摘要  
  
#### # 示例：

``` crypto.hmacDigest({ data: 'hello', algo: 'SHA256', key: 'a secret', success: function(res) { console.log(`### crypto.hmacDigest success:`, res.data) }, fail: function(data, code) { console.log(`### crypto.hmacDigest fail ### ${code}: ${data}`) } }) ```

### # crypto.sign(OBJECT)

用于生成签名

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
data | String/Uint8Array | 否 | 被签名文本，和uri二者必须有一个  
uri | String | 否 | 被签名文件地址，和data二者必须有一个  
algo | String | 否 | 签名算法，默认：'RSA-SHA256'   
可选：RSA-MD5， RSA-SHA1，RSA-SHA256，RSA-SHA512  
privateKey | String | 是 | 私钥  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 完成回调  
  
#### # success 返回值 Object：

参数值 | 类型 | 说明  
---|---|---  
data | String/Uint8Array | 如果输入为字符串，则返回经过base64编码的字符串；否则返回Uint8Array；如果只传uri，默认返回string  
  
#### # 示例：

``` crypto.sign({ data: 'hello', algo: 'RSA-SHA256', privateKey: 'a secret', success: function(res) { console.log(`### crypto.sign success:`, res.data) }, fail: function(data, code) { console.log(`### crypto.sign fail ### ${code}: ${data}`) } }) ```

### # crypto.verify(OBJECT)

用于验证签名

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
data | String/Uint8Array | 否 | 被签名文本，和uri二者必须有一个  
uri | String | 否 | 被签名文件地址，和data二者必须有一个  
algo | String | 否 | 签名算法，默认：'RSA-SHA256'   
可选：RSA-MD5， RSA-SHA1，RSA-SHA256，RSA-SHA512  
signature | String/Uint8Array | 是 | 签名  
publicKey | String | 是 | 公钥  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 完成回调  
  
#### # success 返回值 Boolean：

类型 | 说明  
---|---  
Boolean | 校验结果，通过为true，不通过为false  
  
#### # 示例：

``` crypto.verify({ data: 'hello', algo: 'RSA-SHA256', publicKey: 'public key', signature: 'signature', success: function(data) { console.log(`### crypto.verify success:`, data) }, fail: function(data, code) { console.log(`### crypto.verify fail ### ${code}: ${data}`) } }) ```

### # crypto.encrypt(OBJECT)

加密

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
data | String/Uint8Array | 是 | 待加密数据  
algo | String | 否 | 加密算法 默认： RSA   
可选：RSA， AES  
key | String | 是 | 加密使用到的密钥，经过 base64 编码后生成的字符串  
options | Object | 否 | 加密参数  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 完成回调  
  
#### # RSA 参数options：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
transformation | String | 否 | RSA 算法的加密模式和填充项，默认为"RSA/None/PKCS1Padding"  
  
#### # AES 参数options：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
transformation | String | 否 | AES 算法的加密模式和填充项，默认为"AES/CBC/PKCS7Padding"  
iv | String | 否 | AES 加解密的初始向量，经过 base64 编码后的字符串，默认值为 key 值  
ivOffset | Number | 否 | AES 加解密的初始向量偏移，整数，默认值为 0  
ivLen | Number | 否 | AES 加解密的初始向量字节长度，整数，默认值为 16  
  
#### # success 返回值 Object：

参数值 | 类型 | 说明  
---|---|---  
data | String/Uint8Array | 如果输入为字符串，则返回经过base64编码的字符串；否则返回Uint8Array  
  
#### # 示例：

``` crypto.encrypt({ //待加密的文本内容 data: 'hello', //base64编码后的加密公钥 key: crypto.btoa('KEYKEYKEYKEYKEYK'), algo: 'AES', success: function(res) { console.log(`### crypto.encrypt success:`, res.data) }, fail: function(data, code) { console.log(`### crypto.encrypt fail ### ${code}: ${data}`) } }) ```

### # crypto.decrypt(OBJECT)

解密

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
data | String/Uint8Array | 是 | 待解密数据  
algo | String | 否 | 解密算法 默认： RSA   
可选：RSA， AES  
key | String | 是 | 加密或解密使用到的密钥，经过 base64 编码后生成的字符串  
options | Object | 否 | 解密参数  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 完成回调  
  
#### # RSA 参数options：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
transformation | String | 否 | RSA 算法的加密模式和填充项，默认为"RSA/None/PKCS1Padding"  
  
#### # AES 参数options：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
transformation | String | 否 | AES 算法的加密模式和填充项，默认为"AES/CBC/PKCS7Padding"  
iv | String | 否 | AES 加解密的初始向量，经过 base64 编码后的字符串，默认值为 key 值  
ivOffset | Number | 否 | AES 加解密的初始向量偏移，整数，默认值为 0  
ivLen | Number | 否 | AES 加解密的初始向量字节长度，整数，默认值为 16  
  
#### # success 返回值 Object：

参数值 | 类型 | 说明  
---|---|---  
data | String/Uint8Array | 如果输入为字符串，则返回经过base64编码的字符串；否则返回Uint8Array  
  
#### # 示例：

``` crypto.decrypt({ //待解密的内容 data: 'WB96uM08PfYIHu5G1p6YwA==', //base64编码后的加密公钥 key: crypto.btoa('KEYKEYKEYKEYKEYK'), algo: 'AES', success: function(res) { console.log(`### crypto.decrypt success:`, res.data) }, fail: function(data, code) { console.log(`### crypto.decrypt fail ### ${code}: ${data}`) } }) ```

### # crypto.btoa(STRING)

从String对象中创建一个 base-64 编码的 ASCII 字符串，其中字符串中的每个字符都被视为一个二进制数据字节

#### # 参数：

类型 | 必填 | 说明  
---|---|---  
String | 是 | 待编码文本  
  
#### # 返回值 String：

类型 | 说明  
---|---  
String | 经过编码之后的结果  
  
#### # 示例：

``` const encodeData = crypto.btoa('hello') ```

### # crypto.atob(STRING)

对经过 base-64 编码的字符串进行解码

#### # 参数：

类型 | 必填 | 说明  
---|---|---  
String | 是 | 待解码文本  
  
#### # 返回值 String：

类型 | 说明  
---|---  
String | 经过解码之后的结果  
  
#### # 示例：

``` const encodeString = crypto.btoa('hello') const res = crypto.atob(encodeString) ```

## # 支持明细

设备产品 | 说明  
---|---  
小米 S1 Pro 运动健康手表 | 不支持  
小米手环 8 Pro | 不支持  
Xiaomi Watch S3 | 支持  
Redmi Watch 4 | 不支持  
小米腕部心电血压记录仪 | 不支持  
Xiaomi Watch S4 | 支持  
REDMI Watch 5 | 支持  
  
← [ 电量信息 battery ](</vela/quickapp/zh/features/system/battery.html>) [ 音频 audio ](</vela/quickapp/zh/features/other/audio.html>) → 

快速导航

接口声明

导入模块

接口定义

crypto.hashDigest(OBJECT)

crypto.hmacDigest(OBJECT)

crypto.sign(OBJECT)

crypto.verify(OBJECT)

crypto.encrypt(OBJECT)

crypto.decrypt(OBJECT)

crypto.btoa(STRING)

crypto.atob(STRING)

支持明细
