<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/other/tips.html -->

# Precautions

## Abnormal Scenarios in Watch

  1. Network anomalies, prompt when there is no network.
  2. Data anomalies (failure to obtain data or backend interface returns an error) handling.
  3. JS code error handling.
  4. Prevent duplicate button clicks (especially for operations that send requests upon clicking).
  5. When the screen turns off and then back on, the onShow lifecycle function will be triggered again. If there is a fetch request in this lifecycle function, it will be initiated again when the screen lights up, so use it with caution.

## Code Specifications

  1. The code in the app.ux file must be written within `<script></script>` tags; otherwise, the code will not execute!
  2. In *.ux files, the `template` node can only have one root node.
  3. CSS properties related to angles must include units, such as `total-angle: 360deg`.
  4. In `list-item`, use conditional judgments like `if`/`else`/`show` with caution to ensure that the structure of all `list-item` elements remains consistent.
  5. For the `src` attribute of `image`, do not use variable concatenation (e.g., `src="/common/{{type}}"`), as the compiler will display warnings during code packaging. It is recommended to use variables directly, like `src="{{imgPath}}"`.

## Common Optimizations

  1. Reduce the number and concurrency of network requests.
  2. Consider implementing local caching for interfaces with low real-time data requirements (also consider data size for caching).
  3. Control the number of local files and avoid directly traversing files to obtain their sizes.
  4. Use low-resolution network images whenever possible.
  5. Use pagination for lists, with each page containing no more than 20 items for better performance.
  6. Do not store network-requested data directly in memory; only store the fields that are needed.
  7. Use third-party dependencies with caution and opt for lightweight ones.
  8. Consider placing common code globally to avoid multiple imports.
  9. Add a loading state to prevent multiple network requests from being initiated due to frequent button clicks.

## Selector Usage Recommendations

For details, see: [style documentation](</vela/quickapp/en/guide/framework/style/>)
