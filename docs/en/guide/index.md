<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/ -->

# Overview

The Xiaomi Vela JS application is a type of application developed by Xiaomi Inc., based on Xiaomi's IoT embedded software platform, Xiaomi Vela OS. This article will introduce the features, application scenarios, and development support of Xiaomi Vela JS applications, helping developers better understand and utilize this application type.

If you want to quickly learn how to develop Xiaomi Vela JS applications and get started promptly, please directly visit the [Quick Start](</vela/quickapp/en/guide/start.html>) section.

## Application Features

Xiaomi Vela JS applications are lightweight application models based on the Xiaomi Vela OS operating system, designed to provide a smoother and more convenient user experience for smart wearable devices. They possess the following notable features:

  * **Lightweight** : Xiaomi Vela JS applications adopt a lightweight architectural design. Compared to traditional applications, Xiaomi Vela JS applications have a smaller footprint, enabling them to load and run quickly, especially suitable for wearable devices with limited memory and processing capabilities.
  * **Cross-Platform Compatibility** : Xiaomi Vela JS applications support cross-device operation. Developers can develop once and run on multiple devices, significantly improving development efficiency and application popularity.
  * **High-Performance Rendering** : The system optimizes rendering capabilities, making application animations and interactions smoother and enhancing the user experience.
  * **Security Performance** : Xiaomi Vela OS ensures application security through a triple-isolation mechanism, protecting user data and device security.
  * **Development Support** : Xiaomi provides comprehensive development support. The development tools and documentation for Xiaomi Vela JS applications are complete, allowing developers to easily get started and quickly build high-quality applications. Xiaomi offers a range of development tools, including AIoT-IDE, supporting developers in developing and debugging Xiaomi Vela JS applications on operating systems such as Ubuntu, Windows, and MacOS.

## Application Scenarios

Xiaomi Vela JS applications have a wide range of application scenarios and have been implemented in multiple products, covering various usage scenarios on smart wearable devices:

  * **Health Monitoring** : Applications can monitor users' health data such as heart rate and sleep quality in real-time, providing health advice and early warnings.
  * **Sports Assistance** : During user exercise, applications can record exercise data, providing exercise guidance and health management.
  * **Message Reminders** : Applications can display message reminders from devices such as mobile phones, allowing users to view important information without taking out their phones.
  * **Mobile Payments** : Applications can integrate payment functions, enabling users to complete payment operations directly on wearable devices, enhancing payment convenience.
  * **Smart Control** : As a control center for smart homes, applications can remotely operate smart devices at home, such as lights and air conditioners.
  * **Daily Tools** : Provide daily tool functions such as weather forecasts, alarms, and timers to meet users' diverse needs.

## Technical Advantages

Compared to traditional application frameworks, Xiaomi Vela JS applications have the following technical advantages:

### Front-End Development Paradigm

Xiaomi Vela JS applications are developed using the JavaScript language and support the efficient front-end MVVM development paradigm and responsive UI framework, which are easy to learn and use. This allows developers to reduce the learning curve and shorten development cycles. This model aligns with the thinking habits of mainstream front-end developers, enabling them to quickly build feature-rich and interactive-friendly applications while reducing learning costs. Refer to [Development Syntax](</vela/quickapp/en/guide/framework/>).

### Unified APIs and Components

Xiaomi Vela JS applications provide unified [JS interfaces](</vela/quickapp/en/features/>) and [UI components](</vela/quickapp/en/components/>), allowing developers to not worry about differences in underlying hardware and operating systems, simplifying the development process while ensuring application quality and user experience.

### High-Performance Rendering

  * Through architectural optimization, complex calculations are offloaded to the native layer, addressing the performance bottlenecks of the JS language, thereby achieving native-like operational efficiency and a smooth experience.
  * Provides rich animation capabilities, including over 30 interpolation and physical animations, which can be used for transition and scene-changing effects, making the user interface more vivid, interesting, and expressive.
  * Fully leverages hardware performance, maximizing the use of GPU and CPU hardware acceleration capabilities to make complex UI interfaces and animations smoother, achieving a full 60 fps effect.

### Multi-Screen Adaptation

[Multi-screen adaptation](</vela/quickapp/en/guide/multi-screens/>) is another major feature of the Xiaomi Vela JS application framework, specifically manifested in:

  * **[Adaptation Specifications](</vela/quickapp/en/guide/multi-screens/specs.html>)** : The framework supports adaptive screens of different shapes, sizes, and resolutions, ensuring that applications provide a good visual experience on various devices.
  * **[Design Specifications](</vela/quickapp/en/guide/design/multi-screens.html>)** : Vela provides a set of technical specifications for multi-screen design, helping developers complete multi-screen adaptation of applications according to design drafts.
  * **[Multi-Screen UI Simulator](</vela/quickapp/en/guide/multi-screens/simulator.html>)** : AIoT-IDE provides a multi-screen UI simulator, allowing developers to quickly preview the effects of applications on different screens and make necessary adjustments.
  * **[Adaptation Cases](</vela/quickapp/en/guide/multi-screens/samples.html>)** : Provides code examples and whole-site cases for multi-screen adaptation of common page elements for developers to refer to and learn from.

## Application Development Process

### Environment Setup

Xiaomi provides a range of development tools, including AIoT-IDE, supporting developers in developing and debugging Xiaomi Vela JS applications on operating systems such as Ubuntu, Windows, and MacOS. AIoT-IDE is an integrated development environment for Xiaomi Vela JS applications, providing a series of functions such as project initialization, coding, and debugging. Please refer to [Install Environment](</vela/quickapp/en/guide/start/use-ide.html>) to initialize the project.

### Application Development

After initializing the project, please refer to [Project Structure](</vela/quickapp/en/guide/start/project-overview.html>) to understand the roles of various files and directories in the project. The project consists of configuration files (manifest.json), template code (ux files), style code (css files), logic code (js files), and resource files (images, audio, etc.). Please refer to [Project Configuration](</vela/quickapp/en/guide/framework/manifest.html>) to configure project-related information.

The application development paradigm follows a declarative UI, similar to traditional web development paradigms. Pages and components in the project are all written in files with the `ux` suffix, which are composed of three parts: [template](</vela/quickapp/en/guide/framework/template/>), [style](</vela/quickapp/en/guide/framework/style/>), and [script](</vela/quickapp/en/guide/framework/script/>). Developers can use [UI components](</vela/quickapp/en/components/>), [custom components](</vela/quickapp/en/guide/framework/template/component.html>), and styles to describe page structure and presentation effects by writing `ux` files, and use js scripts to define page data, implement lifecycle interfaces, general methods, event handling, etc. Please refer to [Writing Page UI](</vela/quickapp/en/guide/start/user-interface.html>) to learn more about page development.

### Running and Debugging

AIoT-IDE provides a built-in simulator that supports developers in launching the simulator to run and debug applications directly in the IDE, viewing the running effects in real-time. Please refer to [Running and Debugging](</vela/quickapp/en/guide/start/use-ide.html#_5-running-projects.html>) to learn how to run and debug applications.

### Packaging and Publishing

After completing the application development, developers can use the packaging function provided by AIoT-IDE to package the application into an installation package. Please refer to [Packaging Projects](</vela/quickapp/en/guide/start/use-ide.html#_7-packaging-projects.html>) to learn how to package applications. After successful project packaging, please refer to [Publishing](</vela/quickapp/en/guide/publish/>) to publish the application.
