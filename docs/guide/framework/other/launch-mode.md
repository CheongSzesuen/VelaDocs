<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/other/launch-mode.html -->

# # 页面启动模式

用于定义页面的启动行为。

## # 静态声明

在 manifest 文件中页面路由信息 router.page 可增加启动模式字段 launchMode，用于声明该页面的启动模式。

### # 页面启动模式参数：

属性 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
launchMode | String | standard | 否 | 声明页面的启动模式，支持"singleTask"，"standard"两种页面启动模式。  
标识为"singleTask"模式时每次打开目标页面都会打开已有的目标页面并回调 onRefresh 生命周期函数，清除该页面上打开的其他页面，没有打开过此页面时会创建新的目标页面实例。  
标识为"standard"模式时会每次打开新的目标页面（多次打开目标页面地址时会存在多个相同页面）  
  
### # 示例：

``` "router": { "entry": "PageA", "pages": { "PageA": { "launchMode": "singleTask", "component": "index" }, "PageB": { "launchMode": "standard", "component": "index" }, "PageC": { "launchMode": "singleTask", "component": "index" } } } ```

打开页面的行为逻辑：

若按顺序启动 PageA -> PageB -> PageC -> PageB -> PageC -> PageA

  * 打开 PageA，首次打开时页面栈为空 页面栈为PageA
  * 打开 PageB，PageB 的启动模式为 standard，即在 PageA 之上新建 PageB 的页面实例并显示 页面栈为PageA,PageB
  * 打开 PageC，首次打开 PageC，即在 PageB 之上新建 PageC 的页面实例并显示 页面栈为PageA,PageB,PageC
  * 打开 PageB，PageB 的启动模式为 standard，即在 PageC 之上新建 PageB 的页面实例并显示 页面栈为PageA,PageB,PageC,PageB
  * 打开 PageC，PageC 页面实例已存在，即销毁 PageC 之上的页面实例 PageB，回到之前打开的 PageC 的页面实例并回调此页面生命周期的 onRefresh 函数 页面栈为PageA,PageB,PageC
  * 打开 PageA，PageA 页面实例已存在，即销毁 PageA 之上的页面实例 PageB 和 PageC，回到之前打开的 PageA 的页面实例并回调此页面生命周期的 onRefresh 函数 页面栈为PageA

## # 动态声明

动态声明有两种方式。一种是在 router.push 中携带启动标识参数，另一种是在打开页面的链接中携带启动标识参数。启动标识参数可以控制页面打开行为。

### # 页面启动模式参数：

参数 | 类型 | 必填 | 说明  
---|---|---|---  
___PARAM_LAUNCH_FLAG___ | String | 否 | 跳转 JS 应用页面时传递的页面参数。携带 clearTask 时启动目标页面会清除此页面外的其他页面，存在多个目标页面时只保留最先打开的目标页面并回调 onRefresh 生命周期。如不存在目标页面时将清除所有页面并新建目标页面实例  
  
### # 示例：

``` router.push({ uri: '/PageB', params: { ___PARAM_LAUNCH_FLAG___: 'clearTask' } }) ```

打开页面的行为逻辑：

若已经打开页面栈为 PageA -> PageB -> PageC，此时以 clearTask 标识启动 PageB

  * 销毁 PageC 页面实例
  * 销毁 PageA 页面实例
  * PageB 页面实例已存在，回到此页面实例并回调此页面生命周期的 onRefresh 函数

若已经打开页面栈为 PageA -> PageC，此时以 clearTask 标识启动 PageB

  * 销毁 PageC 页面实例
  * 销毁 PageA 页面实例
  * PageB 页面实例不存在，新建 PageB 页面实例并显示

← [ hap 链接 ](</vela/quickapp/zh/guide/framework/other/hap-schema.html>) [ 适配规范 ](</vela/quickapp/zh/guide/multi-screens/specs.html>) → 

快速导航

静态声明

页面启动模式参数：

示例：

动态声明

页面启动模式参数：

示例：
