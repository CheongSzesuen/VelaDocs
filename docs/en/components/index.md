<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/ -->

# Component

Components are divided into predefined components and custom components.

Predefined components are components that are predefined by the framework and whose rendering and logic are implemented by the framework. For example, when developing a page, developers must use components such as text and div, which are rendered by the platform's Native layer.

If developers are developing a complex page and write all UI parts in the `<template>` of a single file, the maintainability of the code will be very low, and unnecessary coupling relationships between modules may easily arise. To better organize logic and code, the page can be divided into multiple modules according to functionality, with each module responsible for a specific functional part. Finally, the page incorporates and manages these modules, passing business and configuration data to achieve code separation. This is the significance of custom components.

[Custom components](</vela/quickapp/en/guide/framework/template/component.html>) are components written by developers. They are used similarly to Native components and are ultimately rendered according to the component's `<template>`. At the same time, they are developed similarly to pages, with a ViewModel that manages data, events, and methods.

In this light, a page can also be seen as a special type of custom component that can be used without being imported and serves the entire page.

This chapter mainly provides a detailed introduction to the usage of predefined Native components, including their supported styles, properties, and events.
