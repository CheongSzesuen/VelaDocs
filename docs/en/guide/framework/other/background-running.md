<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/other/background-running.html -->

# Background Running

To save system resources, applications usually stop running after switching to the background and restart when switching back to the foreground. However, some applications such as music and sports applications may need to continue running in the background. To meet such requirements, background running is supported. The working principle of the background running mode is as follows:

When an application switches to the background, the system checks whether the conditions for background running are met. If so, the application continues to run; otherwise, it stops. The conditions include:

  1. The background running interface is declared in `manifest.json`.
  2. At least one background running interface (declared in `manifest.json`) is currently running.

Practical suggestions:

  * Background running consumes a lot of system resources, so applications should use it cautiously based on their own needs. Applications that apply for background running will be reviewed during the launch review to determine whether their background running needs are reasonable.
  * Import the background running interface and perform background execution in `app.ux` instead of in pages to avoid the impact of page switching and destruction.

## Configuration Method

Declare the required background running interface in `manifest.json`. The background running interfaces include:

  1. Audio playback: `system.audio`
  2. Upload and download: `system.request`
  3. Geolocation: `system.geolocation`
```javascript
{ "package" : "com.hybrid.demo.sample" , // ...... "config" : { "logLevel" : "trace" , "background" : { "features" : [ "system.audio" , "system.request" ] } } // ...... }
```
