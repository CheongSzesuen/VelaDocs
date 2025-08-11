<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/data/storage.html -->

# 数据存储 storage

## 接口声明
```json
{ "name" : "system.storage" }
```

## 导入模块
```javascript
import storage from '@system.storage' // 或 const storage = require('@system.storage')
```

## 方法

### storage.get(OBJECT)

读取存储内容

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
key | String | 是 | 索引  
default | String | 否 | 如果 key 不存在，返回 default。如果 default 未指定，返回长度为 0 的空字符串  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### success 返回值：

key 对应的存储内容

#### 示例：
```javascript
storage.get({ key : 'A1' , success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### storage.set(OBJECT)

修改存储内容

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
key | String | 是 | 索引  
value | String | 否 | 新值。如果新值是长度为 0 的空字符串，会删除以 key 为索引的数据项  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### 示例：
```javascript
storage.set({ key : 'A1' , value : 'V1' , success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### storage.clear(OBJECT)

清空存储内容

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### 示例：
```javascript
storage.clear({ success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### storage.delete(OBJECT)

删除存储内容

#### 参数：

参数名 | 类型 | 必填 | 说明  
---|:---:|---|---  
key | String | 是 | 索引  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### 示例：
```javascript
storage.delete({ key : 'A1' , success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```
