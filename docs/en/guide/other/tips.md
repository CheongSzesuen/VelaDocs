<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/other/tips.html -->

# Precautions

## Exception Scenarios in the Watch

  1. Network exceptions, prompt when there is no network
  2. Data exceptions (no data is obtained, or the backend interface returns an error)
  3. JS code error handling
  4. Prevent duplicate clicks on buttons (especially pay attention to operations that send requests after clicking)
  5. After the screen is turned off, the onShow lifecycle function will be triggered again when the screen is turned on again. If there is a fetch request in this lifecycle function, the request will be initiated again when the screen is turned on, so use it with caution.

## Code Specifications

  1. The code in the app.ux file must be written within `<script></script>`, otherwise the code will not execute!
  2. In *.ux files, the `template` node can only have one root node
  3. CSS properties related to angles must include units, such as `total-angle: 360deg`
  4. In `list-item`, use conditional judgments like `if`/`else`/`show` cautiously to ensure all `list-item` structures are consistent
  5. For the `src` attribute of `image`, do not use variable concatenation (e.g., `src="/common/{{type}}"`), otherwise the compiler will display a warning during packaging. It is recommended to use the variable directly, like `src="{{imgPath}}"`

## Common Optimizations

  1. Reduce the number of network requests and concurrency
  2. Consider local caching for interfaces with low real-time data requirements (also consider data size for caching)
  3. Control the number of local files and avoid directly traversing files to get all file sizes
  4. Use low-resolution network images whenever possible
  5. Use pagination for lists, with about 20 items per page being optimal
  6. Do not store network request data directly in memory; only store the fields that are needed
  7. Use third-party dependencies cautiously and prefer lightweight ones
  8. Consider placing common code in the global scope to avoid multiple imports
  9. Add a loading state to prevent multiple network requests from being initiated due to frequent button clicks

