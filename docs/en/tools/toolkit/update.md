<!-- 源地址: https://iot.mi.com/vela/quickapp/en/tools/toolkit/update.html -->

# Upgrade Migration

Compared to **AIoT-toolkit1.0** , **AIoT-toolkit2.0** has significantly improved the compilation speed of the `Xiaomi Vela JS` project, while also bringing some **breaking changes**. When an old project uses **1.0** and is preparing to upgrade to **2.0** , please follow the **precautions** below to make minor modifications to the source code.

## Precautions

Developers upgrading from **AIoT-toolkit1.0** to **AIoT-toolkit2.0** should pay attention to the following:

Description | Solution  
---|---  
Some syntax corrections   
1\. No need to nest `{{}}` inside `{{}}`, change `onclick="{{fun({{x}}，{{y}})}}`"  to `onclick="fun(x, y)"`   
  
2\. Unsupported style selectors will report errors, such as pseudo-classes | Modify the source code  
Dynamic paths are not converted to full paths:   
**1.0 syntax** : ../../common   
**2.0 syntax** : /common/**** | Modify the source code  
  
There are also some special dynamic CSS values that need to use new syntax when upgrading from **AIoT-toolkit1.0** to **AIoT-toolkit2.0** :

  * transform
```js
this.divStyle = { transform : JSON.stringify ({ translateX : "10px" , translateY : "20px" , scaleX : 2 , scaleY : 0.5 , rotate : "10deg" , }) , } ;
```

  * background
```js
// Linear gradient this.divStyle = { background : JSON.stringify ({ values : [ { type : "linearGradient" , directions : [ "to" , "left" ] , values : [ "#FF0000 10px" , "#0000FF 100%" ] , } , ] , }) , } ; // Radial gradient this.divStyle = { background : JSON.stringify ({ values : [ { type : "radialGradient" , size : [ "farthest-corner" ] , directions : [ "center" ] , values : [ "#3f87a6" , "#ebf8e1" , "#f69d3c" ] , } ] , }) , } ;
```

  * filter
```js
this.divStyle = { filter : JSON.stringify ({ blur : "10px" , }) , } ;
```

  * url
```js
this.divStyle = { backgroundImage : "/common/logo.png" , } ;
```

Note

Please be sure to make the modifications according to the instructions in the precautions, otherwise, it will affect the normal operation and startup of the project after upgrading to **2.0**.
