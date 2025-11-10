---
layout: default
title: CAMARA Quality on Demand
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 0
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: Quality on Demand

## Description

The Quality-On-Demand (QoD) APIs provides a programmable interface for developers and other users (API consumers) to request stable latency or throughput managed by networks without the necessity to have an in-depth knowledge of the underlying network complexity (e.g. the 4G/5G system in case of a mobile network).

Information: [https://github.com/camaraproject/QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

The API definitions can be obtained here: [https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions](https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions)

## Relation of APIs

### QoS Profiles API
  * **POST /retrieve-qos-profiles** with a request body including a `device` object, `name` of the profile and `status`, it is used to query QoS Profiles for a given device. The response contains information about the QoS Profiles
  * **GET /qos-profiles/{name}** - get QoS Profile for a given name

#### Parameters describing a QoS Profile
* `packetDelayBudget`- the maximum allowable one-way latency between the customer's device and the gateway from the operator's network to other networks. The end-to-end or round trip latency will be about two times this value plus the latency not controlled by the operator
* `targetMinDownstreamRate` - the target minimum downstream rate.
* `targetMinUpstreamRate` - the target minimum upstream rate
* `packetLossErrorRate` - the exponential power of the allowable error loss rate 10^(-N). For 5G network the 3GPP specification TS 23.203 defines the packet error loss rate QCI attribute.
* `jitter`  - this requirement aims to limit the maximum variation in round-trip packet delay for the 99th percentile of traffic, following ITU Y.1540 standards. It considers only acknowledged packets in a session, which are packets that receive a confirmation of receipt from the recipient (e.g., using TCP).
* `minDuration`
* `maxDuration`
* `priority`
* `l4sQueueType`

### Quality on Demand API
  * **POST /sessions** with the request body including a `device` object, `applicationServer` IP, `applicationServerPorts`, `devicePorts`, `qosProfile` and `duration`, it is used to create a QoS session to manage latency/throughput priorities. The response includes information about the creation of the session, with a `sessionId`.
  * **GET /sessions/{sessionId}** - Get QoS session information
  * **DELETE /sessions/{sessionId}** - Delete a QoS session
  * **POST /sessions/{sessionId}/extend** - Extend the duration of an active session
  * **POST /retrieve-sessions** - Get QoS session information for a device

### QoS Provisioning API
  * **POST /qos-assignments** with the request body including a `device` object and `qosProfile`, this request will assign a QoS profile to a device. The response includes an `assignmentId`.
  * **GET /qos-assignments/{assignmentId}** - Querying for details about the QoS profile assignment
  * **DELETE /qos-assignments/{assignmentId}** - Revokes the assignment of a QoS profile to a device performed by a previous assignment operation.
  * **POST /retrieve-qos-assignment** with the request body including the `device` object, this request will return information about the QoS profile assignment for the device with an `assignmentId`.

---

## Workflow: Media application using the QoS Provisioning API to assign a QoS profile to a device

A user of a media application would like to request the assignment of a QoS Profile to a device. The following steps are executed:

<figure>
  <img src="./Content_Production/images/figure_qualityondemand.png" width="80%">
</figure>

### Step 0: Pre-conditions
* The API invoker needs to have signed up with the API provider.
* qosProfiles have already been defined and made available by the network operator.
* Names of such qosProfiles have been disclosed to the user so they can be used when invoking APIs.

### Step 1: Check details of an existing QoS Profile (when not cached)
* **GET /qos-profiles/{name}** to obtain the parameters of the QoS Profile

### Step 2: Attach a device to the QoS Profile
* **POST /qos-assignments** passing the `device` object and the name of the `qosProfile`
* The received "assignmentId" could be used to query details or revoke the assignment
* This QoS profile will be assigned to the device anytime it is connected to the network.

## Workflow: Media application using the Quality on Demand API to create a QoS session

A user of a media application would like to request the creation of a QoS session for the connection between a device and an application server. The following steps are executed:

<figure>
  <img src="./Content_Production/images/figure_qualityondemand.png" width="80%">
</figure>

### Step 0: Pre-conditions
* The API invoker needs to have signed up with the API provider.
* qosProfiles have already been defined and made available by the network operator.
* Names of such qosProfiles have been disclosed to the user so they can be used when invoking APIs.

### Step 1: Check details of an existing QoS Profile (when not cached)
* **GET /qos-profiles/{name}** to obtain the parameters of the QoS Profile

### Step 2: Establish a QoS session
* **POST /sessions** passing the `device` object, `applicationServer` IP, `applicationServerPorts`, `devicePorts`, `qosProfile` and `duration`.

---

## 5G-MAG's Self-Assessment

The QoS Profiles API would be used prior to the start of the event in order to understand the profiles and details of the profiles available in the network. However, it seems that the only way to obtain the list of parameters of a profile is by invoking the API with the QoS Profile `name`. There is a method lacking the query of profile names. There is also no method to define QoS Profiles, and this operation should be done beforehand.

A session may be created by establishing a level of QoS between the device and the application server for a given duration. It is assumed that the QoS Provisioning would result successful when invoked in the given location. However as a service area cannot be defined/requested, it is unclear whether this would be successful or not.

Potential improvements:
- A way to list profile names available in the network
- A solution to the fact that QoS Profiles need to be established manually before being able to invoke them.
- There is no information about the location or service area.
- Understanding opportunities to book QoS sessions in terms of duration and location/area would be useful as the user may be able to move and find a better coverage spot rather than being denied the establishment of QoS at the time and location in which it is requested.

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

## Quality-on-Demand (QoD) Provisioning API Usage

### Provisioning of QoS for a device

### Obtaining the QoD provisioning for a device
With **POST /retrieve-device-qos**, and device object.

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
