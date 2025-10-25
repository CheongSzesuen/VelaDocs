<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/multi-screens/ -->

# Multi-screen Adaptation

## Why is Multi-screen Adaptation Necessary?

Xiaomi offers a wide range of wearable devices (smart bands, smartwatches) with varying screen shapes, sizes, and resolutions. To ensure proper display of applications across different screens, multi-screen adaptation is required. Developers are advised to consider multi-screen adaptation as much as possible when developing applications to enhance their versatility. This ensures that applications can be distributed to as many wearable devices as possible, helping developers expand their user base quickly. The following table provides detailed screen information for devices equipped with Vela OS. Please refer to it.

Device Type | Device Model | Screen Shape | Screen Size | Resolution | PPI | Screen Width (DP) | Aspect Ratio  
---|:---:|---|:---:|---|:---:|---|---  
Smartwatch | Xiaomi Watch S1 Pro | Round | 1.47 inches | 480x480 | 326 | 240 | 1  
Smartwatch | Xiaomi Watch H1 | Round | 1.43 inches | 466x466 | 326 | 233 | 1  
Smartwatch | Xiaomi Watch S3 | Round | 1.43 inches | 466x466 | 326 | 233 | 1  
Smartwatch | Xiaomi Watch S4 sport | Round | 1.43 inches | 466x466 | 326 | 233 | 1  
Smartwatch | Xiaomi Watch S4 | Round | 1.43 inches | 466x466 | 326 | 233 | 1  
Smartwatch | REDMI Watch 5 | Rectangle | 2.07 inches | 432x514 | 324 | 216 | 0.8  
Smart Band | Xiaomi Smart Band 8 Pro | Rectangle | 1.74 inches | 336x480 | 336 | 168 | 0.7  
Smart Band | Xiaomi Smart Band 9 | Capsule-shaped-track-screen | 1.62 inches | 192x490 | 325 | 96 | 0.4  
Smart Band | Xiaomi Smart Band 9 Pro | Rectangle | 1.74 inches | 336x480 | 325 | 160 | 0.7  
  
## How to Perform Multi-screen Adaptation?

Multi-screen adaptation requires applications to be designed for multiple screens. The design drafts should include adaptation plans for different screens. For specific design methods, please refer to [Multi-screen Design](</vela/quickapp/en/guide/design/multi-screens.html>).

The framework provides a series of technical specifications to help developers complete multi-screen adaptation of applications according to the design drafts. Please refer to [Multi-screen Specifications](</vela/quickapp/en/guide/multi-screens/specs.html>).

Our IDE also offers a multi-screen UI simulator to help developers quickly preview the application's effects on different screens and make appropriate adjustments. Please refer to [Multi-screen UI Simulator](</vela/quickapp/en/tools/debug/multi-screens.html>).

We provide some code examples for multi-screen adaptation of common page elements, as well as whole-site cases for reference. [Code Examples](</vela/quickapp/en/guide/multi-screens/samples.html>).
