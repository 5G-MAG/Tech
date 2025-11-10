---
layout: default
title: CAMARA QoS Booking and Assignment
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 6
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: QoS Booking and Assignment API

## Description

The “QoS Booking and Assignment” API enables application developers and service providers to reserve specific network conditions in advance for one or more devices. These conditions are based on a defined Quality of Service (QoS) profile, and also include parameters such as location, start time, and duration.
Once a booking is confirmed, devices can be assigned to it, allowing end users to experience predictable and consistent network performance for those assigned devices — without needing to understand the complexities of the underlying network (e.g., 4G/5G infrastructure).

Information: [https://camaraproject.org/qos-booking-and-assignment/](https://camaraproject.org/qos-booking-and-assignment/) and [https://github.com/camaraproject/QoSBooking](https://github.com/camaraproject/QoSBooking)

The API definitions can be obtained here: [https://github.com/camaraproject/QoSBooking/tree/main/code/API_definitions](https://github.com/camaraproject/QoSBooking/tree/main/code/API_definitions)

## Relation of APIs
### QoS Booking and Assignment - QoS Booking API
  * **POST /qos-bookings** with a request body containing `numDevices`, `qosProfile`, `startTime`, `duration`, `serviceArea`, it triggers a new booking in advance and assign this reserved booking profile to one or more devices when the devices are ready. The response includes a `bookingId`.
    * Dependency: Requires `qosProfile` which can be retrieved from a previous call to the [**QoS Profiles API**](./CAMARA_QoSProfiles.html).
  * **GET /qos-bookings/{bookingId}** - gets booking information for the given bookingId
  * **DELETE /qos-bookings/{bookingId}** - Cancel an existing booking and release resources related to that booking.

### QoS Booking and Assignment - Device Assignment API
  * **POST /qos-bookings/{bookingId}/devices/assign** with a request body containing `device` object, allows the end user to assign one or more devices to the existing QoS Booking.
  * **GET /qos-bookings/{bookingId}/devices** - allows the end user to retrieve the list of devices assigned to the existing QoS Booking.
  * **POST /qos-bookings/{bookingId}/devices/release** with a request body containing `device` object - Release one or more already assigned devices. This is a synchronous call.
  * **POST /qos-bookings/retrieve** with a request body containing `device` object - Querying for QoS Booking resource information details for a device. Returns the QoS booking information for a given device. A device may have multiple bookings (for several times and locations), thus the response is an array

---

## Workflow: Media application requesting a QoS Booking and assinging to a device

A user of a media application would like to request the assignment of a QoS Profile to a device for a given period of time and service area. The following steps are executed:

Figure TBD

### Step 0: Pre-conditions
* qosProfiles have already been defined and made available by the network operator. This is related to the [**QoS Profiles API**](./CAMARA_QosProfiles.html).

### Step 1: Create a QoS Booking for a given number of devices
* **POST /qos-bookings** passing the `numDevices`, `qosProfile`, `startTime`, `duration`, `serviceArea`.

### Step 2: Assing the QoS Booking to a specific Device
* **POST /qos-bookings/{bookingId}/devices/assign** passing the BookingId from the previous step and a `device` object to assign the QoS Booking to a specific device.

## 5G-MAG's Self-Assessment

The QoS Booking can be invoked before the actual usage of the network starts to ensure that the requested capabilities are "reserved" for the specific area, time window and a given number of devices.
Before or during the event a device will be assigned have access to the QoS booking.

Potential improvements:
- Unlike other similar APIs there is no information about the application server. It is unclear what would be the endpoint to which throughput, jitter, latency and other parameters would apply.
- The procedure is very similar to Dedicated Networks. There seems to be redundancy with QoS Booking
- The use of the same name "QoS Booking" is misleading with the other API called "QoS Booking"
---

## QoS Booking and Assignment API Usage

### Request booking of QoS
With **POST /qos-bookings**

```
{
  "numDevices": 15,
  "qosProfile": "QOS_MEDIA_BROADCAST",
  "startTime": "2025-10-27T15:00:00.000Z",
  "duration": 3600,
  "serviceArea": {
    "areaType": "CIRCLE",
    "center": {
      "latitude": 37.735851,
      "longitude": -127.10066
    },
    "radius": 100
  },
  "sink": "https://application-server.com/notifications",
  "sinkCredential": {
    "credentialType": "ACCESSTOKEN",
    "accessToken": "<access_token>",
    "accessTokenExpiresUtc": "2025-12-31T23:59:59Z",
    "accessTokenType": "bearer"
  }
}
```

Type of response: A **bookingId**

```
{
  "bookingId": "8e2f6f30-0a1c-4c6b-92e1-1bd05aef1c58",
  "totalDevices": 15,
  "remainingDevices": 15,
  "qosProfile": "QOS_MEDIA_BROADCAST",
  "startTime": "2025-10-27T15:00:00.000Z",
  "duration": 3600,
  "serviceArea": {
    "areaType": "CIRCLE",
    "center": {
      "latitude": 37.735851,
      "longitude": -127.10066
    },
    "radius": 100
  },
  "status": "SUCCESSFUL",
  "statusInfo": "BOOKING_ACCEPTED"
}
```

### Assign a device
With **POST /qos-bookings/{bookingId}/devices/assign**, and device parameters

```
{
  "devices": [
    {
      "phoneNumber": "+14145550101"
    },
    {
      "networkAccessIdentifier": "+123456789@domain.com"
    },
    {
      "ipv4Address": {
        "publicAddress": "203.0.113.0",
        "publicPort": 59765
      }
    },
    {
      "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
    }
  ],
  "sink": "https://application-server.com/notifications",
  "sinkCredential": {
    "credentialType": "ACCESSTOKEN",
    "accessToken": "<access_token>",
    "accessTokenExpiresUtc": "2025-12-31T23:59:59Z",
    "accessTokenType": "bearer"
  }
}
```
