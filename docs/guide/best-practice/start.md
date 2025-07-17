<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/best-practice/start.html -->

# # 启动时延优化

## # 避免setTimeout延迟

logo页如非必要，在执行页面跳转时，不要增加setTimeout延迟跳转。如果是需要等待异步结果返回，例如获取storage后决定跳转的下一个页面，建议将异步方法封装成同步，使用await，等待结果返回后立即执行跳转。以storage为例：

``` // ❌不推荐写法 onInit(){ this.checkifHome() setTimeout(() => { if(!this.ifHome){ router.push({uri:'pages/home'}) } },1000) } checkifHome(){ const that = this storage.get({ key: 'ifHome', success: function(data) { that.ifHome = data }, fail: function(data, code) { console.log(`handling fail, code = ${code}`) } }) } ```

``` // ✅推荐写法一 onInit(){ storage.get({ key: 'ifHome', success: function(data) { if(!data){ router.push({uri:'pages/home'}) } }, fail: function(data, code) { console.log(`handling fail, code = ${code}`) } }) } ```

``` // ✅推荐写法二 async onInit(){ const ifHome = await checkifHome() if(!ifHome){ router.push({uri:'pages/home'}) } } checkifHome(){ return new Promise((resolve, reject) => { storage.get({ key: 'ifHome', success: function(data) { resolve(data) }, fail: function(data, code) { console.log(`handling fail, code = ${code}`) reject(code) } }) }) } ```

``` // ✅推荐写法三 //可统一封装promise.js,方便其他异步接口复用 export function promisify(fn) { if (typeof fn !== 'function') { throw Error('[promisify] the type of `fn` should be function'); } return (opts={}) => { let { success, fail, complete, ...args } = opts; if (typeof success === 'function' || typeof fail === 'function' || typeof complete === 'function') { console.warn('[promisify] [WARN] The `success`, `fail` and `complete` callback will be ignored'); } return new Promise((resolve, reject) => { try { fn({ ...args, success: data => resolve(data), fail: (data, code) => { let err = new Error(data); err.code = code; reject(err); } }); } catch (error) { reject(error) } }) } } //统一封装storage方法 import storage from '@system.storage'; import {promisify} from './promise'; const _get = promisify(storage.get); const _set = promisify(storage.set); const _clear = promisify(storage.clear); const _delete = promisify(storage.delete); export default { getItem(key) { return _get({key}); }, setItem(key, value) { return _set({key, value}); }, deleteItem(key) { return _delete({key}); }, clear() { return _clear(); }, } //logo.ux async onInit(){ const ifHome = await storage.getItem('ifHome') if(!ifHome){ router.push({uri:'pages/home'}) } } ```

## # 首页数据缓存

首页数据如果二次进入，需要再次展示的，可以考虑在应用（或首页）退出时增加上缓存，下次进入从logo页读取缓存后将数据存储在全局，首页page在onInit时直接读取，然后同时发起异步请求进行更新即可；

## # logo页避免http请求

建议不要在logo页引入http请求，尽可能放到首页执行，防止弱网或者无网情况阻塞页面跳转；

## # UI先行

如音乐类应用，进入应用建议默认状态为不播放，可以UI先行，如果歌曲信息获取成功立即展示，无需等到audio资源加载完成展示；

## # 隐私页信息使用静态数据

隐私页的数据代码里使用静态的数据，不用动态获取。需要展示长文本的，可以通过二维码扫码查看，二维码直接本地写死一个h5链接，不要通过接口去获取；

## # 减少从console打印

尽可能减少console打印，特别是长日志，很影响性能，避免很长的（>10行）console打印，尽可能减少json对象的打印，如果是debug期间需要打印日志，建议使用console.debug，并且配置quickapp.config.js（具体配置如下），在打release包的时候过滤掉console.debug的日志；

``` const TerserPlugin = require("terser-webpack-plugin") const webpack = require("webpack") module.exports = { postHook: (config) => { if (config.mode === "production") { config.optimization.minimize = true config.optimization.minimizer = [ new TerserPlugin({ terserOptions: { compress: { pure_funcs: ["console.debug"] } } }) ] } } } ```

## # 图片缓存/裁剪

如果有较大的（>100kb）动态图片，建议首次加载增加loading页，下载并缓存到本地，后续通过internal://files/XXX.png加载（重要：一般非必要不建议引入在线大图，引入的大图尺寸也不要超过屏幕尺寸，且大小不超过200kb，尽量使用本地图片代替在线图片，或者在线图片里支持resize-尺寸裁剪）

``` //login.ux export function downloadFile(url) {// 下载图片 return new Promise((resolve, reject) => { if(!url){ resolve('') } request.download({ url, success: function (ret) { const token = ret.token request.onDownloadComplete({ token: token, success: function (ret) { console.info(`### request.download ### ret`,ret) resolve(ret.uri) }, fail: function (msg, code) { console.info(`### request.onDownloadComplete ### ${code}: ${msg}`) resolve(null) } }) } }) }) } const formUrl = 'http://XXX.cdn.homeBg.png' downloadFile(formUrl).then(url => { global.homeBgUrl = url; //url => 'internal://files/homeBg.png' }) //home.ux <image class="w-466 h-466" src="{{bgImage}}" alt="../../common/images/homeBg.png"></image> //.... computed:{ bgImage() { const img = global.homeBgUrl || 'http://XXX.cdn.homeBg.png' return img } } //.... //logo页 global.homeBgUrl = await storage.getItem('homeBgUrl') //根据条件变化，及时进行图片清理 logoOut(){ file.delete({ uri:global.homeBgUrl, success: function(data) { console.info(`###delFile sucess ${data}`) resolve(true) }, fail: function(data, code) { resolve(false) console.log(`###delFile fail, code = ${code}`) } }) } ```

## # 通信类应用通信之前使用diagnosis方法判断连接状态

使用interconnect实现手表app和手机app的通信时，摒弃之前的轮询调用getApkStatus方法，改用新api [diagnosis](</vela/quickapp/zh/features/network/interconnect.html#connect-diagnosis-object>)

``` data: { status: '', connectNum: 3, conn: null }, onInit() { this.conn = interconnect.instance(); this.connectStatus(); }, ```

``` // ❌ 不推荐写法 connectStatus() { let status = this.conn.getApkStatus(); if (status === 'CONNECTED' || this.connectNum === 0){ this.status = status; // do something } else if (this.connectNum > 0) { this.connectNum --; setTimeout(() => { this.connectStatus() },500) } } ```

``` // ✅推荐写法 connectStatus() { this.conn.diagnosis({ success: (data) => { console.log(`handling success, status= ${data.status}`) // do something }, fail: (data,code) => { console.log(`handling fail, code = ${code}`) // do something } }) } ```

## # 使用interconnect传输多条数据

手表app向手机app传输多条数据时，若传输数量不大，建议直接一次性发送，无需增加延迟发送

``` // ❌不推荐写法 sendMsg(list) { for (let x in list) { setTimeout(() => { this.conn.send({ data: list[x], success: ()=>{ }, fail: (data: {data, code})=> { } }) },x*500) } } ```

``` // ✅推荐写法 sendMsg(list) { for (let x in list) { this.conn.send({ data: list[x], success: ()=>{ }, fail: (data: {data, code})=> { } }) } } ```

← [ 常用业务优化 ](</vela/quickapp/zh/guide/best-practice/business.html>) [ 验收标准 ](</vela/quickapp/zh/guide/publish/acceptance-criteria.html>) → 

快速导航

避免setTimeout延迟

首页数据缓存

logo页避免http请求

UI先行

隐私页信息使用静态数据

减少从console打印

图片缓存/裁剪

通信类应用通信之前使用diagnosis方法判断连接状态

使用interconnect传输多条数据
