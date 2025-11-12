---
layout: default
title: CAMARA Network Slice Booking
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 4
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: Network Slice Booking API

## Description

The “Network Slice Booking” API provides developers with a programmable interface. Industry customers can reserve and manage network slice resources within designated areas and time periods, and offer network guarantee services to end users. Within this API, developers can customize service areas (e.g., circular or polygonal regions), time periods, set Quality of Service (QoS) parameters (e.g., throughput, latency, and terminal limits), apply for network slice resources from operators, and bind slice resources for end users at the same time to achieve network guarantee functions.

Information: [https://camaraproject.org/network-slice-booking/](https://camaraproject.org/network-slice-booking/) and [https://github.com/camaraproject/NetworkSliceBooking](https://github.com/camaraproject/NetworkSliceBooking)

The API definitions can be obtained here: [https://github.com/camaraproject/NetworkSliceBooking/blob/main/code/API_definitions](https://github.com/camaraproject/NetworkSliceBooking/blob/main/code/API_definitions)

## Relation of APIs

### Network Slice Booking API 
  * **POST /sessions** with a request body including `serviceTime`, `serviceArea`, `sliceQoSProfiles`, it is used to create a new session (network slice) with the expected service time, service area, and QoS profile. The reponse contains a `sessionId`. If expected network slice resources are not available, the API consumer will receive an error response `422 - NETWORK_SLICE_BOOKING.RESOURCES_NOT_APPLICABLE`
  * **GET /sessions/{sessionId}** - query session resource information details.
  * **DELETE /sessions/{sessionId}** - delete a Network Slice Booking session.

#### Parameters describing a Network Slice QoS Profile
* `maxNumOfDevices`- is the maximum number of devices that can be connected to the slice
* `downStreamRatePerDevice` - is the maximum downstream rate allowed for each device connected to the slice. It indicates the individual device capability required for the slice.
* `upStreamRatePerDevice` - is the maximum upstream rate allowed for each device connected to the slice. It indicates the individual device capability required for the slice.
* `downStreamDelayBudget` - is the maximum allowable downlink packet transmission latency (millisecond). By limiting the delay, the network can provide an acceptable level of performance for various services, such as voice calls, video streaming, and data.
* `upStreamDelayBudget`  - is the maximum allowable uplink packet transmission latency (millisecond). By limiting the delay, the network can provide an acceptable level of performance for various services, such as voice calls, video streaming, and data.

---

## Workflow: Media application using the QoS Network Slice Booking API

A user of a media application would like to book the availability of a network slice for a given time area and QoS Profile. The following steps are executed:

Figure TBD

### Step 0: Pre-conditions
* In principle none. Only after invoking the API the API consumer will receive a response whether the network slice booking can be sucessfuly created.

### Step 1: Create a Network Slice Booking
* **POST /sessions** passing the `serviceTime`, `serviceArea` and `sliceQoSProfiles` parameters.

---

## 5G-MAG's Self-Assessment

The Network Slice Booking API would be used prior to the start of the event in order to book resources for a given time, area and QoS profile.
The booking applies for a service time and area but it not associated to a device.
The QoS Profile is defined for an aggregation of devices each of which gets a pro-rated downstreamrate/upstreamrate value. This may assume a design of the resources for the peak values per device, which may result in overdimensioning resources.
This API may be redundant in comparison with the Dedicated Network API.

Potential improvements:
- For consistency, the definition of the QoS profile could leverage the `qosProfile` defined for other QoS-related APIs.
- The booking could be applied per device rather than to an aggregate of devices
- It is unclear how to associate devices to make use of the resources. As it stands, this process assumed that all devices connected to the network in such area and time window will be covered by such network slice booking.

---

## Network Slice Booking API Usage
With **POST /sessions** and:

A location described as a circle
```
{
  "ServiceTime": {
    "StartTime": "2024-06-01T12:00:00Z",
    "EndTime": "2024-06-01T12:00:00Z"
  },
  "ServiceArea": {
    "AreaType": "CIRCLE",
    "center": {
      "latitude": 45.754114,
      "longitude": 4.860374
    },
    "radius": 800
  },
  "QoSProfile": {
    "MaxNumofTerminals": 5,
    "DLThroughputPerTerminal": {
      "value": 10,
      "unit": "bps"
    },
    "ULThroughputPerTerminal": {
      "value": 10,
      "unit": "bps"
    },
    "DLLatency": {
      "value": 12,
      "unit": "Days"
    },
    "ULLatency": {
      "value": 12,
      "unit": "Days"
    }
  }
}
```

or described as a polygon:

```
  "ServiceArea": {
    "AreaType": "POLYGON",
    "boundary": [
      {
        "latitude": 45.754114,
        "longitude": 4.860374
      },
      {
        "latitude": 45.753845,
        "longitude": 4.863185
      },
      {
        "latitude": 45.753916,
        "longitude": 4.866531
      },
      {
        "latitude": 45.754116,
        "longitude": 4.876353
      }
    ]
  },
```

Type of response: A **sessionID**

```
{
  "status": 200,
  "sessionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "result": "Success"
}
```
