<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/multi-screens/ -->

# Multi-screen Adaptation

## Why is Multi-screen Adaptation Necessary?

Xiaomi has a wide range of wearable devices (smart bands, smartwatches), with varying screen shapes, sizes, and resolutions. To ensure that the app displays correctly on different screens, multi-screen adaptation is required. It is recommended that developers consider multi-screen adaptation as much as possible during app development to enhance the app's versatility, ensuring it can be distributed to as many wearable devices as possible and helping developers quickly expand their user base. The following table provides detailed screen information for devices running Vela OS. Please refer to it.

Device Type | Device Model | Screen Shape | Screen Size | Resolution | PPI | Screen Width (DP) | Aspect Ratio
---|---|---|---|---|---|---|---
Smartwatch | Xiaomi Watch S1 Pro | Round | 1.47 inches | 480x480 | 326 | 240 | 1
Smartwatch | Xiaomi Watch H1 | Round | 1.43 inches | 466x466 | 326 | 233 | 1
Smartwatch | Xiaomi Watch S3 | Round | 1.43 inches | 466x466 | 326 | 233 | 1
Smartwatch | Xiaomi Watch S4 sport | Round | 1.43 inches | 466x466 | 326 | 233 | 1
Smartwatch | Xiaomi Watch S4 | Round | 1.43 inches | 466x466 | 326 | 233 | 1
Smartwatch | REDMI Watch 5 | Rectangular | 2.07 inches | 432x514 | 324 | 216 | 0.8
Smart Band | Xiaomi Smart Band 8 Pro | Rectangular | 1.74 inches | 336x480 | 336 | 168 | 0.7
Smart Band | Xiaomi Smart Band 9 | Capsule-shaped | 1.62 inches | 192x490 | 325 | 96 | 0.4
Smart Band | Xiaomi Smart Band 9 Pro | Rectangular | 1.74 inches | 336x480 | 336 | 168 | 0.7
Smart Band | Xiaomi Smart Band 10 | Capsule-shaped | 1.725 inches | 212x520 | 326 | 106 | 0.4 

## How to Perform Multi-screen Adaptation?

The prerequisite for multi-screen adaptation is that the app must undergo multi-screen design. The design drafts should include adaptation plans for different screens. For specific design methods, please refer to [Multi-screen Design](</vela/quickapp/en/guide/design/multi-screens.html>).

The framework provides a series of technical specifications to assist developers in completing multi-screen adaptation of their apps according to the design drafts. Please refer to [Multi-screen Specifications](</vela/quickapp/en/guide/multi-screens/specs.html>).

Our IDE also offers a multi-screen UI simulator to help developers quickly preview how the app will look on different screens, allowing for appropriate adjustments. Please refer to [Multi-screen UI Simulator](</vela/quickapp/en/tools/debug/multi-screens.html>).

We provide code examples for multi-screen adaptation of common page elements, as well as a full-site case for reference. [Code Examples](</vela/quickapp/en/guide/multi-screens/samples.html>).
