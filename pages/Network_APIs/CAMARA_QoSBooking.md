---
layout: default
title: CAMARA QoS Booking
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 5
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: QoS Booking API

## Description

The “QoS Booking” (Quality of Service Booking) API provides a programmable interface for developers and other users (capabilities consumers) to request in advance certain network conditions to be provided by Telco networks, without the necessity to have an in-depth knowledge of the underlying network complexity (e.g. the 4G/5G system in case of a mobile network).

Information: [https://camaraproject.org/qos-booking/](https://camaraproject.org/qos-booking/) and [https://github.com/camaraproject/QoSBooking](https://github.com/camaraproject/QoSBooking)

The API definitions can be obtained here: [https://github.com/camaraproject/QoSBooking/tree/main/code/API_definitions](https://github.com/camaraproject/QoSBooking/tree/main/code/API_definitions)

## Relation of APIs
### QoS Booking API
  * **POST /device-qos-bookings** with a request body containing `qosProfile`, `applicationServer`, `applicationServerPorts`, `device` object, `devicePorts`, `startTime`, `duration`, `serviceArea`, it triggers a new booking to assign certain QoS Profile to certain devices. The response includes a `bookingId`.
    * Dependency: Requires `qosProfile` which can be retrieved from a previous call to the [**QoS Profiles API**](./CAMARA_QoSProfiles.html).
  * **GET /device-qos-bookings/{bookingId}** - Get QoS Booking information.
  * **DELETE /device-qos-bookings/{bookingId}** - Deletes a QoS Booking.
  * **POST /retrieve-device-qos-bookings** with a request body containing a `device` object, queries for QoS Booking resource information details for a device.

---

## Workflow: Media application requesting to assing a QoS Profile to a device

A user of a media application would like to request the assignment of a QoS Profile to a device for a given period of time and service area. The following steps are executed:

Figure TBD

### Step 0: Pre-conditions
* qosProfiles have already been defined and made available by the network operator. This is related to the [**QoS Profiles API**](./CAMARA_QosProfiles.html).

### Step 1: Create a QoS Booking for a device
* **POST /device-qos-bookings** passing the `qosProfile`, `applicationServer`, `applicationServerPorts`, `device` object, `devicePorts`, `startTime`, `duration`, `serviceArea`.

### Step 2: Use the QoS Booking
Use the QoS Booking for the device and the time window and service area. The device connected to the network at the time and service area will be able to benefit from the QoS Booking.

## 5G-MAG's Self-Assessment

The QoS Booking APIs can be invoked before the actual usage of the network starts to ensure that the requested capabilities are "reserved" for the specific area, time window and device.
During the event a device will have access to the QoS Booking.

This API may be suitable for a setup where a single device requires access to network resources (e.g. MoJo). However this is impractical for a Media Production setup with multiple devices as not all of them may be running at the same time. Making different QoS bookings for each of them while not requiring access to network resources concurrently may result in inneficiencies.

Potential improvements:
- It is unclear how to associate devices to make use of the resources. As it stands, the device is granted the booking as soon as connected to the network under the service area and for the specified duration.
- It is unclear how to update the booking. In the event that a device would need to be exchanged, deleting and creating a new booking may lead to loosing the ability to reserve resources during operation.

---

## QoS Booking API Usage

### Request booking of QoS for a device
With **POST /device-qos-bookings**, and device parameters

```
{
  "device": {
    "phoneNumber": "+123456789",
    "networkAccessIdentifier": "123456789@domain.com",
    "ipv4Address": {
      "publicAddress": "203.0.113.0",
      "publicPort": 59765
    },
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  },
  "qosProfile": "QCI_1_voice",
  "applicationServer": {
    "ipv4Address": "198.51.100.0/24",
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  },
  "devicePorts": {
    "ranges": [
      {
        "from": 5010,
        "to": 5020
      }
    ],
    "ports": [
      5060,
      5070
    ]
  },
  "applicationServerPorts": {
    "ranges": [
      {
        "from": 5010,
        "to": 5020
      }
    ],
    "ports": [
      5060,
      5070
    ]
  },
  "sink": "https://endpoint.example.com/sink",
  "sinkCredential": {},
  "startTime": "2024-06-01T12:00:00Z",
  "duration": 3600,
  "serviceArea": {}
}
```

Type of response: A **bookingId**

```
{
  "device": {
    "phoneNumber": "+123456789",
    "networkAccessIdentifier": "123456789@domain.com",
    "ipv4Address": {
      "publicAddress": "203.0.113.0",
      "publicPort": 59765
    },
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  },
  "qosProfile": "QCI_1_voice",
  "applicationServer": {
    "ipv4Address": "198.51.100.0/24",
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  },
  "devicePorts": {
    "ranges": [
      {
        "from": 5010,
        "to": 5020
      }
    ],
    "ports": [
      5060,
      5070
    ]
  },
  "applicationServerPorts": {
    "ranges": [
      {
        "from": 5010,
        "to": 5020
      }
    ],
    "ports": [
      5060,
      5070
    ]
  },
  "sink": "https://endpoint.example.com/sink",
  "sinkCredential": {},
  "startTime": "2024-06-01T12:00:00Z",
  "duration": 3600,
  "serviceArea": {},
  "bookingId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "startedAt": "2024-06-01T12:00:00Z",
  "status": "REQUESTED",
  "statusInfo": "DURATION_EXPIRED"
}
```

### Obtains the existing QoS booking for a device
With **POST /retrieve-device-qos-bookings**, and device parameters

```
{
  "device": {
    "phoneNumber": "+123456789",
    "networkAccessIdentifier": "123456789@domain.com",
    "ipv4Address": {
      "publicAddress": "203.0.113.0",
      "publicPort": 59765
    },
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  }
}
```

### Obtains the QoS booking information
With **GET /device-qos-bookings/{bookingId}**

```
{
  "bookingId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "duration": 3600,
  "device": {
    "ipv4Address": {
      "publicAddress": "203.0.113.0",
      "publicPort": 59765
    }
  },
  "qosProfile": "QOS_L",
  "sink": "https://application-server.com/notifications",
  "startTime": "2024-06-01T12:00:00Z",
  "startedAt": "2024-06-01T12:00:00Z",
  "status": "AVAILABLE",
  "serviceArea": {
    "areaType": "CIRCLE",
    "center": {
      "latitude": 50.735851,
      "longitude": 7.10066
    },
    "radius": 100
  }
}
```
