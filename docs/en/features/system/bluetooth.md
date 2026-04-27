<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html -->

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

Creates a GattClientDevice (Generic Attribute Profile client) instance.

#### Parameters:

Parameter Name | Type | Required | Description
---|---|---|---
deviceId | String | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
addressType | String | No | Indicates the device address type. Optional values are: 'PUBLIC', 'RANDOM', 'ANONYMOUS', 'UNKNOWN'. Default value: UNKNOWN. 

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

#### Properties of the OBJECT:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion. 

#### ScanFilter

Scanning filter parameters.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb. 

#### ScanOptions

Scanning configuration parameters.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER. 

#### ScanDuty

Enumeration of scanning modes.

Name | Default Value | Description
---|---|---
SCAN_MODE_LOW_POWER | 0 | Indicates the low-power mode. Default value.
SCAN_MODE_BALANCED | 1 | Indicates the balanced mode.
SCAN_MODE_LOW_LATENCY | 2 | Indicates the low-latency mode. 

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

#### Properties of the OBJECT:

Property Name | Type | Required | Description
---|---|---|---
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion. 

#### Properties of the success callback object:

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

Subscribes to BLE device discovery reporting events.

#### Properties of the OBJECT:

Property Name | Type | Required | Description
---|---|---|---
callback | Function | No | Device discovery reporting callback.
fail | Function | No | Failure callback. 

#### Return Value:

Type | Description
---|---
Number | Subscription ID. 

#### Parameters of the callback:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.0 

#### ScanResult

Scanning result reporting data.

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.1 

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

Cancels the subscription to BLE device discovery reporting events.

#### Parameters:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.2 

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

The client initiates a connection to a remote Bluetooth Low Energy device.

#### Properties of the OBJECT:

| Property Name | Type | Description | | | | -------- | -------- | ---- | ---------------- | | success | Function | No | Callback upon successful instruction sending by the client (not upon successful connection). | | fail | Function | No | Failure callback. | | complete | Function | No | Callback after execution completion. |

#### Parameters of the success callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.disconnect(OBJECT)

The client disconnects from a remote Bluetooth Low Energy device.

#### Properties of the OBJECT:

| Property Name | Type | Description | | | | -------- | -------- | ---- | ---------------- | | success | Function | No | Callback upon successful instruction sending by the client. | | fail | Function | No | Failure callback. | | complete | Function | No | Callback after execution completion. |

#### Parameters of the success callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.close()

Closes the client function, deregisters the client from the protocol stack. After this interface is called, the GattClientDevice instance can no longer be used.

#### Return Value:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.3

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.getServices(OBJECT)

The client obtains all services of a Bluetooth Low Energy device, that is, service discovery.

#### Properties of the OBJECT:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.4 

#### Parameters of the success callback:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.5 

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.readCharacteristicValue(OBJECT)

The client reads the characteristic value of a specific service from a Bluetooth Low Energy device.

#### Properties of the OBJECT:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.6 

#### Parameters of the success callback:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.7 

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.readDescriptorValue(OBJECT)

The client reads the descriptor contained in a specific characteristic from a Bluetooth Low Energy device.

#### Properties of the OBJECT:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.8 

#### Parameters of the success callback:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Peer device address, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution completion.9 

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.writeCharacteristicValue(OBJECT)

The client writes a specific characteristic value to a Bluetooth Low Energy device.

#### Properties of the OBJECT:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.0 

#### Parameters of the success callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.writeDescriptorValue(OBJECT)

The client writes binary data to a specific descriptor of a Bluetooth Low Energy device.

#### Properties of the OEJBCT:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.1 

#### Parameters of the success callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.setBLEMtuSize(OBJECT)

The client negotiates the Maximum Transmission Unit (MTU) size with a remote Bluetooth Low Energy device. Note: This can only be used after a successful connection is established using the connect interface.

#### Properties of the OEJECT:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.2 

#### Parameters of the success callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.setNotifyCharacteristicChanged(OBJECT)

Sends a request to the server to set notifications for this characteristic value.

#### Properties of the OBJECT:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.3 

#### Parameters of the success callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.onBLECharacteristicChange

Subscribes to characteristic value change events of a Bluetooth Low Energy device. The setNotifyCharacteristicChanged interface must be called first to receive notifications from the server.

#### Event callback parameters:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.4 

#### Example:

```javascript
const scanner = bluetoothBLE.createScanner();
```

### GattClientDevice.onBLEConnectionStateChange

The client subscribes to connection state change events of a Bluetooth Low Energy device.

#### Event callback parameters:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.5 

#### Example:

```javascript
const scanner = bluetoothBLE.createScanner();
```

### GattClientDevice.getDeviceName(OBJECT)

The client obtains the name of a remote Bluetooth Low Energy device.

#### Properties of the OBJECT:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.6 

#### Properties of the success callback object parameters:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.7 

#### Example:

```javascript
const scanner = bluetoothBLE.createScanner();
```

### GattClientDevice.getRssiValue(OBJECT)

The client obtains the Received Signal Strength Indication (RSSI) of a remote Bluetooth Low Energy device. This can only be used after a successful connection is established using the connect interface.

#### Properties of the OBJECT:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.8 

#### Properties of the success callback object parameters:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the filtered BLE device address, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the filtered BLE device name.
serviceUuid | String | Yes | Yes | Indicates the filtered devices that contain the service with this UUID, for example: 00001888-0000-1000-8000-00805f9b34fb.9 

#### Example:

```javascript
const scanner = bluetoothBLE.createScanner();
```

## GattService

Describes the object attribute definitions of GattService.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.0 

## BLECharacteristic

Describes the object attribute definitions of characteristic.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.1 

## BLEDescriptor

Describes the object attribute definitions of descriptor.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.2 

## GattProperties

Property description definitions for specific characteristics.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.3 

## BLEConnectionState

Enumeration of BLE connection states.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.4 

## Status Codes

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.5 

## Background Running Restrictions

Prohibited.
