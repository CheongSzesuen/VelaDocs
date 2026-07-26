<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html -->
<!-- 最近更新日期: 2026-05-12 -->

# Bluetooth bluetooth

## Interface Declaration

```json
{ "name": "system.bluetooth.ble" }
```

## Import Module

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

## Interface Definition

### bluetoothBLE.createScanner()

Initializes the Bluetooth module.

#### Parameters:

None

#### Return Value:

Scanner instance

#### Example:

```javascript
const scanner = bluetoothBLE.createScanner();
```

### bluetoothBLE.createGattClientDevice(deviceId, addressType)

Creates a GattClientDevice (Generic Attribute Profile Client) instance.

#### Parameters:

Parameter Name | Type | Required | Description
---|---|---|---
deviceId | String | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
addressType | String | No | Indicates the device address type. Optional values: 'PUBLIC', 'RANDOM', 'ANONYMOUS', 'UNKNOWN'. Default value: UNKNOWN.

#### Return Value:

GattClientDevice instance.

#### Example:

```javascript
const gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX", 'PUBLIC');
```

## Scanner

### Methods

### startBLEScan(OBJECT)

Initiates a BLE scanning process.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### ScanFilter

Scanning filter parameters.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.

#### ScanOptions

Scanning configuration parameters.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.

#### ScanDuty

Enumeration of scanning modes.

Name | Default Value | Description
---|---|---
SCAN_MODE_LOW_POWER | 0 | Indicates the low power consumption mode. This is the default value.
SCAN_MODE_BALANCED | 1 | Indicates the balanced mode.
SCAN_MODE_LOW_LATENCY | 2 | Indicates the low latency mode.

#### Example:

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

Stops the BLE scanning process.

#### Parameters:

None

#### Return Value:

None

#### Example:

```ts
scanner.stopBLEScan();
```

### Scanner.getScanState(OBJECT)

Obtains the current scanning state of the Scanner.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Properties of the success Callback Object:

Property Name | Type | Description
---|---|---
scanState | [ScanState](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanState) | Scanning state.

#### ScanState

Enumeration of BLE scanning states.

Name | Default Value | Description
---|---|---
STATE_NON_SCAN | 0 | Indicates that the local device has not started scanning for surrounding devices.
STATE_SCANING | 1 | Indicates that the local device is scanning for surrounding devices.

#### Example:

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

Subscribes to the BLE device discovery reporting event.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
callback | Function | No | Device discovery reporting callback.
fail | Function | No | Failure callback.

#### Return Value:

Type | Description
---|---
Number | Subscription ID.

#### Parameters of the callback Callback:

Type | Description
---|---
Array<[ScanResult](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanResult)> | Scanning result reporting data.

#### ScanResult

Scanning result reporting data.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | No | Indicates the address of the scanned device, for example: "XX:XX:XX:XX:XX:XX".
rssi | Number | Yes | No | Indicates the RSSI value of the scanned device.
data | ArrayBuffer | Yes | No | Indicates the broadcast packet sent by the scanned device.
addressType | String | Yes | No | Indicates the device address type. The values can be: 'PUBLIC', 'RANDOM', 'ANONYMOUS', 'UNKNOWN'.

#### Example:

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

Cancels the subscription to the BLE device discovery reporting event.

#### Parameters:

Type | Description
---|---
Number | Subscription ID

#### Return Value:

None

#### Example:

```ts
scanner.unsubscribeBLEDeviceFind(subscribeId);
```

### Scanner.close()

Closes the Scanner function. After this interface is called, the Scanner instance can no longer be used.

#### Parameters:

None

#### Return Value:

None

#### Example:

```ts
scanner.close();
```

## GattClientDevice

### Methods

### GattClientDevice.connect(OBJECT)

The client initiates a connection to a remote Bluetooth low-energy device.

#### Properties of the OBJECT Object:

| Property Name | Type | Description | | | | -------- | -------- | ---- | ---------------- | | success | Function | No | Callback after the client sends the command successfully (not indicating a successful connection). | | fail | Function | No | Failure callback. | | complete | Function | No | Callback after execution is complete. |

#### Parameters of the success Callback:

None

#### Example:

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

The client disconnects from a remote Bluetooth low-energy device.

#### Properties of the OBJECT Object:

| Property Name | Type | Description | | | | -------- | -------- | ---- | ---------------- | | success | Function | No | Callback after the client sends the command successfully. | | fail | Function | No | Failure callback. | | complete | Function | No | Callback after execution is complete. |

#### Parameters of the success Callback:

None

#### Example:

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

Closes the client function, deregisters the client from the protocol stack, and makes the GattClientDevice instance no longer usable after this interface is called.

#### Return Value:

Type | Description
---|---
Boolean | Returns true if the interface is called successfully, and false otherwise.

```ts
let result = gattClientDevice.close();
console.log(`gattClientDevice close ${result}`);
```

### GattClientDevice.getServices(OBJECT)

The client obtains all services of a Bluetooth low-energy device, that is, service discovery.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Parameters of the success Callback:

Type | Description
---|---
Array<[GattService](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#GattService)> | Service data of the server.

#### Example:

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

The client reads the characteristic value of a specific service of a Bluetooth low-energy device.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
characteristic | [BLECharacteristic](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLECharacteristic) | Yes | The characteristic value to be read.
success | Function | No | Callback after the server returns data.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Parameters of the success Callback:

Type | Description
---|---
[BLECharacteristic](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLECharacteristic) | The characteristic value read by the client and obtained through the callback function.

#### Example:

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

The client reads the descriptor contained in a specific characteristic of a Bluetooth low-energy device.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
descriptor | [BLEDescriptor](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLEDescriptor) | Yes | The descriptor to be read.
success | Function | No | Callback after the server returns data.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Parameters of the success Callback:

Type | Description
---|---
[BLEDescriptor](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLEDescriptor) | Interface parameter definition for describing the descriptor.

#### Example:

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

The client writes a specific characteristic value to a Bluetooth low-energy device.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
characteristic | [BLECharacteristic](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLECharacteristic) | Yes | The binary value of the Bluetooth device characteristic and other parameters.
success | Function | No | Callback after the client sends the command successfully (not indicating a successful server response).
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Parameters of the success Callback:

None

#### Example:

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

The client writes binary data to a specific descriptor of a Bluetooth low-energy device.

#### Properties of the OEJBCT Object:

Property Name | Type | Required | Description
---|---|---|---
descriptor | BLEDescriptor | Yes | The binary value of the Bluetooth device descriptor and other parameters.
success | Function | No | Callback after the client sends the command successfully (not indicating a successful server response).
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Parameters of the success Callback:

None

#### Example:

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

The client negotiates the Maximum Transmission Unit (MTU) of a remote Bluetooth low-energy device. Note: This interface can be used only after a successful connection is established by calling the connect interface.

#### Properties of the OEJECT Object:

Property Name | Type | Required | Description
---|---|---|---
mtu | Number | Yes | The setting range is 22–512.
success | Function | No | Callback after the client sends the command successfully (not indicating a successful server response).
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Parameters of the success Callback:

None

#### Example:

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

Sends a request to the server to set a notification for this characteristic value.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
characteristic | [BLECharacteristic](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLECharacteristic) | Yes | Bluetooth low-energy characteristic.
enable | Boolean | Yes | Set to true to enable receiving notifications, and false otherwise.
success | Function | No | Callback after the client sends the command successfully (not indicating a successful server response).
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Parameters of the success Callback:

None

#### Example:

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

Subscribes to the event of characteristic value changes of a Bluetooth low-energy device. You need to call the setNotifyCharacteristicChanged interface first to receive notifications from the server.

#### Parameters of the Event Callback:

Type | Description
---|---
[BLECharacteristic](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLECharacteristic) | Characteristic value of the Bluetooth low-energy device.

#### Example:

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

The client subscribes to the event of connection state changes of a Bluetooth low-energy device.

#### Parameters of the Event Callback:

Type | Description
---|---
[BLEConnectionState](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLEConnectionState) | Indicates the connection state.

#### Example:

```ts
let gattClientDevice = bluetoothBLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClientDevice.onBLEConnectionStateChange = function (state) {
  console.log(`onBLEConnectionStateChange state = ${state}`);
};
```

### GattClientDevice.getDeviceName(OBJECT)

The client obtains the name of a remote Bluetooth low-energy device.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Properties of the success Callback Object Parameter:

Parameter Name | Type | Description
---|---|---
deviceName | String | The client obtains the name of the peer server device through the registered callback function.

#### Example:

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

The client obtains the Received Signal Strength Indication (RSSI) of a remote Bluetooth low-energy device. This interface can be used only after a successful connection is established by calling the connect interface.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.

#### Properties of the success Callback Object Parameter:

Property Name | Type | Description
---|---|---
rssi | Number | Signal strength, in dBm, obtained through the registered callback function.

#### Example:

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

Describes the object attribute definition of GattService.

Property Name | Type | Readable | Writable | Description
---|---|---|---|---
serviceUuid | String | Yes | Yes | UUID of a specific service (service), for example: 00001888-0000-1000-8000-00805f9b34fb.
isPrimary | Boolean | Yes | Yes | Set to true if it is a primary service, and false otherwise.
characteristics | Array<[BLECharacteristic](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLECharacteristic)> | Yes | Yes | List of characteristics contained in the current service.
includeServices | Array<[GattService](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#GattService)> | Yes | Yes | Other services that the current service depends on.

## BLECharacteristic

Describes the object attribute definition of characteristic.

Property Name | Type | Readable | Writable | Description
---|---|---|---|---
serviceUuid | String | Yes | Yes | UUID of a specific service (service), for example: 00001888-0000-1000-8000-00805f9b34fb.
characteristicUuid | String | Yes | Yes | UUID of a specific characteristic (characteristic), for example: 00002a11-0000-1000-8000-00805f9b34fb.
characteristicValue | ArrayBuffer | Yes | Yes | Binary value corresponding to the characteristic.
descriptors | Array<[BLEDescriptor](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#BLEDescriptor)> | Yes | Yes | List of descriptors of the specific characteristic.
properties | [GattProperties](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#GattProperties) | Yes | Yes | Property description of the specific characteristic.

## BLEDescriptor

Describes the object attribute definition of descriptor.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
serviceUuid | String | Yes | Yes | UUID of a specific service (service), for example: 00001888-0000-1000-8000-00805f9b34fb.
characteristicUuid | String | Yes | Yes | UUID of a specific characteristic (characteristic), for example: 00002a11-0000-1000-8000-00805f9b34fb.
descriptorUuid | String | Yes | Yes | UUID of the descriptor (descriptor), for example: 00002902-0000-1000-8000-00805f9b34fb.
descriptorValue | ArrayBuffer | Yes | Yes | Binary value corresponding to the descriptor.

## GattProperties

Defines the property description of a specific characteristic.

Property Name | Type | Required | Description
---|---|---|---
read | Boolean | No | Indicates whether the characteristic value supports the read operation.
write | Boolean | No | Indicates whether the characteristic value supports the write operation. true indicates that a response from the peer device is required.
writeNoResponse | Boolean | No | Indicates whether the characteristic value supports the write operation. true indicates that the characteristic supports the write operation and no response from the peer device is required.
notify | Boolean | No | Indicates whether the characteristic value supports the notify operation. true indicates that the characteristic can notify the peer device.
indicate | Boolean | No | Indicates whether the characteristic value supports the indicate operation. true indicates that the characteristic can notify the peer device and requires a response from the peer device.

## BLEConnectionState

Enumeration of BLE connection states.

Name | State Value | Description
---|---|---
STATE_DISCONNECTED | 0 | Indicates that the profile is disconnected.
STATE_CONNECTING | 1 | Indicates that the profile is being connected.
STATE_CONNECTED | 2 | Indicates that the profile is connected.
STATE_DISCONNECTING | 3 | Indicates that the profile is being disconnected.

## Status Codes

Error Code | Description
---|---
203 | This function is not supported.
205 | Duplicate submission, for example: gattClient is connected successfully and then connected again.
10001 | The Bluetooth function of the current system is not turned on.
10008 | Unknown Bluetooth error.
10012 | Connection error.
10013 | No memory or connection resource.
10014 | The specified Bluetooth device is not found.

## Background Running Restrictions

Prohibited.

## Support Details

Device Product | Description
---|---
Xiaomi S1 Pro Sports and Health Watch | Not supported
Xiaomi Band 8 Pro | Not supported
Xiaomi Band 9 / 9 Pro | Not supported
Xiaomi Watch S3 | Not supported
Redmi Watch 4 | Not supported
Xiaomi Wrist ECG Blood Pressure Recorder | Not supported
Xiaomi Band 10 | Not supported
Xiaomi Watch S4 | Not supported
REDMI Watch 5 | Not supported
REDMI Watch 6 | Not supported
Xiaomi Watch S5 | Supported
