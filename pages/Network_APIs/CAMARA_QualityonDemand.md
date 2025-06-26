---
layout: default
title: CAMARA: Quality on Demand
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 3
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: Quality on Demand

## Description

* The **Quality-On-Demand (QoD) API** provides a programmable interface for developers and other users (API consumers) to request stable latency or throughput managed by networks without the necessity to have an in-depth knowledge of the underlying network complexity (e.g. the 4G/5G system in case of a mobile network). It offers the application developers the capability to request for stable latency (reduced jitter) or throughput for some specified application data flows between application clients (within a user device) and application servers (backend services). The developer has a pre-defined set of Quality of Service (QoS) profiles which they could choose from depending on their latency or throughput requirements.

* The **Qualtiy-of-Service (QoS) Profiles API** provides a set of predefined network performance characteristics, such as latency, throughput, and priority, identified by a unique name. These profiles allow application developers to specify the desired network behavior for their application's data traffic, ensuring optimal performance. By selecting an appropriate QoS profile, developers can request stable latency (reduced jitter) or throughput for specific data flows between client devices and application servers when used by the Quality-On-Demand APIs.

* The **Quality-on-Demand (QoD) Provisioning API** provides a programmable interface for developers to request the association of a specific QoS profile with a device, indefinitely. The association resulting from the QoD provisioning request is represented by a QoD provisioning record (or QoD provisioning for short) that includes information about the date of provisioning, the QoS profile, the provisioning status, etc., as well as a provisioningId that uniquely identifies this record for later use. Additionally, this API configures the network to apply the requested QoS profile to a specified device whenever the device is connected to the network, until the provisioning is revoked.

Information: [https://github.com/camaraproject/QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

The API definitions can be obtained here: [https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions](https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions)

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
  "sessionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "duration": 3600,
  "startedAt": "2024-06-01T12:00:00Z",
  "expiresAt": "2024-06-01T13:00:00Z",
  "qosStatus": "REQUESTED",
  "statusInfo": "DURATION_EXPIRED"
}
```

### Request QoS session information for a device
With **POST /retrieve-sessions** and device identification

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

### Delete a QoS session
With **DELETE /sessions/{sessionId}**


## Quality-of-Service (QoS) Profiles API Usage

### Obtain QoS profiles available
With **POST /retreive-qos-profiles**, and device parameters.

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
  "name": "voice",
  "status": "ACTIVE"
}
```

Type of response: information about the QoS Profiles

```
[
  {
    "name": "voice",
    "description": "QoS profile for video streaming",
    "status": "ACTIVE",
    "targetMinUpstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "maxUpstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "maxUpstreamBurstRate": {
      "value": 10,
      "unit": "bps"
    },
    "targetMinDownstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "maxDownstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "maxDownstreamBurstRate": {
      "value": 10,
      "unit": "bps"
    },
    "minDuration": {
      "value": 12,
      "unit": "Days"
    },
    "maxDuration": {
      "value": 12,
      "unit": "Days"
    },
    "priority": 20,
    "packetDelayBudget": {
      "value": 12,
      "unit": "Days"
    },
    "jitter": {
      "value": 12,
      "unit": "Days"
    },
    "packetErrorLossRate": 3,
    "l4sQueueType": "non-l4s-queue",
    "serviceClass": "real_time_interactive"
  }
]
```

### Obtain QoS profiles that match a given name
With **GET /qos-profiles/{name}**


## Quality-on-Demand (QoD) Provisioning API Usage

### Provisioning of QoS for a device
With **POST /device-qos**, and device parameters.

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
  "sink": "https://endpoint.example.com/sink",
  "sinkCredential": {}
}
```

Type of response: Returns a **provisioningId**

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
  "sink": "https://endpoint.example.com/sink",
  "sinkCredential": {},
  "provisioningId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "startedAt": "2024-06-01T12:00:00Z",
  "status": "REQUESTED",
  "statusInfo": "NETWORK_TERMINATED"
}
```

### Obtaining the QoD provisioning for a device
With **POST /retrieve-device-qos**, and device parameters.

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

Type of response:

```
{
  "device": {
    "phoneNumber": "+123456789"
  },
  "qosProfile": "QOS_L",
  "sink": "https://application-server.com/callback",
  "sinkCredential": {
    "credentialType": "ACCESSTOKEN",
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    "accessTokenExpiresUtc": "2024-12-01T12:00:00Z",
    "accessTokenType": "bearer"
  },
  "provisioningId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "startedAt": "2024-05-12T17:32:01Z",
  "status": "AVAILABLE"
}
```

### Obtaining the QoD provisioning information
With **GET /device-qos/{provisioningId}**

### Revoking the QoD provisioning
With **DELETE /device-qos/{provisioningId}**
