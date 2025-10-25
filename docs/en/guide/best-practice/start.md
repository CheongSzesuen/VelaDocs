<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/best-practice/start.html -->

# Startup Latency Optimization

## Avoid setTimeout Delay

When performing page redirects from the logo page, avoid adding setTimeout delays for the redirect unless absolutely necessary. If you need to wait for asynchronous results, such as determining the next page to redirect to after retrieving data from storage, it is recommended to encapsulate the asynchronous method as synchronous using await, and execute the redirect immediately after the results are returned. Taking storage as an example:
```js
// ❌ Not Recommended onInit () { this.checkifHome () setTimeout (() => { if (! this.ifHome) { router.push ({ uri : 'pages/home' }) } } , 1000) } checkifHome () { const that = this storage.get ({ key : 'ifHome' , success : function (data) { that.ifHome = data } , fail : function (data , code) { console.log (` handling fail, code = ${ code } `) } }) }
```

```js
// ✅ Recommended Approach 1 onInit () { storage.get ({ key : 'ifHome' , success : function (data) { if (! data) { router.push ({ uri : 'pages/home' }) } } , fail : function (data , code) { console.log (` handling fail, code = ${ code } `) } }) }
```

```js
// ✅ Recommended Approach 2 async onInit () { const ifHome = await checkifHome () if (! ifHome) { router.push ({ uri : 'pages/home' }) } } checkifHome () { return new Promise ((resolve , reject) => { storage.get ({ key : 'ifHome' , success : function (data) { resolve (data) } , fail : function (data , code) { console.log (` handling fail, code = ${ code } `) reject (code) } }) }) }
```

```js
// ✅ Recommended Approach 3 // You can encapsulate a unified promise.js for reuse with other asynchronous interfaces export function promisify (fn) { if (typeof fn !== 'function') { throw Error ('[promisify] the type of `fn` should be function') ; } return (opts = { }) => { let { success , fail , complete , ... args } = opts ; if (typeof success === 'function' || typeof fail === 'function' || typeof complete === 'function') { console.warn ('[promisify] [WARN] The `success`, `fail` and `complete` callback will be ignored') ; } return new Promise ((resolve , reject) => { try { fn ({ ... args , success : data => resolve (data) , fail : (data , code) => { let err = new Error (data) ; err.code = code ; reject (err) ; } }) ; } catch (error) { reject (error) } }) } } // Unified encapsulation of storage methods import storage from '@system.storage' ; import { promisify } from './promise' ; const _get = promisify (storage.get) ; const _set = promisify (storage.set) ; const _clear = promisify (storage.clear) ; const _delete = promisify (storage.delete) ; export default { getItem (key) { return _get ({ key }) ; } , setItem (key , value) { return _set ({ key , value }) ; } , deleteItem (key) { return _delete ({ key }) ; } , clear () { return _clear () ; } , } // logo.ux async onInit () { const ifHome = await storage.getItem ('ifHome') if (! ifHome) { router.push ({ uri : 'pages/home' }) } }
```

## Homepage Data Caching

If the homepage data needs to be displayed again upon second entry, consider adding caching when the application (or homepage) exits. The next time you enter, read the cache from the logo page and store the data globally. The homepage page can read it directly during onInit and simultaneously initiate an asynchronous request to update it;

## Avoid HTTP Requests on Logo Page

It is recommended not to introduce HTTP requests on the logo page; try to perform them on the homepage to prevent page redirects from being blocked in weak or no network conditions;

## UI First

For applications like music apps, it is suggested to have a default state of not playing upon entering the app. The UI can be displayed first, and if song information is successfully retrieved, it can be shown immediately without waiting for the audio resource to load completely;

## Use Static Data for Privacy Page Information

Use static data in the code for the privacy page instead of dynamic fetching. For long text that needs to be displayed, it can be viewed via QR code scanning. The QR code can directly link to a local H5 page and should not be fetched via an API;

## Minimize Console Logging

Minimize console logging, especially long logs, as they significantly impact performance. Avoid very long (>10 lines) console logs and minimize printing JSON objects. If logging is necessary during debugging, use console.debug and configure quickapp.config.js (as shown below) to filter out console.debug logs when building the release package;
```js
const TerserPlugin = require ("terser-webpack-plugin") const webpack = require ("webpack") module.exports = { postHook : (config) => { if (config.mode === "production") { config.optimization.minimize = true config.optimization.minimizer = [ new TerserPlugin ({ terserOptions : { compress : { pure_funcs : [ "console.debug" ] } } }) ] } } }
```

## Image Caching/Cropping

For large (>100kb) dynamic images, it is recommended to add a loading page during the first load, download and cache them locally, and then load them via internal://files/XXX.png for subsequent uses (Important: Generally, it is not recommended to introduce large online images unless necessary. The dimensions of introduced large images should not exceed the screen size, and the size should not exceed 200kb. Try to use local images instead of online images, or support resize cropping for online images).
```js
// login.ux export function downloadFile (url) { // Download image return new Promise ((resolve , reject) => { if (! url) { resolve ('') } request.download ({ url , success : function (ret) { const token = ret.token request.onDownloadComplete ({ token : token , success : function (ret) { console.info (` ### request.download ### ret ` , ret) resolve (ret.uri) } , fail : function (msg , code) { console.info (` ### request.onDownloadComplete ### ${ code } : ${ msg } `) resolve (null) } }) } }) }) } const formUrl = 'http://XXX.cdn.homeBg.png' downloadFile (formUrl) . then (url => { global.homeBgUrl = url ; // url => 'internal://files/homeBg.png' }) // home.ux < image class = "w-466 h-466" src = "{{bgImage}}" alt = "../../common/images/homeBg.png" > < / image > //.... computed : { bgImage () { const img = global.homeBgUrl || 'http://XXX.cdn.homeBg.png' return img } } //.... // logo page global.homeBgUrl = await storage.getItem ('homeBgUrl') // Clean up images promptly based on condition changes logoOut () { file.delete ({ uri : global.homeBgUrl , success : function (data) { console.info (` ###delFile sucess ${ data } `) resolve (true) } , fail : function (data , code) { resolve (false) console.log (` ###delFile fail, code = ${ code } `) } }) }
```

## Use diagnosis Method for Connection Status Before Communication in Communication Apps

When using interconnect for communication between the watch app and the phone app, abandon the previous polling method of calling getApkStatus and switch to the new API [diagnosis](</vela/quickapp/en/features/network/interconnect.html#connect-diagnosis-object>).
```js
data : { status : '' , connectNum : 3 , conn : null } , onInit () { this.conn = interconnect.instance () ; this.connectStatus () ; } ,
```

```js
// ❌ Not Recommended connectStatus () { let status = this.conn.getApkStatus () ; if (status === 'CONNECTED' || this.connectNum === 0) { this.status = status ; // do something } else if (this.connectNum > 0) { this.connectNum \-- ; setTimeout (() => { this.connectStatus () } , 500) } }
```

```js
// ✅ Recommended connectStatus () { this.conn.diagnosis ({ success : (data) => { console.log (` handling success, status= ${ data.status } `) // do something } , fail : (data , code) => { console.log (` handling fail, code = ${ code } `) // do something } }) }
```

## Use interconnect to Transfer Multiple Data Items

When transferring multiple data items from the watch app to the phone app, if the number of items is not large, it is recommended to send them all at once without adding delays.
```js
// ❌ Not Recommended sendMsg (list) { for (let x in list) { setTimeout (() => { this.conn.send ({ data : list [ x ] , success : () => { } , fail : (data : { data , code }) => { } }) } , x * 500) } }
```

```js
// ✅ Recommended sendMsg (list) { for (let x in list) { this.conn.send ({ data : list [ x ] , success : () => { } , fail : (data : { data , code }) => { } }) } }
```
