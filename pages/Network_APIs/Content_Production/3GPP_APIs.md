---
layout: default
title: 3GPP APIs for Qos
parent: Network API Initiatives
grand_parent: Network APIs
nav_order: 0
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Network Exposure and APIs Supporting Media Services and Applications**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Analysis of 3GPP APIs related to Quality of Service

We collect here information about the following CAMARA APIs
 - [Connectivity Insights APIs](#connectivityinsights)
 - [Quality On Demand APIs](#qualityondemand)
 - [QoS Booking APIs](#qosbooking)
 - [Dedicated Networks APIs](#dedicatednetworks)
 - [Network Slice Booking APIs](#networkslicebooking)

----

## [ConnectivityInsights](https://github.com/camaraproject/ConnectivityInsights)

### Description

With CAMARA Connectivity Insights, application developers gain essential visibility into network quality. This enables them to make informed decisions that enhance the end-user experience for their applications.

* The **Connectivity Insights API** allows an application developer to ask the network the likelihood that an application's networking requirements can be met for a given end user session. This information helps a developer ensure their end users are able to get the best experience while using the application over their current network. Depending on the answer the network gives, the developer may decide to request a network boost (via the CAMARA QoD API) , and/or apply specific changes on the application side e.g. adjusting the resolution of the video stream upwards or downwards.

* The **Connectivity Insights Subscriptions API** allows creating and managing a subscription to receive periodic connectivity insights.

* The **Application Profiles API** allows creating and managing a subscription to receive periodic connectivity insights.

The API definitions can be obtained here: [https://github.com/camaraproject/ConnectivityInsights/tree/main/code/API_definitions](https://github.com/camaraproject/ConnectivityInsights/tree/main/code/API_definitions)

### Overall usage
The overall usage would follow this sequence:

  1. Create an application profile using the Connectivity Insights **application-profiles** API
  2. Request: **POST check-network-quality**, passing the **applicationProfileId** obtained in step 1, the address/port of an application server, and at least one device identifier.
  3. Response: The network will indicate whether it can or cannot meet the application requirements.
Optional: use the **connectivity-insights-subscriptions** API to receive notifications of network quality.

### Application Profiles API Usage

#### Create a profile which represent the network demands of an application
With **POST /application-profiles**

```
{
  "networkQualityThresholds": {
    "packetDelayBudget": {
      "value": 12,
      "unit": "Minutes"
    },
    "targetMinDownstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "targetMinUpstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "packetlossErrorRate": 3,
    "jitter": {
      "value": 12,
      "unit": "Minutes"
    }
  }
}
```

Type of response: An **applicationProfileId**

```
{
  "applicationProfileId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "networkQualityThresholds": {
    "packetDelayBudget": {
      "value": 12,
      "unit": "Minutes"
    },
    "targetMinDownstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "targetMinUpstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "packetlossErrorRate": 3,
    "jitter": {
      "value": 12,
      "unit": "Minutes"
    }
  }
}
```

Parameters:
  - "packet delay budget": the maximum allowable one-way latency between the customer's device and the gateway from the operator's network to other networks. The end-to-end or round trip latency will be about two times this value plus the latency not controlled by the operator
  - "targetMinDownstreamRate": This is the target minimum downstream rate.
  - "targetMinUpstreamRate": This is the target minimum upstream rate
  - "packetlossErrorRate": The exponential power of the allowable error loss rate 10^(-N). For 5G network the 3GPP specification TS 23.203 defines the packet error loss rate QCI attribute.
  - "jitter" requirement aims to limit the maximum variation in round-trip packet delay for the 99th percentile of traffic, following ITU Y.1540 standards. It considers only acknowledged packets in a session, which are packets that receive a confirmation of receipt from the recipient (e.g., using TCP).

#### Update the profile
With **PATCH /application-profiles/{applicationProfileId}**

#### Obtain an existing application profile
With **GET /application-profiles/{applicationProfileId}**

#### Delete an existing application profile
With **DELETE /application-profiles/{applicationProfileId}**

### Connectivity Insights API Usage

#### Obtain information about network quality
With **POST /check-network-quality** and:

  - An **ApplicationProfileId** and one or more device identifiers. Together these allow the network to calculate whether the thresholds defined in the application profile can be met for the particular connected device.
  - Identifier for the device: At least one identifier for the device (user equipment) out of four options: IPv4 address, IPv6 address, Phone number, or Network Access Identifier assigned by the mobile network operator for the device.
  - Identifier for the application server: IPv4 and/or IPv6 address of the application server (application backend)
  - Notification URL and token: Developers may provide a callback URL on which notifications can be received from the service provider. This is an optional parameter.

```
{
  "applicationProfileId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "device": {
    "phoneNumber": "123456789",
    "networkAccessIdentifier": "123456789@domain.com",
    "ipv4Address": {
      "publicAddress": "84.125.93.10",
      "publicPort": 59765
    },
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  },
  "applicationServer": {
    "ipv4Address": "192.168.0.1/24",
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
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
  "monitoringTimeStamp": "2023-07-03T12:27:08.312Z"
}
```

Type of response: The network's current level of confidence that it can meet an application profile's quality thresholds for a given end user device.

```
{
  "packetDelayBudget": "meets the application requirements",
  "targetMinDownstreamRate": "meets the application requirements",
  "targetMinUpstreamRate": "meets the application requirements",
  "packetlossErrorRate": "meets the application requirements",
  "jitter": "meets the application requirements",
  "additionalKPIs": {
    "signalStrength": "excellent",
    "connectivityType": "5G-SA"
  }
}
```

### Connectivity Insights Subscriptions API Usage

#### Create a subcription for a device
With **POST /subscriptions**

```
{
  "protocol": "HTTP",
  "sink": "https://endpoint.example.com/sink",
  "sinkCredential": {},
  "types": [
    "org.camaraproject.connectivity-insights-subscriptions.v0.network-quality"
  ],
  "config": {
    "subscriptionDetail": {
      "device": {
        "phoneNumber": "123456789",
        "networkAccessIdentifier": "123456789@domain.com",
        "ipv4Address": {
          "publicAddress": "84.125.93.10",
          "publicPort": 59765
        },
        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
      },
      "applicationServer": {
        "ipv4Address": "192.168.0.1/24",
        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
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
      "applicationProfileId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    },
    "subscriptionExpireTime": "2023-07-03T12:27:08.312Z",
    "subscriptionMaxEvents": 5,
    "initialEvent": true
  }
}
```

Type of response: A **subcriptionId**

```
{
  "sink": "https://endpoint.example.com/sink",
  "types": [
    "string"
  ],
  "config": {
    "subscriptionDetail": {
      "device": {
        "phoneNumber": "123456789",
        "networkAccessIdentifier": "123456789@domain.com",
        "ipv4Address": {
          "publicAddress": "84.125.93.10",
          "publicPort": 59765
        },
        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
      },
      "applicationServer": {
        "ipv4Address": "192.168.0.1/24",
        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
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
      "applicationProfileId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    },
    "subscriptionExpireTime": "2023-07-03T12:27:08.312Z",
    "subscriptionMaxEvents": 5,
    "initialEvent": true
  },
  "subscriptionId": "1119920371",
  "startsAt": "2023-07-03T12:27:08.312Z",
  "expiresAt": "2023-07-03T12:27:08.312Z",
  "status": "ACTIVATION_REQUESTED"
}
```

#### Obtain a list of event subscription details
With **GET /subscriptions**

#### Obtain a subscription based on the provided ID
With **GET /subscriptions/{subscriptionId}**

#### Delete a subscription based on the provided ID
With **DELETE /subscriptions/{subscriptionId}**


## [QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

### Description

* The **Quality-On-Demand (QoD) API** provides a programmable interface for developers and other users (API consumers) to request stable latency or throughput managed by networks without the necessity to have an in-depth knowledge of the underlying network complexity (e.g. the 4G/5G system in case of a mobile network). It offers the application developers the capability to request for stable latency (reduced jitter) or throughput for some specified application data flows between application clients (within a user device) and application servers (backend services). The developer has a pre-defined set of Quality of Service (QoS) profiles which they could choose from depending on their latency or throughput requirements.

* The **Qualtiy-of-Service (QoS) Profiles API** provides a set of predefined network performance characteristics, such as latency, throughput, and priority, identified by a unique name. These profiles allow application developers to specify the desired network behavior for their application's data traffic, ensuring optimal performance. By selecting an appropriate QoS profile, developers can request stable latency (reduced jitter) or throughput for specific data flows between client devices and application servers when used by the Quality-On-Demand APIs.

* The **Quality-on-Demand (QoD) Provisioning API** provides a programmable interface for developers to request the association of a specific QoS profile with a device, indefinitely. The association resulting from the QoD provisioning request is represented by a QoD provisioning record (or QoD provisioning for short) that includes information about the date of provisioning, the QoS profile, the provisioning status, etc., as well as a provisioningId that uniquely identifies this record for later use. Additionally, this API configures the network to apply the requested QoS profile to a specified device whenever the device is connected to the network, until the provisioning is revoked.

The API definitions can be obtained here: [https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions](https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions)

### Quality-On-Demand (QoD) API Usage

#### Request the creation of a session
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

#### Request QoS session information for a device
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

#### Request duration extension of an active QoS session
With **POST /sessions/{sessionId}/extend** and the requested additional duration

```
{
  "requestedAdditionalDuration": 1800
}
```

#### Obtain QoS session information
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

#### Delete a QoS session
With **DELETE /sessions/{sessionId}**


### Quality-of-Service (QoS) Profiles API Usage

#### Obtain QoS profiles available
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

#### Obtain QoS profiles that match a given name
With **GET /qos-profiles/{name}**


### Quality-on-Demand (QoD) Provisioning API Usage

#### Provisioning of QoS for a device
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

#### Obtaining the QoD provisioning for a device
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

#### Obtaining the QoD provisioning information
With **GET /device-qos/{provisioningId}**

#### Revoking the QoD provisioning
With **DELETE /device-qos/{provisioningId}**


----


## [QoSBooking](https://github.com/camaraproject/QoSBooking)

### Description

* The **QoS (Quality of Service) Booking API** provides programmable interface for developers and other users (capabilities consumers) to request in advance certain network conditions to be provided by Telco networks, without the necessity to have an in-depth knowledge of the underlying network complexity (e.g. the 4G/5G system in case of a mobile network).

The API definitions can be obtained here: [https://github.com/camaraproject/QoSBooking/tree/main/code/API_definitions](https://github.com/camaraproject/QoSBooking/tree/main/code/API_definitions)

### QoS Booking API Usage

#### Request booking of QoS for a device
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

#### Obtains the existing QoS booking for a device
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

#### Obtains the QoS booking information
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

#### Delete the QoS booking
With **DELETE /device-qos-bookings/{bookingId}**

----


## [DedicatedNetworks](https://github.com/camaraproject/DedicatedNetworks)

### Description

The Dedicated Network APIs are a set of APIs to provide functionalities for reserving network connectivity resources (e.g. throughput) potentially with an SLA and for time and location (service area) limits, discover supported and prepared network capabilities/resources (e.g. existing slices to connect to), manage device access, offering insights based on network profiles and resource states.

* The **Dedicated Network API** is invoked for reservation and lifecycle management of network connectivity resources for dedicated use. A Dedicated Network is a logical resource and is used to embody the reservation of network connectivity resources in the physical network. Initiating a new reservation request using this API results in a new Dedicated Network resource being created. The Dedicated Network undergoes various lifecycle States including REQUESTED, RESERVED, ACTIVATED and TERMINATED. Reservation of resources occurs based on the selected **Network Profile**, **duration** when the reservation is needed (Service Time) and **geographical areas** where the service is needed (Service Area).

* The **Dedicated Network Profiles API** is invoked for discovery of predefined set of network capabilities and performance characteristics. A Network Profile represents a predefined set of network capabilities and performance characteristics that can be applied when creating dedicated networks. Each profile represents a validated, supported configuration that has been pre-approved in the terms and conditions between the API Provider and API Consumer.

* The **Dedicated Network Accesses API** is invoked to managing access to the Dedicated Network, i.e., controlling which devices may benefit from the reserved resources and capabilities. A Device Access represents the permission for a specific device to use a Dedicated Network's reserved connectivity resources. The usage of resources can be tailored to each device within the constraints of the applicable Network Profile.

The API definitions can be obtained here: [https://github.com/camaraproject/DedicatedNetworks/tree/main/code/API_definitions](https://github.com/camaraproject/DedicatedNetworks/tree/main/code/API_definitions)

### Dedicated Network API Usage

This API allows for requesting a Dedicated Network, which provides a set of capabilities and connectivity performance targets. The Dedicated Network may be requested for a particular geographical location and at a particular time window. Depending on the requested start time for the dedicated network, the network may first enter a reserved state.

#### Request the creation of a dedicated network
With **POST /networks**, passing a **profileId**, **serviceTime**, **serviceArea**, among others.

```
{
  "profileId": "string",
  "serviceTime": {
    "start": "2025-06-18T11:42:33.700Z",
    "end": "2025-06-18T11:42:33.700Z"
  },
  "serviceArea": {},
  "sink": "string",
  "sinkCredential": {}
}
```

Type of response: Information about the **status** of the request.

```
[
  {
    "profileId": "string",
    "serviceTime": {
      "start": "2025-06-18T11:41:09.988Z",
      "end": "2025-06-18T11:41:09.988Z"
    },
    "serviceArea": {},
    "sink": "string",
    "sinkCredential": {},
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "status": "REQUESTED"
  }
]
```

#### Obtain a list of dedicated networks
With **GET /networks**

```
[
  {
    "profileId": "string",
    "serviceTime": {
      "start": "2025-06-18T11:47:40.371Z",
      "end": "2025-06-18T11:47:40.371Z"
    },
    "serviceArea": {},
    "sink": "string",
    "sinkCredential": {},
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "status": "REQUESTED"
  }
]
```

#### Obtain the current information about a dedicated network
With **GET /networks/{networkId}**

#### Delete a dedicated network
With **DELETE /networks/{networkId}**

### Dedicated Network Profiles API Usage

This API allows for discovering available network profiles, which are offered by the network provider to be used in conjunction of the Dedicated Network API. Network profiles describe the capabilities and performance targets of a dedicated network. A Network Profile represents a predefined set of network capabilities and performance characteristics that can be applied when creating a Network. It enables API Consumers to understand the capabilities they can expect when using the reserved network connectivity resources. A Network Profile is a validated, supported configuration that has been pre-approved between the API Provider and API Consumer.

A Network Profile contains information about:
- the maximum number of devices allowed,
- the aggregated throughput to be provided,
- a set of allowed QoS Profiles that devices can use when having access to the Dedicated Network.

#### Obtain list of available dedicated network profiles
With **GET GET /profiles**

```
[
  {
    "id": "string",
    "maxNumberOfDevices": 0,
    "aggregatedUlThroughput": {
      "value": 10,
      "unit": "bps"
    },
    "aggregatedDlThroughput": {
      "value": 10,
      "unit": "bps"
    },
    "qosProfiles": [
      "string"
    ],
    "defaultQosProfile": "string"
  }
]
```

#### Obtain list of available dedicated network profiles
With **GET GET /profiles**

```
[
  {
    "id": "string",
    "maxNumberOfDevices": 0,
    "aggregatedUlThroughput": {
      "value": 10,
      "unit": "bps"
    },
    "aggregatedDlThroughput": {
      "value": 10,
      "unit": "bps"
    },
    "qosProfiles": [
      "string"
    ],
    "defaultQosProfile": "string"
  }
]
```

#### Obtain a dedicated network profiles
With **GET /profiles/{profileId}**

### Dedicated Network Accesses API Usage
This API allows for requesting network access for devices. A device is identified by the CAMARA device object, containing either an MSIDSN or a Network Access Identifier.
A Device Access represents the permission for a specific device to use a Dedicated Network's reserved connectivity resources. Only devices for which a Device Access resource has been created can use the connectivity resources allocated for that network. The usage of resources can be tailored to each device within the constraints of the applicable Network Profile.

#### Create a device access to a dedicated network with given configuration
With **POST /accesses**

```
{
  "networkId": "string",
  "device": {
    "phoneNumber": "+123456789",
    "networkAccessIdentifier": "123456789@domain.com"
  },
  "qosProfiles": [
    "string"
  ],
  "defaultQosProfile": "string"
}
```

Type of response: An **id** for the requested device access.

```
{
  "networkId": "string",
  "device": {
    "phoneNumber": "+123456789",
    "networkAccessIdentifier": "123456789@domain.com"
  },
  "qosProfiles": [
    "string"
  ],
  "defaultQosProfile": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

#### Obtain a list of device accesses to dedicated networks
With **GET /accesses**

```
[
  {
    "networkId": "string",
    "device": {
      "phoneNumber": "+123456789",
      "networkAccessIdentifier": "123456789@domain.com"
    },
    "qosProfiles": [
      "string"
    ],
    "defaultQosProfile": "string",
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
]
```

#### Obtain a device access to the dedicated network
With **GET /accesses/{accessId}**

#### Delete a device access to the dedicated network
With **DELETE /accesses/{accessId}**


----


## [NetworkSliceBooking](https://github.com/camaraproject/NetworkSliceBooking)

### Description

The **Network Slice Booking (NSB) API** provides programmable interface for developers to reserve a slice resource of a selected area within a period, and manage device access control as needed.

The API definitions can be obtained here: [https://github.com/camaraproject/NetworkSliceBooking/blob/main/code/API_definitions](https://github.com/camaraproject/NetworkSliceBooking/blob/main/code/API_definitions)

### Network Slice Booking (NSB) API Usage

#### Create a new Network Slide Booking session
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

#### Obtain information about an existing Network Slide Booking session
With **GET /sessions/{sessionId}**

#### Delete an existing Network Slide Booking session
With **DELETE /sessions/{sessionId}**












OTHER APIs not yet analysed

### [DeviceIdentifier](https://github.com/camaraproject/DeviceIdentifier)

#### Scope
- Service APIs for “Device Identifier API” (see API Backlog)
- It provides the customer with the ability to:
  - Retrieve the current identity (IMEI) of the mobile device being used by a given mobile subscriber
  - Retrieve the type (manufacturer and model) of the mobile device being used by a given mobile subscriber

### [DeviceLocation](https://github.com/camaraproject/DeviceLocation)

#### Scope
- Service APIs for “Device Location” (see APIBacklog)
- It provides the customer with the ability to:
  - verify the location of a device (location-verification).
  - retrieve the location of a device (location-retrieval).
  - subscribe and receive notifications about a device entering or leaving certain location (geofencing-subscriptions).
  - NOTE: The scope of this API family should be limited (at least at a first stage) to 4G and 5G.

### [DeviceStatus](https://github.com/camaraproject/DeviceStatus)

#### Scope
- Service APIs for “Device Status” (see APIBacklog)
- It provides the API consumer with the ability to:
  - check if a device is reachable or is not connected to the network
  - check if a device is roaming, and in which country
  - receive notifications if the connectivity or roaming status of the device changes
