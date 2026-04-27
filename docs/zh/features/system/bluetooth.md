<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html -->

# 蓝牙 bluetooth

## 接口声明

```json
{ "name": "system.bluetooth.ble" }
```

## 导入模块

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

## 接口定义

### bluetoothBLE.createScanner()

初始化蓝牙模块。

#### 参数：

无

#### 返回值：

Scanner 实例

#### 示例：

```javascript
const scanner = bluetoothBLE.createScanner();
```

### bluetoothBLE.createGattClientDevice(deviceId, addressType)

创建一个 GattClientDevice（通用属性协议客户端）实例。

#### 参数：

参数名 | 类型 | 必填 | 说明
---|---|---|---
deviceId | String | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
addressType | String | 否 | 表示设备地址类型，可选值为：'PUBLIC'、'RANDOM'、'ANONYMOUS' 、'UNKNOWN'，默认值：UNKNOWN。 

#### 返回值：

GattClientDevice 实例。

#### 示例：

```javascript
const gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX", 'PUBLIC');
```

## Scanner

### 方法

### startBLEScan(OBJECT)

发起 BLE 扫描流程。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。 

#### ScanFilter

扫描过滤参数。

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。 

#### ScanOptions

扫描的配置参数。

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanDuty) | 是 | 是 | 表示扫描模式，默认值为 SCAN_MODE_LOW_POWER。 

#### ScanDuty

枚举，扫描模式。

名称 | 默认值 | 说明
---|---|---
SCAN_MODE_LOW_POWER | 0 | 表示低功耗模式，默认值。
SCAN_MODE_BALANCED | 1 | 表示均衡模式。
SCAN_MODE_LOW_LATENCY | 2 | 表示低延迟模式。 

#### 示例：

```ts
let scanner = bluetoothBLE.createScanner();
scanner.startBLEScan({
  filters: [
    {
      deviceId: "XX:XX:XX:XX:XX:XX",
      name: "test",
      serviceUuid: "00001888-0000-1000-8000-00805f9b34fb",
    }
  ],
  options: {
    dutyMode: ScanDuty.SCAN_MODE_LOW_POWER,
  },
  success: function () {
    console.log(`startBLEScan success`);
  },
  fail: function (data, code) {
    console.log(`startBLEScan fail, code = ${code}`);
  },
  complete: function () {
    console.log(`startBLEScan complete`);
  },
});
```

### Scanner.stopBLEScan()

停止 BLE 扫描流程。

#### 参数：

无

#### 返回值：

无

#### 示例：

```ts
scanner.stopBLEScan();
```

### Scanner.getScanState(OBJECT)

获得当前Scanner的扫描状态。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 描述
---|---|---|---
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。 

#### success 回调对象的属性：

属性名 | 类型 | 说明
---|---|---
scanState | [ScanState](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanState) | 扫描状态。 

#### ScanState

枚举，BLE扫描状态。

名称 | 默认值 | 说明
---|---|---
STATE_NON_SCAN | 0 | 表示本地未开始扫描周围设备。
STATE_SCANING | 1 | 表示本地正在扫描周围设备。 

#### 示例：

```ts
scanner.getScanState({
  success: function (data) {
    console.log(`getScanState success, state = ${data.scanState}`);
  },
  fail: function (data, code) {
    console.log(`getScanState fail, code = ${code}`);
  },
  complete: function () {
    console.log(`getScanState complete`);
  },
});
```

### Scanner.subscribeBLEDeviceFind(OBJECT)

订阅 BLE 设备发现上报事件。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
callback | Function | 否 | 设备发现上报回调。
fail | Function | 否 | 失败回调。 

#### 返回值：

类型 | 说明
---|---
Number | 订阅 id。 

#### callback 回调参数：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。0 

#### ScanResult

扫描结果上报数据。

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。1 

#### 示例：

```ts
let scanner = bluetoothBLE.createScanner();
const subscribeId = scanner.subscribeBLEDeviceFind({
  callback(data) {
    for (let i = 0; i < data.length; i++) {
      console.info(`subscribeBLEDeviceFind deviceId = ${data[i].deviceId}, rssi = ${data[i].rssi}, addressType = ${data[i].addressType}`);
    }
  },
  fail(data, code) {
    console.log(`subscribeBLEDeviceFind fail, code = ${code}`);
  },
});
```

### Scanner.unsubscribeBLEDeviceFind(subscribeId)

取消订阅 BLE 设备发现上报事件。

#### 参数：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。2 

#### 返回值：

无

#### 示例：

```ts
scanner.unsubscribeBLEDeviceFind(subscribeId);
```

### Scanner.close()

关闭Scanner功能，调用该接口后Scanner实例将不能再使用。

#### 参数：

无

#### 返回值：

无

#### 示例：

```ts
scanner.close();
```

## GattClientDevice

### 方法

### GattClientDevice.connect(OBJECT)

client 端发起连接远端蓝牙低功耗设备。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。3 

#### success 的回调参数：

无

#### 示例：

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.disconnect(OBJECT)

client 端断开与远端蓝牙低功耗设备的连接。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。4 

#### success 的回调参数：

无

#### 示例：

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.close()

关闭客户端功能，注销 client 在协议栈的注册，调用该接口后 GattClientDevice 实例将不能再使用。

#### 返回值：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。5

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.getServices(OBJECT)

client 端获取蓝牙低功耗设备的所有服务，即服务发现 。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。6 

#### success 的回调参数：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。7 

#### 示例：

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.readCharacteristicValue(OBJECT)

client 端读取蓝牙低功耗设备特定服务的特征值。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。8 

#### success 的回调参数：

属性名 | 类型 | 必填 | 描述
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanFilter)> | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。
options | [ScanOptions](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanOptions) | 否 | 表示扫描的参数配置，可选参数。
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。9 

#### 示例：

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.readDescriptorValue(OBJECT)

client 端读取蓝牙低功耗设备特定的特征包含的描述符。

#### OBJECT 对象的属性：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。0 

#### success 的回调参数：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。1 

#### 示例：

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.writeCharacteristicValue(OBJECT)

client 端向低功耗蓝牙设备写入特定的特征值。

#### OBJECT 对象的属性：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。2 

#### success 的回调参数：

无

#### 示例：

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.writeDescriptorValue(OBJECT)

client 端向低功耗蓝牙设备特定的描述符写入二进制数据。

#### OEJBCT 对象的属性：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。3 

#### success 的回调参数：

无

#### 示例：

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.setBLEMtuSize(OBJECT)

client 协商远端蓝牙低功耗设备的最大传输单元（Maximum Transmission Unit, MTU）。注意：在调用 connect 接口连接成功后才能使用。

#### OEJECT 对象的属性：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。4 

#### success 的回调参数：

无

#### 示例：

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.setNotifyCharacteristicChanged(OBJECT)

向服务端发送设置通知此特征值请求。

#### OBJECT 对象的属性：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。5 

#### success 的回调参数：

无

#### 示例：

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
或
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.onBLECharacteristicChange

订阅蓝牙低功耗设备的特征值变化事件。需要先调用 setNotifyCharacteristicChanged 接口才能接收 server 端的通知。

#### 事件回调参数：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。6 

#### 示例：

```javascript
const scanner = bluetoothBLE.createScanner();
```

### GattClientDevice.onBLEConnectionStateChange

client 端订阅蓝牙低功耗设备的连接状态变化事件。

#### 事件回调参数：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。7 

#### 示例：

```javascript
const scanner = bluetoothBLE.createScanner();
```

### GattClientDevice.getDeviceName(OBJECT)

client 获取远端蓝牙低功耗设备名。

#### OBJECT 对象的属性：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。8 

#### success 回调对象参数的属性：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 是 | 表示过滤的 BLE 设备地址，例如："XX:XX:XX:XX:XX:XX"。
name | String | 是 | 是 | 表示过滤的 BLE 设备名。
serviceUuid | String | 是 | 是 | 表示过滤包含该 UUID 服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。9 

#### 示例：

```javascript
const scanner = bluetoothBLE.createScanner();
```

### GattClientDevice.getRssiValue(OBJECT)

client 获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用 connect 接口连接成功后才能使用。

#### OBJECT 对象的属性：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanDuty) | 是 | 是 | 表示扫描模式，默认值为 SCAN_MODE_LOW_POWER。0 

#### success 回调对象参数的属性：

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanDuty) | 是 | 是 | 表示扫描模式，默认值为 SCAN_MODE_LOW_POWER。1 

#### 示例：

```javascript
const scanner = bluetoothBLE.createScanner();
```

## GattService

描述 GattService 的对象属性定义。

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanDuty) | 是 | 是 | 表示扫描模式，默认值为 SCAN_MODE_LOW_POWER。2 

## BLECharacteristic

描述 characteristic 的对象属性定义 。

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanDuty) | 是 | 是 | 表示扫描模式，默认值为 SCAN_MODE_LOW_POWER。3 

## BLEDescriptor

描述 descriptor 的对象属性定义 。

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanDuty) | 是 | 是 | 表示扫描模式，默认值为 SCAN_MODE_LOW_POWER。4 

## GattProperties

特定特征的属性描述定义。

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanDuty) | 是 | 是 | 表示扫描模式，默认值为 SCAN_MODE_LOW_POWER。5 

## BLEConnectionState

BLE 的连接状态枚举。

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanDuty) | 是 | 是 | 表示扫描模式，默认值为 SCAN_MODE_LOW_POWER。6 

## 状态码

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanDuty) | 是 | 是 | 表示扫描模式，默认值为 SCAN_MODE_LOW_POWER。7 

## 后台运行限制

禁止使用。
