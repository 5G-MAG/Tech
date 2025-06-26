---
layout: default
title: Connectivity Insights
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: Connectivity Insights

## Description

With CAMARA Connectivity Insights, application developers gain essential visibility into network quality. This enables them to make informed decisions that enhance the end-user experience for their applications.

* The **Connectivity Insights API** allows an application developer to ask the network the likelihood that an application's networking requirements can be met for a given end user session. This information helps a developer ensure their end users are able to get the best experience while using the application over their current network. Depending on the answer the network gives, the developer may decide to request a network boost (via the CAMARA QoD API) , and/or apply specific changes on the application side e.g. adjusting the resolution of the video stream upwards or downwards.

* The **Connectivity Insights Subscriptions API** allows creating and managing a subscription to receive periodic connectivity insights.

* The **Application Profiles API** allows creating and managing a subscription to receive periodic connectivity insights.

Information: [https://github.com/camaraproject/ConnectivityInsights](https://github.com/camaraproject/ConnectivityInsights)

The API definitions can be obtained here: [https://github.com/camaraproject/ConnectivityInsights/tree/main/code/API_definitions](https://github.com/camaraproject/ConnectivityInsights/tree/main/code/API_definitions)

## Overall usage
The overall usage would follow this sequence:

  1. Create an application profile using the Connectivity Insights **application-profiles** API
  2. Request: **POST check-network-quality**, passing the **applicationProfileId** obtained in step 1, the address/port of an application server, and at least one device identifier.
  3. Response: The network will indicate whether it can or cannot meet the application requirements.
Optional: use the **connectivity-insights-subscriptions** API to receive notifications of network quality.

## Application Profiles API Usage

### Create a profile which represent the network demands of an application
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

### Update the profile
With **PATCH /application-profiles/{applicationProfileId}**

### Obtain an existing application profile
With **GET /application-profiles/{applicationProfileId}**

### Delete an existing application profile
With **DELETE /application-profiles/{applicationProfileId}**

## Connectivity Insights API Usage

### Obtain information about network quality
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

## Connectivity Insights Subscriptions API Usage

### Create a subcription for a device
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

### Obtain a list of event subscription details
With **GET /subscriptions**

### Obtain a subscription based on the provided ID
With **GET /subscriptions/{subscriptionId}**

### Delete a subscription based on the provided ID
With **DELETE /subscriptions/{subscriptionId}**
