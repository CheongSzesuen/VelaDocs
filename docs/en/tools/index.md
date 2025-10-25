<!-- 源地址: https://iot.mi.com/vela/quickapp/en/tools/ -->

# About AIoT-IDE

`AIoT-IDE` is the official integrated development environment for developing `Xiaomi Vela JS applications`. Built upon [Visual Studio Code (opens new window)](<https://code.visualstudio.com/>) (hereinafter referred to as VS Code), it inherits all the functionalities of VS Code, such as **code editing** , **plugin integration** , **theme customization** , and personalized settings. Additionally, `AIoT-IDE` introduces a series of enhanced features specifically tailored for the development of `Xiaomi Vela JS applications`, including but not limited to:

  * Intelligent code suggestions
  * Vela JS application debugging
  * Real-time compilation preview
  * Packaging and publishing of Vela JS applications
  * Real-device debugging of Vela JS applications

This chapter primarily introduces the core functionalities of `AIoT-IDE`. For download and installation instructions, please refer to the [Installation Environment](</vela/quickapp/en/guide/start/use-ide.html>) chapter.

## Project Structure

The enhanced features for application development are only available when `AIoT-IDE` opens a `Xiaomi Vela JS application`.

A basic `Xiaomi Vela JS application` consists of a configuration file `manifest.json` that describes project information, an `app.ux` file that contains the project's public resources, and UX files that describe different pages.
```bash
├── manifest.json ├── app.ux ├── pages │ ├── index | | └── index.ux │ └── detail | └── detail.ux ├── i18n | ├── defaults.json | ├── zh-CN.json | └── en-US.json └── common ├── style.css ├── utils.js └── logo.png
```

When `AIoT-IDE` opens a project, it checks whether there is a `manifest.json` file in the **root directory** or **src directory** of the current project. If found, it reads the **deviceTypeList** from `manifest.json` and determines the type of `Xiaomi Vela JS application` based on the content of the **deviceTypeList** field.
