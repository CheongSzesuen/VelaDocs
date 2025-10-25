<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/manifest.html -->

# Project Configuration

The `manifest.json` file contains application descriptions, interface declarations, and page routing information.

## manifest

Property | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
package | String |:---:| Yes | Application package name. **Ensure it is different from the native application's package name.** It is recommended to use the format com.company.module, e.g., com.example.demo.  
name | String |:---:| Yes | Application name. **Within 6 Chinese characters and consistent with the name saved in the app store.** Used to display the application name on desktop icons, pop-ups, etc.  
icon | String |:---:| Yes | Application icon. A 192x192 size is sufficient.  
versionName | String |:---:| No | Application version name, e.g., "1.0".  
versionCode | Integer |:---:| Yes | Application version number, incremented from `1`. **It is recommended to increment`versionCode` by 1 each time the package is re-uploaded.**  
minAPILevel | Integer | 1 | No | Minimum supported API standard version number. **Compatibility check to avoid running on low-version platforms and causing incompatibility.** If not filled, it will be treated as a beta version.  
features | Array |:---:| No | Interface list. Most interfaces need to be declared here; otherwise, they cannot be called. See the documentation for each interface for details.  
config | Object |:---:| Yes | System configuration information. See the description below.  
router | Object |:---:| Yes | Routing information. See the description below.  
display | Object |:---:| No | UI display-related configuration. See the description below.  
deviceTypeList | Array<String> | watch | No | Optional values: watch, tv, car, phone. Currently, only watch is supported.  
permissions | Array |:---:| No | Permission requests. Example: [{"name": "hapjs.permission.LOCATION"}]  
  
### config

Used to define system configurations and global data.

Property | Type | Default Value | Description  
---|:---:|---|---  
logLevel | String | log | Log printing level, divided into off, error, warn, info, log, debug.  
designWidth | Integer |:---:| Page design reference width. Scales element sizes based on the actual device width.  
background | Object |:---:| Background running configuration information. Use the features field to request interfaces that need to be used in the background (while still declaring them in the top-level features field). Requestable interfaces include:   
system.audio   
system.geolocation   
system.request, etc.   
See [Background Running](</vela/quickapp/en/guide/framework/other/background-running.html>) for detailed usage.  
  
### minAPILevel

The minimum supported API standard version number, indicating that the developer's rpk package can be compatible and run on devices that implement at least this version of the API standard. The default value is 1. When using features added in API standard version 1 or higher, ensure that minAPILevel is at least this version number to avoid errors when running on devices that implement lower API standard versions.

Example:
```json
{ "minAPILevel" : 1 }
```

### router

Used to define the composition of pages and related configuration information. If a page does not have routing information configured, it will be skipped during compilation and packaging.

Property | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
entry | String |:---:| Yes | Homepage name. When using the sub-package feature, it is recommended to define the homepage in the base package.  
pages | Object |:---:| Yes | Page configuration list. The key value is the page name (corresponding to the page directory name, e.g., Hello corresponds to the 'Hello' directory), and the value is the detailed page configuration page. See the description below.  
  
Example code:
```json
"router" : { "entry" : "Demo" , "pages" : { "Demo" : { "component" : "index" } } }
```

#### router.pages

Used to define routing information for a single page.

Property | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
component | String |:---:| Yes | The component name corresponding to the page, consistent with the ux file name, e.g., "hello" corresponds to "hello.ux".  
path | String | /<page-name> | No | Page path, e.g., "/user". If not filled, it defaults to /<page-name>.   
The path must be unique and cannot be the same as another page's path.   
The path of the following page will be set to "/Index" due to its absence:   
`"Index": {"component": "index"}`  
launchMode | String | standard | No | Declares the page's launch mode. Supports two page launch modes: "singleTask" and "standard".   
When set to "singleTask" mode, each time the target page is opened, the existing target page will be opened, and the onRefresh lifecycle function will be called, clearing other pages opened on this page. If this page has not been opened before, a new target page instance will be created.   
When set to "standard" mode, a new target page will be opened each time (multiple identical pages will exist when the target page address is opened multiple times).  
  
### Example Code
```json
{ "package" : "com.company.unit" , "name" : "appName" , "icon" : "/Common/icon.png" , "versionName" : "1.0" , "versionCode" : 1 , "minPlatformVersion" : 1000 , "features" : [ { "name" : "system.network" } ] , "router" : { "entry" : "Hello" , "pages" : { "Hello" : { "component" : "hello" , "path" : "/" } } } }
```

### display

Used to define UI display-related configurations.

If the following property values are defined under the display object, their scope of effect will be all pages of this JS application.

Property | Type | Default Value | Description  
---|:---:|---|---  
backgroundColor | String | #ffffff | Window background color.  
  
### Permission Descriptions

Permission Name | feature | api | Description | Permission Error Codes  
---|:---:|---|:---:|---  
hapjs.permission.LOCATION | system.geolocation | getLocation   
subscribe   
unsubscribe | Geolocation | 400: Permission denied   
402: Permission error (permission not declared)  
hapjs.permission.DEVICE_INFO | system.device | getSerial   
getDeviceId | Get device information | 400: Permission denied   
402: Permission error (permission not declared)
