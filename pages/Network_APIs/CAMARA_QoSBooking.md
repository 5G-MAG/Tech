---
layout: default
title: CAMARA QoS Booking
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 5
has_children: false
---

<img src="../../assets/images/Banner_NetworkAPIs.png" /> 

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
