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

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.0 

#### ScanResult

Scanning result reporting data.

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.1 

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

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.2 

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

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.disconnect(OBJECT)

The client disconnects from a remote Bluetooth low-energy device.

#### Properties of the OBJECT Object:

| Property Name | Type | Description | | | | -------- | -------- | ---- | ---------------- | | success | Function | No | Callback after the client sends the command successfully. | | fail | Function | No | Failure callback. | | complete | Function | No | Callback after execution is complete. |

#### Parameters of the success Callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.close()

Closes the client function, deregisters the client from the protocol stack, and makes the GattClientDevice instance no longer usable after this interface is called.

#### Return Value:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.3

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.getServices(OBJECT)

The client obtains all services of a Bluetooth low-energy device, that is, service discovery.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.4 

#### Parameters of the success Callback:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.5 

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.readCharacteristicValue(OBJECT)

The client reads the characteristic value of a specific service of a Bluetooth low-energy device.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.6 

#### Parameters of the success Callback:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.7 

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.readDescriptorValue(OBJECT)

The client reads the descriptor contained in a specific characteristic of a Bluetooth low-energy device.

#### Properties of the OBJECT Object:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.8 

#### Parameters of the success Callback:

Property Name | Type | Required | Description
---|---|---|---
filters | Array<[ScanFilter](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanFilter)> | Yes | Address of the peer device, for example: "XX:XX:XX:XX:XX:XX".
options | [ScanOptions](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanOptions) | No | Indicates the scanning parameter configuration. Optional parameters.
success | Function | No | Success callback.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution is complete.9 

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.writeCharacteristicValue(OBJECT)

The client writes a specific characteristic value to a Bluetooth low-energy device.

#### Properties of the OBJECT Object:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.0 

#### Parameters of the success Callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.writeDescriptorValue(OBJECT)

The client writes binary data to a specific descriptor of a Bluetooth low-energy device.

#### Properties of the OEJBCT Object:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.1 

#### Parameters of the success Callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.setBLEMtuSize(OBJECT)

The client negotiates the Maximum Transmission Unit (MTU) of a remote Bluetooth low-energy device. Note: This interface can be used only after a successful connection is established by calling the connect interface.

#### Properties of the OEJECT Object:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.2 

#### Parameters of the success Callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.setNotifyCharacteristicChanged(OBJECT)

Sends a request to the server to set a notification for this characteristic value.

#### Properties of the OBJECT Object:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.3 

#### Parameters of the success Callback:

None

#### Example:

```javascript
import bluetoothBLE from '@system.bluetooth.ble'
or
const bluetoothBLE = require("@system.bluetooth.ble")
```

### GattClientDevice.onBLECharacteristicChange

Subscribes to the event of characteristic value changes of a Bluetooth low-energy device. You need to call the setNotifyCharacteristicChanged interface first to receive notifications from the server.

#### Parameters of the Event Callback:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.4 

#### Example:

```javascript
const scanner = bluetoothBLE.createScanner();
```

### GattClientDevice.onBLEConnectionStateChange

The client subscribes to the event of connection state changes of a Bluetooth low-energy device.

#### Parameters of the Event Callback:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.5 

#### Example:

```javascript
const scanner = bluetoothBLE.createScanner();
```

### GattClientDevice.getDeviceName(OBJECT)

The client obtains the name of a remote Bluetooth low-energy device.

#### Properties of the OBJECT Object:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.6 

#### Properties of the success Callback Object Parameter:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.7 

#### Example:

```javascript
const scanner = bluetoothBLE.createScanner();
```

### GattClientDevice.getRssiValue(OBJECT)

The client obtains the Received Signal Strength Indication (RSSI) of a remote Bluetooth low-energy device. This interface can be used only after a successful connection is established by calling the connect interface.

#### Properties of the OBJECT Object:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.8 

#### Properties of the success Callback Object Parameter:

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
deviceId | String | Yes | Yes | Indicates the BLE device address to be filtered, for example: "XX:XX:XX:XX:XX:XX".
name | String | Yes | Yes | Indicates the BLE device name to be filtered.
serviceUuid | String | Yes | Yes | Indicates the device with the service containing this UUID to be filtered, for example: 00001888-0000-1000-8000-00805f9b34fb.9 

#### Example:

```javascript
const scanner = bluetoothBLE.createScanner();
```

## GattService

Describes the object attribute definition of GattService.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.0 

## BLECharacteristic

Describes the object attribute definition of characteristic.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.1 

## BLEDescriptor

Describes the object attribute definition of descriptor.

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.2 

## GattProperties

Defines the property description of a specific characteristic.

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

## Support Details

Parameter Name | Type | Readable | Writable | Description
---|---|---|---|---
dutyMode | [ScanDuty](https://iot.mi.com/vela/quickapp/en/features/system/bluetooth.html#ScanDuty) | Yes | Yes | Indicates the scanning mode. The default value is SCAN_MODE_LOW_POWER.6
