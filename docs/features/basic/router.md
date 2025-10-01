<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/basic/router.html -->

# 页面路由 router

## 接口声明

无需声明

## 导入模块
```javascript
import router from '@system.router' // 或 const router = require('@system.router')
```

## 接口定义

### router.push(OBJECT)

跳转到应用内的某个页面

#### 参数：

参数 | 类型 | 必填 | 说明  
---|:---:|---|---  
uri | String | 是 | 要跳转到的 uri，可以是下面的格式：  
1、包含 schema 的完整 uri；  
2、以‘/’开头的应用内页面的路径；例：/about  
3、以非‘/’开头的应用内页面的名称；例：About  
4、特殊的，如果 uri 的值是"/"，则跳转到 path 为"/"的页，没有则跳转到首页  
  
支持包含 schema 的完整 uri。对于带有 schema 的 uri，处理流程如下：  
如果 schema 是 hap （参见 [hap 链接](</vela/quickapp/zh/guide/framework/other/hap-schema.html>)），会跳转到 hap 链接所支持的类型  
params | Object | 否 | 跳转时需要传递的数据，参数可以在目标页面中通过`this.param1`的方式使用，param1 为 json 中的参数名，param1 对应的值会统一转换为 String 类型。使用`this.param1`变量时，需要在目标页面中在 `public`（应用外传参）或 `protected` (应用内传参)下定义 key 名相同的属性  
  
#### params参数：

参数 | 类型 | 必填 | 说明  
---|:---:|---|---  
___PARAM_LAUNCH_FLAG___ | String | 否 | JS 应用启动参数，目前仅支持"clearTask"，在启动目标页面时会清除除此页面外的其他页面。详见[页面启动模式](</vela/quickapp/zh/guide/framework/other/launch-mode.html>)  
  
#### 示例：

  * 应用内切换页面

    * path 切换
```javascript
router.push({ uri : '/about' , params : { testId : '1' } })
```

    * name 切换
```javascript
// open page by name router.push({ uri : 'About' , params : { testId : '1' } })
```

    * 切换页面并清除其他页面
```javascript
router.push({ uri : '/about' , params : { ___PARAM_LAUNCH_FLAG___ : 'clearTask' } })
```

### router.replace(OBJECT)

用应用内的某个页面替换当前页面，并销毁被替换的页面

#### 参数：

参数 | 类型 | 必填 | 说明  
---|:---:|---|---  
uri | String | 是 | 要跳转到的 uri，可以是下面的格式：

  1. 以"/"开头的应用内页面的路径；例：/about
  2. 以非"/"开头的应用内页面的名称；例：About
  3. 特殊的，如果 uri 的值是"/"，则跳转到 path 为"/"的页，没有则跳转到首页

  
params | Object | 否 | 跳转时需要传递的数据，参数可以在目标页面中通过`this.param1`的方式使用，param1 为 json 中的参数名，param1 对应的值会统一转换为 String 类型。使用`this.param1`变量时，需要在目标页面中在 `public`（应用外传参）或 `protected` (应用内传参)下定义 key 名相同的属性  
  
#### 示例：
```javascript
router.replace({ uri : '/test' , params : { testId : '1' } })
```

### router.back(OBJECT)

返回指定页面

#### 参数：

参数 | 类型 | 必填 | 说明  
---|:---:|---|---  
path | String | 否 | 返回目标页面的路径，可以是以下几种取值：

  1. 不传该参数，返回上一页面
  2. 以"/"开头的应用内已打开页面的路径；例：/about
  3. 特殊的，如果 path 的值是"/"，则跳转到页面名称为"/"的页，没有则跳转到首页

注意点：
  1. path 需要是以"/"开头的当前应用已经打开的页面路径，否则均视为无效参数，返回上一页面
  2. 若根据 path 未匹配到已经打开的页面，返回上一页面
  3. 若根据 path 参数匹配到多个页面，返回至最后打开的页面

  
  
#### 示例：
```javascript
// A页面, open page by name router.push({ uri : 'B' })// B页面, open page by name router.push({ uri : 'C' })// C页面, open page by name router.push({ uri : 'D' })// D页面, open page by name router.push({ uri : 'E' })// E页面不传入页面路径，返回至D页面 router.back() // D页面不传入页面名称，返回至C页面 router.back() // C页面传入页面路径，返回至A页面 router.back({ path : '/A' })
```

### router.clear()

清空所有历史页面记录，仅保留当前页面

#### 参数：

无

#### 示例：
```javascript
router.clear()
```

### router.getLength()

获取当前页面栈的页面数量

#### 返回值:

类型 | 说明  
---|---  
Number | 页面数量  
  
#### 示例：
```javascript
var length = router.getLength() console.log(` page's length = ${ length } `)
```

### router.getState()

获取当前页面状态

#### 返回参数：

参数名 | 类型 | 说明  
---|:---:|---  
index | Number | 当前页面在页面栈中的位置  
name | String | 当前页面的名称  
path | String | 当前页面的路径  
  
#### 示例：
```javascript
var page = router.getState() console.log(` page index = ${ page.index } `)console.log(` page name = ${ page.name } `)console.log(` page path = ${ page.path } `)
```

### router.getPages()

获取当前页面栈列表

#### 返回值：

类型 | 说明  
---|---  
Array | 页面栈列表。数组每一项都为 Object 类型  
  
数组每一项构成：

字段 | 类型 | 说明  
---|:---:|---  
name | String | 页面的名称  
path | String | 页面的路径  
  
#### 示例：
```javascript
var stacks = router.getPages() console.log('栈底页面名称为：' , stacks [ 0 ] . name)// 如 list、detail 等 console.log('栈底页面路径为：' , stacks [ 0 ] . path)// 如 /list、/detail、/home/preview
```
