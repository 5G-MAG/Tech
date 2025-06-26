---
layout: default
title: CAMARA: Network Slice Booking
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 3
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: Network Slice Booking

## Description

The **Network Slice Booking (NSB) API** provides programmable interface for developers to reserve a slice resource of a selected area within a period, and manage device access control as needed.

Information: [https://github.com/camaraproject/NetworkSliceBooking](https://github.com/camaraproject/NetworkSliceBooking)

The API definitions can be obtained here: [https://github.com/camaraproject/NetworkSliceBooking/blob/main/code/API_definitions](https://github.com/camaraproject/NetworkSliceBooking/blob/main/code/API_definitions)

## Network Slice Booking (NSB) API Usage

### Create a new Network Slide Booking session
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
{
  "ServiceTime": {
    "StartTime": "2024-06-01T12:00:00Z",
    "EndTime": "2024-06-01T12:00:00Z"
  },
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

Type of response: A **sessionID**

```
{
  "status": 200,
  "sessionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "result": "Success"
}
```

### Obtain information about an existing Network Slide Booking session
With **GET /sessions/{sessionId}**

### Delete an existing Network Slide Booking session
With **DELETE /sessions/{sessionId}**
