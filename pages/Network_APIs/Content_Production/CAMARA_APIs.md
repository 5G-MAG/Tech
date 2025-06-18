---
layout: default
title: Analysis of CAMARA APIs
parent: Content Production & Contribution
grand_parent: Network APIs
nav_order: 4
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Network Exposure and APIs Supporting Media Services and Applications**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Analysis of CAMARA APIs within the scope of Content Production & Contribution

We collect here information about the following CAMARA APIs
 - [ConnectivityInsights](https://5g-mag.github.io/Tech/pages/Network_APIs/Content_Production/CAMARA_APIs.html#connectivityinsights)
 - [QualityOnDemand](https://5g-mag.github.io/Tech/pages/Network_APIs/Content_Production/CAMARA_APIs.html#qualityondemand)
 - [QualityOnDemand Provisioning](https://5g-mag.github.io/Tech/pages/Network_APIs/Content_Production/CAMARA_APIs.html#qualityondemand-provisioning)
 - [DedicatedNetworks](https://jordijoangimenez.github.io/Tech/pages/Network_APIs/Content_Production/CAMARA_APIs.html#dedicatednetworks)

## General information

- CAMARA Repositories in GitHub: [Link](https://github.com/orgs/camaraproject/repositories?q=sort%3Aname-asc)
- API Backlog: [Link](https://github.com/camaraproject/WorkingGroups/blob/main/APIBacklog/documentation/APIbacklog.md)
- Proposed new APIs: [Link](https://github.com/camaraproject/WorkingGroups/pulls)

Potentially additional APIs:
* QOS Boking: 
  * https://github.com/camaraproject/QoSBooking
  * Yaml in PR: Only a withdrawn yaml: https://github.com/camaraproject/QoSBooking/pull/5
  * API Backlog: [documentation/API proposals/APIproposal_QoS_Booking_KDDI.md](https://github.com/camaraproject/APIBacklog/blob/main/documentation/API%20proposals/APIproposal_QoS_Booking_KDDI.md)
  * 

* Network Slice Booking
  * https://github.com/camaraproject/NetworkSliceBooking
  * But no real progress since some time.
  * API Backlog: https://github.com/camaraproject/APIBacklog/blob/main/documentation/API%20proposals/APIproposal_NetworkSlicing_ChinaUnicom.md
  * Supporting slides: https://github.com/camaraproject/APIBacklog/raw/refs/heads/main/documentation/SupportingDocuments/Network%20Slicing%20Service%20API%20Introduction%20for%20CAMARA.PPTX

## [ConnectivityInsights](https://github.com/camaraproject/ConnectivityInsights)

### Description

The Connectivity Insights API allows an application developer to ask the network the likelihood that an application's networking requirements can be met for a given end user session.
Depending on the answer the network gives, the developer may decide to request a network boost (via the CAMARA QoD API), and/or apply specific changes on the application side e.g. adjusting the resolution of the video stream upwards or downwards.

### Usage

1. Create an Application Profile using the Connectivity Insights **_application-profiles_ API**. It retruns an **_applicationProfileId_**
2. Request with a **POST _check-network-quality_**, passing:
    - the **_applicationProfileId_** obtained in step 1
    - the address/port of an application server, and
    - at least one device identifier.
3. Response: The network will indicate whether it can or cannot meet the application requirements.
Optional: use the **_connectivity-insights-subscriptions_ API** to receive subcribe to notifications of network quality.

#### How does an Application Profile look like?

Example:

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

  - "packet delay budget": the maximum allowable one-way latency between the customer's device and the gateway from the operator's network to other networks. The end-to-end or round trip latency will be about two times this value plus the latency not controlled by the operator
  - "targetMinDownstreamRate": This is the target minimum downstream rate.
  - "targetMinUpstreamRate": This is the target minimum upstream rate
  - "packetlossErrorRate": The exponential power of the allowable error loss rate 10^(-N). For 5G network the 3GPP specification TS 23.203 defines the packet error loss rate QCI attribute.
  - "jitter" requirement aims to limit the maximum variation in round-trip packet delay for the 99th percentile of traffic, following ITU Y.1540 standards. It considers only acknowledged packets in a session, which are packets that receive a confirmation of receipt from the recipient (e.g., using TCP).

#### How to check network quality?

Example:

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

  - An ApplicationProfileId and one or more device identifiers. Together these allow the network to calculate whether the thresholds defined in the application profile can be met for the particular connected device.
  - Identifier for the device: At least one identifier for the device (user equipment) out of four options: IPv4 address, IPv6 address, Phone number, or Network Access Identifier assigned by the mobile network operator for the device.
  - Identifier for the application server: IPv4 and/or IPv6 address of the application server (application backend)
  - Notification URL and token: Developers may provide a callback URL on which notifications can be received from the service provider. This is an optional parameter.

Type of response:

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

#### How to subscribe to notifications?

Example:

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

#### How is a device identified?

Device identifiers include:
  - `ipv4Address`
  - `ipv6Address`
  - `phoneNumber`: A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+' (e.g. "+123456789").
  - `networkAccessIdentifier`: A public identifier addressing a subscription in a mobile network. In 3GPP terminology, it corresponds to the GPSI formatted with the External Identifier ({Local Identifier}@{Domain Identifier}). Unlike the telephone number, the network access identifier is not subjected to portability ruling in force, and is individually managed by each operator (e.g. "123456789@domain.com")

## [QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

### Description

**Scope:** QoS profiles per App-Flow

The Quality-On-Demand (QoD) API provides a programmable interface for developers and other users (API consumers) to request stable latency or throughput managed by networks without the necessity to have an in-depth knowledge of the underlying network complexity (e.g. the 4G/5G system in case of a mobile network).

### Usage

The usage of the QoD API is based on QoS profile classes and parameters which define App-Flows. Based on the API, QoS session resources can be created, queried, and deleted. Once an offered QoS profile class is requested, application users get a prioritized service with stable latency or throughput even in the case of congestion.

1. Retrieve QoS profiles available by **POST _/retreive-qos-profiles_**
2. Create a QoS session by **POST _/sessions_**. It retruns session details and notifications into a sink address.
    - indication of a **_qosProfile_** and labels: Latency, throughput or priority requirements of the application mapped to relevant QoS profile values. Available QoS profiles can be obtained with a GET
    - the address/port of an application server,
    - the address/port of the server used to receive notifications, and
    - a device identifier.
3. Response: The network will indicate whether the request is active and for how long.

#### How to retrieve QoS profiles?

```
{
  "device": {
  "phoneNumber": "+123456789",
  "networkAccessIdentifier": "123456789@domain.com",
  "ipv4Address": {},
  "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  },
  "name": "voice",
  "status": "ACTIVE"
}
```

Type of response:

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

#### How to create a QoS session?

Example:

```
{
  "device": {
    "phoneNumber": "+123456789",
    "networkAccessIdentifier": "123456789@domain.com",
    "ipv4Address": {},
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  },
  "applicationServer": {
    "ipv4Address": "198.51.100.0/24",
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  },
  "devicePorts": {
    "ranges": [],
    "ports": []
  },
  "applicationServerPorts": {
    "ranges": [],
    "ports": []
  },
  "qosProfile": "voice",
  "sink": "https://endpoint.example.com/sink",
  "sinkCredential": {
    "credentialType": "PLAIN"
  },
  "duration": 3600
}
```

Type of response:

```
{
  "sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
  "duration": 3600,
  "startedAt": "2024-06-01T12:00:00Z",
  "expiresAt": "2024-06-01T13:00:00Z",
  "qosStatus": "REQUESTED",
  "statusInfo": "DURATION_EXPIRED"
}
```

#### How is a device identified?

Device identifiers include:
  - `ipv4Address`
  - `ipv6Address`
  - `phoneNumber`: A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+' (e.g. "+123456789").
  - `networkAccessIdentifier`: A public identifier addressing a subscription in a mobile network. In 3GPP terminology, it corresponds to the GPSI formatted with the External Identifier ({Local Identifier}@{Domain Identifier}). Unlike the telephone number, the network access identifier is not subjected to portability ruling in force, and is individually managed by each operator (e.g. "123456789@domain.com")

## [QualityOnDemand Provisioning](https://github.com/camaraproject/QualityOnDemand)

### Description

The Quality-on-Demand (QoD) Provisioning API provides a programmable interface for developers to request the association of a specific QoS profile with a device, indefinitely. The association resulting from the QoD provisioning request is represented by a QoD provisioning record (or QoD provisioning for short) that includes information about the date of provisioning, the QoS profile, the provisioning status, etc., as well as a provisioningId that uniquely identifies this record for later use. Additionally, this API configures the network to apply the requested QoS profile to a specified device whenever the device is connected to the network, until the provisioning is revoked.

### Usage

1. Provision QoS profile for a device by **POST _/device-qos_**
    - indication of a **_qosProfile_** and labels: Latency, throughput or priority requirements of the application mapped to relevant QoS profile values. Available QoS profiles can be obtained with a GET
    - the address/port of the server used to receive notifications, and
    - a device identifier.
3. Response: The network will indicate whether the request is active and for how long.

#### How to provision a QoS profile for a device?

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
  "sinkCredential": {
    "credentialType": "PLAIN"
  }
}
```

Type of response:

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
  "sinkCredential": {
    "credentialType": "PLAIN"
  },
  "provisioningId": "8857548e-8974-477e-95e6-d461c2c06b56",
  "startedAt": "2024-06-01T12:00:00Z",
  "status": "REQUESTED",
  "statusInfo": "NETWORK_TERMINATED"
}
```

#### How is a device identified?

Device identifiers include:
  - `ipv4Address`
  - `ipv6Address`
  - `phoneNumber`: A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+' (e.g. "+123456789").
  - `networkAccessIdentifier`: A public identifier addressing a subscription in a mobile network. In 3GPP terminology, it corresponds to the GPSI formatted with the External Identifier ({Local Identifier}@{Domain Identifier}). Unlike the telephone number, the network access identifier is not subjected to portability ruling in force, and is individually managed by each operator (e.g. "123456789@domain.com")

## [DedicatedNetworks](https://github.com/camaraproject/DedicatedNetworks)

### Description

The Dedicated Network APIs are a set of APIs to provide functionalities for reserving network connectivity resources (e.g. throughput) potentially with an SLA and for time and location (service area) limits, discover supported and prepared network capabilities/resources (e.g. existing slices to connect to), manage device access, offering insights based on network profiles and resource states.

* The **Dedicated Network API** is invoked for reservation and lifecycle management of network connectivity resources for dedicated use. A Dedicated Network is a logical resource and is used to embody the reservation of network connectivity resources in the physical network. Initiating a new reservation request using this API results in a new Dedicated Network resource being created. The Dedicated Network undergoes various lifecycle States including REQUESTED, RESERVED, ACTIVATED and TERMINATED. Reservation of resources occurs based on the selected **Network Profile**, **duration** when the reservation is needed (Service Time) and **geographical areas** where the service is needed (Service Area).

* The **Dedicated Network Profiles API** is invoked for discovery of predefined set of network capabilities and performance characteristics. A Network Profile represents a predefined set of network capabilities and performance characteristics that can be applied when creating dedicated networks. Each profile represents a validated, supported configuration that has been pre-approved in the terms and conditions between the API Provider and API Consumer.

* The **Dedicated Network Accesses API** is invoked to managing access to the Dedicated Network, i.e., controlling which devices may benefit from the reserved resources and capabilities. A Device Access represents the permission for a specific device to use a Dedicated Network's reserved connectivity resources. The usage of resources can be tailored to each device within the constraints of the applicable Network Profile.

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

### [NetworkSliceBooking](https://github.com/camaraproject/NetworkSliceBooking)

#### Scope
- Service APIs for “Network Slice Booking” (see APIBacklog.md)
- It provides the customer with the ability to:
  - reserve, dynamically provisioning, query, dynamically delete a slice with customized SLA assurance capabilities, customized service duration, expected slice covered locations.

