<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/other/hap-schema.html -->

# hap link

An hap link refers to a URI starting with `hap://` supported in the router module. For usage scenarios, refer to [Page Routing](</vela/quickapp/en/features/basic/router.html>).

Currently, supported hap links start with `hap://app/` and support opening specified JS applications. The format is as follows:

`hap://app/<package>/[path][?key=value]`

Parameter description:

  * package: The application package name (required)
  * path: The path to the page within the application (optional, defaults to the homepage)
  * key-value: Parameters to be passed to the page (optional, multiple parameters can be included)

