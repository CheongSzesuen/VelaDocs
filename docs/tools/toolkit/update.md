<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/tools/toolkit/update.html -->

# # 升级迁移

相较于**AIoT-toolkit1.0** ，**AIoT-toolkit2.0** 对`Xiaomi Vela JS`项目编译的速度有了极大的提升，同时也带来一些**破坏性更新** 。在老项目使用了**1.0** 现准备向2.0**升级迁移** 时，请按下面的**注意事项** ，对源代码进行轻微修改。

## # 注意事项

开发者在从**AIoT-toolkit1.0** 升级到**AIoT-toolkit2.0** 有以下注意事项:

描述 | 解决办法  
---|---  
有些语法修正   
1\. `{{}}` 中无需再嵌套`{{}}`，onclick="`{{`fun(`{{`x`}}`，`{{`y`}}`)`}}`"改为 `onclick="fun(x, y)"`   
  
2.不支持的样式选择器报错，例如伪类 | 修改源代码  
动态路径没有转换为完整的路径：  
**1.0写法** ：../../common   
**2.0写法** ：/common/**** | 修改源代码  
  
还有一些特殊的动态css值，从**AIoT-toolkit1.0** 升级到**AIoT-toolkit2.0** ，也要使用新的写法:

  * transform

``` this.divStyle = { transform: JSON.stringify({ translateX: "10px", translateY: "20px", scaleX: 2, scaleY: 0.5, rotate: "10deg", }), }; ```

  * background

``` // 线性渐变 this.divStyle = { background: JSON.stringify({ values: [ { type: "linearGradient", directions: ["to", "left"], values: ["#FF0000 10px", "#0000FF 100%"], }, ], }), }; // 径向渐变 this.divStyle = { background: JSON.stringify({ values: [{ type: "radialGradient", size: ["farthest-corner"], directions: ["center"], values: ["#3f87a6", "#ebf8e1", "#f69d3c"], }], }), }; ```

  * filter

``` this.divStyle = { filter: JSON.stringify({ blur: "10px", }), }; ```

  * url

``` this.divStyle = { backgroundImage: "/common/logo.png", }; ```

注意

以上改动请务必按照注意事项中的说明进行修改，否则在升级到**2.0** 后将影响项目的正常运行和启动。

← [ AIoT-toolkit ](</vela/quickapp/zh/tools/toolkit/start.html>) [ 打包应用 ](</vela/quickapp/zh/tools/release/start.html>) → 

快速导航

注意事项
