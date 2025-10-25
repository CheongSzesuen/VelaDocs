<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/ -->

# Framework Introduction

This application framework is a set of tools for application development, primarily utilizing a front-end development technology stack. It adopts a popular front-end development model that aligns with the thinking habits of mainstream front-end developers. Additionally, it significantly enhances application performance, provides access to a range of system capabilities that are unavailable in front-end environments, and offers integration capabilities with numerous third-party services.

## File Structure

The application consists of a manifest.json file and multiple page ux files. The manifest.json file defines information such as application description, functional permission declarations, system configurations, and page routing. The page ux files implement the specifics of individual pages, including UI templates, stylesheets, data definitions, and callback event handling. For detailed usage, refer to [Project Structure](</vela/quickapp/en/guide/framework/project-structure.html>).

## Application Framework

### Routing Management

The framework manages the page routing of the entire application, enabling seamless transitions between pages and overseeing the complete lifecycle of each page. Developers are required to register pages in the manifest.json file and implement page transitions using the interface methods provided by the framework. For detailed usage, refer to [Project Configuration](</vela/quickapp/en/guide/framework/manifest.html>) and [Page Transition](</vela/quickapp/en/guide/framework/page-switch.html>).

### Data Binding

Data binding simplifies the synchronization between data and views. When data modifications occur, developers only need to update the data in the logic layer, and the view layer will automatically reflect these changes. For detailed usage of data binding, refer to [Template Syntax](</vela/quickapp/en/guide/framework/template/>).

### UI Components

The framework provides a set of basic UI components. In addition to supporting common HTML5 tags, such as `<div>` and `<input>`, the framework also offers component tags related to native UI, such as `<switch>`, `<slider>`, and `<list>`. For detailed usage, refer to [Components](</vela/quickapp/en/components/>).

### Native Interfaces

The framework also offers a rich set of native interfaces, encompassing both general system functionalities and integrations with third-party services, such as network requests and local storage. These APIs can significantly reduce the workload for developers and facilitate rapid application development. For detailed usage, refer to [Interfaces](</vela/quickapp/en/features/>).
