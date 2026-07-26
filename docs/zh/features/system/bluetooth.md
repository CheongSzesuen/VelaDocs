<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html -->
<!-- 最近更新日期: 2026-05-12 -->

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

类型 | 说明
---|---
Array<[ScanResult](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#ScanResult)> | 扫描结果上报数据。

#### ScanResult

扫描结果上报数据。

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
deviceId | String | 是 | 否 | 表示扫描到的设备地址，例如："XX:XX:XX:XX:XX:XX"。
rssi | Number | 是 | 否 | 表示扫描到的设备的 rssi 值。
data | ArrayBuffer | 是 | 否 | 表示扫描到的设备发送的广播包。
addressType | String | 是 | 否 | 表示设备地址类型，取值为：'PUBLIC' 、'RANDOM'、'ANONYMOUS' 、'UNKNOWN' 。

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

类型 | 说明
---|---
Number | 订阅 id

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

属性名 | 说明 | - | -
---|---|---|---
success | Function | 否 | client端发送指令成功后回调（非连接成功）。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 的回调参数：

无

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClientDevice.connect({
  success: function () {
    console.log(`send connect success`);
  },
  fail: function (data, code) {
    console.log(`connect fail, code = ${code}`);
  },
  complete: function () {
    console.log(`connect complete`);
  }
});
```

### GattClientDevice.disconnect(OBJECT)

client 端断开与远端蓝牙低功耗设备的连接。

#### OBJECT 对象的属性：

属性名 | 说明 | - | -
---|---|---|---
success | Function | 否 | client端发送指令成功后回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 的回调参数：

无

#### 示例：

```ts
gattClientDevice.disconnect({
  success: function () {
    console.log(`disconnect success`);
  },
  fail: function (data, code) {
    console.log(`disconnect fail, code = ${code}`);
  },
  complete: function () {
    console.log(`disconnect complete`);
  }
});
```

### GattClientDevice.close()

关闭客户端功能，注销 client 在协议栈的注册，调用该接口后 GattClientDevice 实例将不能再使用。

#### 返回值：

类型 | 说明
---|---
Boolean | 调用接口成功返回 true，失败返回 false。

```ts
let result = gattClientDevice.close();
console.log(`gattClientDevice close ${result}`);
```

### GattClientDevice.getServices(OBJECT)

client 端获取蓝牙低功耗设备的所有服务，即服务发现 。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 的回调参数：

类型 | 描述
---|---
Array<[GattService](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#GattService)> | 服务端的 service 数据。

#### 示例：

```ts
function outputServices(services) {
  console.log("bluetooth services size is ", services.length);
  for (let i = 0; i < services.length; i++) {
    console.log("bluetooth serviceUuid is " + services[i].serviceUuid);
  }
}

let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClientDevice.connect();
gattClientDevice.getServices({
  success: function (services) {
    outputServices(services);
  },
  fail: function (data, code) {
    console.log(`getServices fail, code = ${code}`);
  },
  complete: function () {
    console.log(`getServices complete`);
  },
});
```

### GattClientDevice.readCharacteristicValue(OBJECT)

client 端读取蓝牙低功耗设备特定服务的特征值。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
characteristic | [BLECharacteristic](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLECharacteristic) | 是 | 待读取的特征值。
success | Function | 否 | 服务端返回数据后，进行回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 的回调参数：

类型 | 说明
---|---
[BLECharacteristic](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLECharacteristic) | client 读取特征值，通过回调函数获取。

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let descriptors = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor = {
  serviceUuid: "00001810-0000-1000-8000-00805F9B34FB",
  characteristicUuid: "00001820-0000-1000-8000-00805F9B34FB",
  descriptorUuid: "00002903-0000-1000-8000-00805F9B34FB",
  descriptorValue: bufferDesc,
};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic = {
  serviceUuid: "00001810-0000-1000-8000-00805F9B34FB",
  characteristicUuid: "00001820-0000-1000-8000-00805F9B34FB",
  characteristicValue: bufferCCC,
  descriptors: descriptors,
};

gattClientDevice.readCharacteristicValue({
  characteristic,
  success: function (data) {
    console.log(`readCharacteristicValue uuid: ${data.characteristicUuid}`);
    if (data.characteristicValue) {
      let value = new Uint8Array(data.characteristicValue);
      console.log(`readCharacteristicValue value: ${value[0]}, ${value[1]}, ${value[2]}, ${value[3]}`);
    }
  },
  fail: function (data, code) {
    console.log(`readCharacteristicValue fail, code = ${code}`);
  },
  complete: function () {
    console.log(`readCharacteristicValue complete`);
  },
});
```

### GattClientDevice.readDescriptorValue(OBJECT)

client 端读取蓝牙低功耗设备特定的特征包含的描述符。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
descriptor | [BLEDescriptor](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLEDescriptor) | 是 | 待读取的描述符。
success | Function | 否 | 服务端返回数据后，进行回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 的回调参数：

类型 | 说明
---|---
[BLEDescriptor](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLEDescriptor) | 描述 descriptor 的接口参数定义 。

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor = {
  serviceUuid: "00001810-0000-1000-8000-00805F9B34FB",
  characteristicUuid: "00001820-0000-1000-8000-00805F9B34FB",
  descriptorUuid: "00002903-0000-1000-8000-00805F9B34FB",
  descriptorValue: bufferDesc,
};

gattClientDevice.readDescriptorValue({
  descriptor,
  success: function (data) {
    console.log("readDescriptorValue uuid: " + data.descriptorUuid);
    if (data.descriptorValue) {
      let value = new Uint8Array(data.descriptorValue);
      console.log(`readDescriptorValue value: ${value[0]}, ${value[1]}, ${value[2]}, ${value[3]}`);
    }
  },
  fail: function (data, code) {
    console.log(`readDescriptorValue fail, code = ${code}`);
  },
  complete: function () {
    console.log(`readDescriptorValue complete`);
  },
});
```

### GattClientDevice.writeCharacteristicValue(OBJECT)

client 端向低功耗蓝牙设备写入特定的特征值。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
characteristic | [BLECharacteristic](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLECharacteristic) | 是 | 蓝牙设备特征对应的二进制值及其它参数。
success | Function | 否 | client端发送指令成功后回调（非服务端成功）。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 的回调参数：

无

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let descriptors = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor = {
  serviceUuid: "00001810-0000-1000-8000-00805F9B34FB",
  characteristicUuid: "00001820-0000-1000-8000-00805F9B34FB",
  descriptorUuid: "00002903-0000-1000-8000-00805F9B34FB",
  descriptorValue: bufferDesc,
};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic = {
  serviceUuid: "00001810-0000-1000-8000-00805F9B34FB",
  characteristicUuid: "00001820-0000-1000-8000-00805F9B34FB",
  characteristicValue: bufferCCC,
  descriptors: descriptors,
};

gattClientDevice.writeCharacteristicValue({
  characteristic,
  success: function () {
    console.log(`writeCharacteristicValue success`);
  },
  fail: function (data, code) {
    console.log(`writeCharacteristicValue fail, code = ${code}`);
  },
  complete: function () {
    console.log(`writeCharacteristicValue complete`);
  }
});
```

### GattClientDevice.writeDescriptorValue(OBJECT)

client 端向低功耗蓝牙设备特定的描述符写入二进制数据。

#### OEJBCT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
descriptor | BLEDescriptor | 是 | 蓝牙设备描述符的二进制值及其它参数。
success | Function | 否 | client端发送指令成功后回调（非服务端成功）。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 的回调参数：

无

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 22;
let descriptor = {
  serviceUuid: "00001810-0000-1000-8000-00805F9B34FB",
  characteristicUuid: "00001820-0000-1000-8000-00805F9B34FB",
  descriptorUuid: "00002903-0000-1000-8000-00805F9B34FB",
  descriptorValue: bufferDesc,
};

gattClientDevice.writeDescriptorValue({
  descriptor,
  success: function () {
    console.log(`writeDescriptorValue success`);
  },
  fail: function (data, code) {
    console.log(`writeDescriptorValue fail, code = ${code}`);
  },
  complete: function () {
    console.log(`writeDescriptorValue complete`);
  }
});
```

### GattClientDevice.setBLEMtuSize(OBJECT)

client 协商远端蓝牙低功耗设备的最大传输单元（Maximum Transmission Unit, MTU）。注意：在调用 connect 接口连接成功后才能使用。

#### OEJECT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
mtu | Number | 是 | 设置范围为 22~512。
success | Function | 否 | client端发送指令成功后回调（非服务端成功）。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 的回调参数：

无

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClientDevice.setBLEMtuSize({
  mtu: 128,
  success: function () {
    console.log(`setBLEMtuSize success`);
  },
  fail: function (data, code) {
    console.log(`setBLEMtuSize fail, code = ${code}`);
  },
  complete: function () {
    console.log(`setBLEMtuSize complete`);
  }
});
```

### GattClientDevice.setNotifyCharacteristicChanged(OBJECT)

向服务端发送设置通知此特征值请求。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
characteristic | [BLECharacteristic](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLECharacteristic) | 是 | 蓝牙低功耗特征。
enable | Boolean | 是 | 启用接收 notify 设置为 true，否则设置为 false。
success | Function | 否 | client端发送指令成功后回调（非服务端成功）。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 的回调参数：

无

#### 示例：

```ts
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor = {
  serviceUuid: "00001810-0000-1000-8000-00805F9B34FB",
  characteristicUuid: "00001820-0000-1000-8000-00805F9B34FB",
  descriptorUuid: "00002902-0000-1000-8000-00805F9B34FB",
  descriptorValue: arrayBuffer,
};
descriptors[0] = descriptor;

let arrayBufferC = new ArrayBuffer(8);
let characteristic = {
  serviceUuid: "00001810-0000-1000-8000-00805F9B34FB",
  characteristicUuid: "00001820-0000-1000-8000-00805F9B34FB",
  characteristicValue: arrayBufferC,
  descriptors: descriptors,
};

let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClientDevice.setNotifyCharacteristicChanged({
  characteristic,
  enable: false,
  success: function () {
    console.log(`setNotifyCharacteristicChanged success`);
  },
  fail: function (data, code) {
    console.log(`setNotifyCharacteristicChanged fail, code = ${code}`);
  },
  complete: function () {
    console.log(`setNotifyCharacteristicChanged complete`);
  }
});
```

### GattClientDevice.onBLECharacteristicChange

订阅蓝牙低功耗设备的特征值变化事件。需要先调用 setNotifyCharacteristicChanged 接口才能接收 server 端的通知。

#### 事件回调参数：

类型 | 说明
---|---
[BLECharacteristic](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLECharacteristic) | 蓝牙低功耗设备的特征值。

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClientDevice.onBLECharacteristicChange = function (data) {
  console.log(`readCharacteristicValue uuid: ${data.characteristicUuid}`);
  if (data.characteristicValue) {
    let value = new Uint8Array(data.characteristicValue);
    console.log(`readCharacteristicValue value: ${value[0]}, ${value[1]}, ${value[2]}, ${value[3]}`);
  }
}
```

### GattClientDevice.onBLEConnectionStateChange

client 端订阅蓝牙低功耗设备的连接状态变化事件。

#### 事件回调参数：

类型 | 说明
---|---
[BLEConnectionState](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLEConnectionState) | 表示连接状态。

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClientDevice.onBLEConnectionStateChange = function (state) {
  console.log(`onBLEConnectionStateChange state = ${state}`);
};
```

### GattClientDevice.getDeviceName(OBJECT)

client 获取远端蓝牙低功耗设备名。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 回调对象参数的属性：

参数名 | 类型 | 说明
---|---|---
deviceName | String | client 获取对端 server 设备名，通过注册回调函数获取。

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClientDevice.getDeviceName({
  success: function (data) {
    console.log(`getDeviceName success, name = ${data.deviceName}`);
  },
  fail: function (data, code) {
    console.log(`getDeviceName fail, code = ${code}`);
  },
  complete: function () {
    console.log(`getDeviceName complete`);
  },
});
```

### GattClientDevice.getRssiValue(OBJECT)

client 获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用 connect 接口连接成功后才能使用。

#### OBJECT 对象的属性：

属性名 | 类型 | 必填 | 说明
---|---|---|---
success | Function | 否 | 成功回调。
fail | Function | 否 | 失败回调。
complete | Function | 否 | 执行结束后的回调。

#### success 回调对象参数的属性：

属性名 | 类型 | 说明
---|---|---
rssi | Number | 信号强度，单位 dBm，通过注册回调函数获取。

#### 示例：

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");

gattClientDevice.getRssiValue({
  success: function (data) {
    console.log(`getRssiValue success, rssi = ${data.rssi}`);
  },
  fail: function (data, code) {
    console.log(`getRssiValue fail, code = ${code}`);
  },
  complete: function () {
    console.log(`getRssiValue complete`);
  },
});
```

## GattService

描述 GattService 的对象属性定义。

属性名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
serviceUuid | String | 是 | 是 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。
isPrimary | Boolean | 是 | 是 | 如果是主服务设置为 true，否则设置为 false。
characteristics | Array<[BLECharacteristic](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLECharacteristic)> | 是 | 是 | 当前服务包含的特征列表。
includeServices | Array<[GattService](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#GattService)> | 是 | 是 | 当前服务依赖的其它服务。

## BLECharacteristic

描述 characteristic 的对象属性定义 。

属性名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
serviceUuid | String | 是 | 是 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。
characteristicUuid | String | 是 | 是 | 特定特征（characteristic）的 UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。
characteristicValue | ArrayBuffer | 是 | 是 | 特征对应的二进制值。
descriptors | Array<[BLEDescriptor](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#BLEDescriptor)> | 是 | 是 | 特定特征的描述符列表。
properties | [GattProperties](https://iot.mi.com/vela/quickapp/zh/features/system/bluetooth.html#GattProperties) | 是 | 是 | 特定特征的属性描述。

## BLEDescriptor

描述 descriptor 的对象属性定义 。

参数名 | 类型 | 可读 | 可写 | 描述
---|---|---|---|---
serviceUuid | String | 是 | 是 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。
characteristicUuid | String | 是 | 是 | 特定特征（characteristic）的 UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。
descriptorUuid | String | 是 | 是 | 描述符（descriptor）的 UUID，例如：00002902-0000-1000-8000-00805f9b34fb。
descriptorValue | ArrayBuffer | 是 | 是 | 描述符对应的二进制值。

## GattProperties

特定特征的属性描述定义。

属性名 | 类型 | 是否必填 | 描述
---|---|---|---
read | Boolean | 否 | 该特征值是否支持 read 操作。
write | Boolean | 否 | 该特征值是否支持 write 操作。true表示需要对端设备的回复。
writeNoResponse | Boolean | 否 | 该特征值是否支持 write 操作。true表示该特征支持写操作，无需对端设备回复。
notify | Boolean | 否 | 该特征值是否支持 notify 操作。true表示该特征可通知对端设备。
indicate | Boolean | 否 | 该特征值是否支持 indicate 操作。true表示该特征可通知对端设备，需要对端设备的回复。

## BLEConnectionState

BLE 的连接状态枚举。

名称 | 状态值 | 描述
---|---|---
STATE_DISCONNECTED | 0 | 表示 profile 已断连。
STATE_CONNECTING | 1 | 表示 profile 正在连接。
STATE_CONNECTED | 2 | 表示 profile 已连接。
STATE_DISCONNECTING | 3 | 表示 profile 正在断连。

## 状态码

错误码 | 描述
---|---
203 | 该功能不支持
205 | 重复提交，如：gattClient 连接成功后，再次连接
10001 | 当前系统蓝牙未打开
10008 | 蓝牙未知错误
10012 | 连接错误
10013 | 无内存或连接资源
10014 | 没有找到指定蓝牙设备

## 后台运行限制

禁止使用。

## 支持明细

设备产品 | 说明
---|---
小米 S1 Pro 运动健康手表 | 不支持
小米手环 8 Pro | 不支持
小米手环 9 / 9 Pro | 不支持
Xiaomi Watch S3 | 不支持
Redmi Watch 4 | 不支持
小米腕部心电血压记录仪 | 不支持
小米手环 10 | 不支持
Xiaomi Watch S4 | 不支持
REDMI Watch 5 | 不支持
REDMI Watch 6 | 不支持
Xiaomi Watch S5 | 支持
