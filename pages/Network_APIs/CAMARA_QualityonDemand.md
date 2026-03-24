---
layout: default
title: CAMARA Quality on Demand
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 9
has_children: false
---

<img src="../../assets/images/Banner_NetworkAPIs.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: Quality on Demand API

## Description

The “Quality-On-Demand” (QoD) API provides a programmable interface for developers to request stable latency or prioritized throughput managed by networks. This API abstracts the complexity of underlying network technologies — such as mobile, fiber, cable, and other broadband networks — allowing developers to focus on enhancing user experiences for applications that demand high-quality network communication.

Information: [https://camaraproject.org/quality-on-demand/](https://camaraproject.org/quality-on-demand/) and [https://github.com/camaraproject/QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

The API definitions can be obtained here: [https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions](https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions)

## Relation of APIs

### Quality on Demand API
  * **POST /sessions** with the request body including a `device` object, `applicationServer` IP, `applicationServerPorts`, `devicePorts`, `qosProfile` and `duration`, it is used to create a QoS session to manage latency/throughput priorities. The response includes information about the creation of the session, with a `sessionId`.
    * Dependency: Requires `qosProfiles` which can be retrieved from a previous call to the [**QoS Profiles API**](./CAMARA_QoSProfiles.html).
  * **GET /sessions/{sessionId}** - Get QoS session information
  * **DELETE /sessions/{sessionId}** - Delete a QoS session
  * **POST /sessions/{sessionId}/extend** - Extend the duration of an active session
  * **POST /retrieve-sessions** - Get QoS session information for a device

---

## Quality-On-Demand (QoD) API Usage

### Request the creation of a session
With **POST /sessions**, to manage latency/throughput priorities.

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
  "qosProfile": "voice",
  "sink": "https://endpoint.example.com/sink",
  "sinkCredential": {
    "credentialType": "PLAIN"
  },
  "duration": 3600
}
```

Type of response: Information about the **status** of the request.

```
{
  "applicationServer": {
    "ipv4Address": "198.51.100.0/24"
  },
  "qosProfile": "QOS_L",
  "sink": "https://application-server.com/notifications",
  "sessionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "duration": 3600,
  "qosStatus": "REQUESTED"
}
```

### Request QoS session information for a device
With **POST /retrieve-sessions** and device object

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

Type of response including QoS sessions information
```
[
  {
    "applicationServer": {
      "ipv4Address": "0.0.0.0/0"
    },
    "qosProfile": "QOS_L",
    "sink": "https://application-server.com/notifications",
    "sessionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "duration": 3600,
    "startedAt": "2024-06-01T12:00:00Z",
    "expiresAt": "2024-06-01T13:00:00Z",
    "qosStatus": "AVAILABLE"
  }
]
```

### Request duration extension of an active QoS session
With **POST /sessions/{sessionId}/extend** and the requested additional duration

```
{
  "requestedAdditionalDuration": 1800
}
```

### Obtain QoS session information
With **GET /sessions/{sessionId}**

```
{
  "duration": 3600,
  "device": {
    "ipv4Address": {
      "publicAddress": "203.0.113.0",
      "publicPort": 59765
    }
  },
  "applicationServer": {
    "ipv4Address": "198.51.100.0/24"
  },
  "qosProfile": "QOS_L",
  "sink": "https://application-server.com/notifications",
  "sessionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "startedAt": "2024-06-01T12:00:00Z",
  "expiresAt": "2024-06-01T13:00:00Z",
  "qosStatus": "AVAILABLE"
}
```
