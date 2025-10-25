<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/other/faq.html -->

# FAQ

## How to adapt to screens of different sizes?

The default screen resolution of the framework is 480 _480\. Vela third-party apps will automatically adapt, and developers can directly develop according to the size of the design draft. For example, if the design draft is 466_ 466, you can configure `designWidth: 466` in `manifest.json`, and then keep the size-related values in the CSS consistent with the design draft. For more detailed information, please refer to: [Page Styles and Layout](</vela/quickapp/en/guide/framework/style/page-style-and-layout.html>).

## How does the simulator communicate with the watch?

For the simulator to communicate with a mobile phone, an external Bluetooth adapter is required, and the configuration is relatively complex. It is recommended to use real device debugging.

## How to resolve the issue of incorrect signature prompts during communication?

Before the watch and mobile phone communicate, the application's signature is checked. If the signature is incorrect, communication will be rejected. Therefore, when debugging communication, the mobile phone app and the watch rpk need to be packaged using matching certificates. When encountering an incorrect signature error, please check whether the certificate used when exporting the rpk is the same as the certificate used when packaging the mobile phone app.

## How to troubleshoot issues related to communication (interconnect)?

First, check whether the data structure of the data sent from the watch side is correct (refer to sending data) and the execution status of the callback line number of the send method. Secondly, you can troubleshoot the logs printed on the mobile phone side (using the adb logcat tool) to see the data received by the mobile phone side.

## How to resolve the issue of flickering when updating list data?

For lists rendered through a for loop, if flickering occurs during data updates, you can add a tid to resolve the issue. For detailed documentation, please refer to: [Loop Directive](</vela/quickapp/en/guide/framework/template/for.html>).

## What are the requirements for the packaging certificate when building a release version of the rpk?

  1. If watch-to-mobile phone communication is involved, the certificate used when packaging the rpk must be consistent with the certificate used when packaging the mobile phone app; otherwise, communication will not be possible.
  2. If no communication is involved, there are no special requirements for the certificate. It can be generated according to the steps in the documentation.

> Note: Please keep the certificate secure and ensure that the same certificate is used each time to package the release version of the rpk. If the certificate changes, it may not be possible to list the app.

## How to resolve the issue of obtaining the connection status between the watch and the mobile phone?

Directly obtaining the status when entering the page often results in `DISCONNECTED`. Therefore, polling is required to obtain the status and determine the connection status between the watch and the mobile phone based on the return value of `getApkStatus()`.

## Which platforms does the simulator support?

The simulator supports three platforms: Windows, Mac, and Ubuntu. Windows supports Win10+, and Mac supports macOS12+.

## Can Windows and Mac package rpk?

Yes, Windows and Mac can package rpk.

## How to upload the rpk to the watch real device for running?

  1. Install the Mi Fitness app on your mobile phone (currently provided through business group对接. For Vela third-party app development needs, please contact Chang Jian via email: [changjian@xiaomi.com](<mailto:changjian@xiaomi.com>)).
  2. Click on [Mi Fitness] --> [Me] --> [About] --> [Debug].
  3. Click on [Third-Party Apps].
  4. Click on [Click to input package name].
  5. Enter any character (only need the detailed package name when uninstalling).
  6. Select [Install third app].
  7. Select the local rpk file for installation.
  8. A Toast prompt will appear upon successful installation.

## How to view logs on the watch real device?

  1. Install the Mi Fitness app on your mobile phone (currently provided through business group对接. For Vela third-party app development needs, please contact Chang Jian via email: [changjian@xiaomi.com](<mailto:changjian@xiaomi.com>)).
  2. Synchronize Mi Fitness with the watch.
  3. Reproduce the issue on the watch.
  4. Click on [Mi Fitness] --> [Me] --> [About] --> [Debug] --> [Pull firmware logs].
  5. After successful pulling, the logs are saved on the mobile phone. Log file directory: `/sdcard/Android/data/com.mi.health/files/log`.

