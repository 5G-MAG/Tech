---
layout: default
title: CAMARA APIs
parent: Content Production & Contribution
grand_parent: Network APIs
nav_order: 2
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Network Exposure and APIs Supporting Media Services and Applications**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Requirements coverage by CAMARA APIs

## Media delivery with Quality of Service (QoS)

 Requirement | CAMARA APIs  
 -- | --
Ability to apply different QoS profiles to individual data flows coming from the same production device node | 
Ability to separate media/data flows coming from the same production device node | 
Delivery to endpoint (Application Media Server) may be identified by security/protocol/IP/port | 
Ability to configure new or re-configure existing QoS profiles to be selected during runtime  | 
Ability to select at runtime a QoS profile for a media flow | 
Ability to receive ACK (success/fail) | 

## Information monitoring, logging and/or Network assistance

 Requirement | CAMARA APIs  
 -- | --
Ability to receive real-time information from the network | 
Ability to receive information from the network during runtime for troubleshooting | 
Ability to receive information from the network after the session (logging information) for post-processing | 

## Time Synchronization

 Requirement | CAMARA APIs  
 -- | --
Ability to enable distribution of timing information | 

## Voice service for Intercom

 Requirement | CAMARA APIs  
 -- | --
Ability to establish a voice service across the intercom devices deployed at the production location or between the production center and the production location | 

# Considerations for API selection

## Identification of devices
  - Devices should be uniquely identifiable during operation
  - Devices should be dynamically added or deleted during operation and attachable to given network capabilities
  - Each device should only access the network capabilities which have been assigned during booking.

## Device on-boarding and API consumer on-boarding
- TBD How to obtain credentials

## Discovery of network capabilities
- TBD How to discover network capabilities

# CAMARA APIs and related aspects within the scope of Content Production & Contribution

## General information

- CAMARA Repositories in GitHub: [Link](https://github.com/orgs/camaraproject/repositories?q=sort%3Aname-asc)
- API Backlog: [Link](https://github.com/camaraproject/WorkingGroups/blob/main/APIBacklog/documentation/APIbacklog.md)
- Proposed new APIs: [Link](https://github.com/camaraproject/WorkingGroups/pulls)

## Device identification

### Description
Device identifiers include:
  - `ipv4Address`
  - `ipv6Address`
  - `phoneNumber`: A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+' (e.g. "+123456789").
  - `networkAccessIdentifier`: A public identifier addressing a subscription in a mobile network. In 3GPP terminology, it corresponds to the GPSI formatted with the External Identifier ({Local Identifier}@{Domain Identifier}). Unlike the telephone number, the network access identifier is not subjected to portability ruling in force, and is individually managed by each operator (e.g. "123456789@domain.com")

### Usage

## [ConnectivityInsights](https://github.com/camaraproject/ConnectivityInsights)

### Description
The Connectivity Insights API allows an application developer to ask the network the likelihood that an application's networking requirements can be met for a given end user session.
Depending on the answer the network gives, the developer may decide to request a network boost (via the CAMARA QoD API) , and/or apply specific changes on the application side e.g. adjusting the resolution of the video stream upwards or downwards.

### Scope
{: .note }
We could qualify the API as e.g. Informative - it doesn't have any direct interaction with the network

### Usage
1. Create an Application Profile using the Connectivity Insights **_application-profiles_ API**. It retruns an **_applicationProfileId_**
2. Request with a **POST _check-network-quality_**, passing:
    - the **_applicationProfileId_** obtained in step 1
    - the address/port of an application server, and
    - at least one device identifier.
3. Response: The network will indicate whether it can or cannot meet the application requirements.
Optional: use the **_connectivity-insights-subscriptions_ API** to receive notifications of network quality.

#### Application Profiles
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

#### Checking network quality
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
#### Subscription to notifications
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

## [QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

### Description

### Scope

### Usage

## [DedicatedNetworks](https://github.com/camaraproject/DedicatedNetworks)

### Description

### Scope

### Usage




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

### [QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

#### Scope
- Service APIs for “Quality on Demand” (see APIBacklog.md)
- It provides the API consumer with the ability to:
  - set quality for a flow within an access network connections (e.g. mobile device connection or fixed access between a home gateway and the service providers gateway router)
    - Session mode, for a specific duration
    - Provision mode, indefinitely for each time the device connects to the same access network
  - get notification if the network cannot fulfill
