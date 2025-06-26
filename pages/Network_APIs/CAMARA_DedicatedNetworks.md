---
layout: default
title: CAMARA Dedicated Networks
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 3
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: Dedicated Networks

## Description

The Dedicated Network APIs are a set of APIs to provide functionalities for reserving network connectivity resources (e.g. throughput) potentially with an SLA and for time and location (service area) limits, discover supported and prepared network capabilities/resources (e.g. existing slices to connect to), manage device access, offering insights based on network profiles and resource states.

* The **Dedicated Network API** is invoked for reservation and lifecycle management of network connectivity resources for dedicated use. A Dedicated Network is a logical resource and is used to embody the reservation of network connectivity resources in the physical network. Initiating a new reservation request using this API results in a new Dedicated Network resource being created. The Dedicated Network undergoes various lifecycle States including REQUESTED, RESERVED, ACTIVATED and TERMINATED. Reservation of resources occurs based on the selected **Network Profile**, **duration** when the reservation is needed (Service Time) and **geographical areas** where the service is needed (Service Area).

* The **Dedicated Network Profiles API** is invoked for discovery of predefined set of network capabilities and performance characteristics. A Network Profile represents a predefined set of network capabilities and performance characteristics that can be applied when creating dedicated networks. Each profile represents a validated, supported configuration that has been pre-approved in the terms and conditions between the API Provider and API Consumer.

* The **Dedicated Network Accesses API** is invoked to managing access to the Dedicated Network, i.e., controlling which devices may benefit from the reserved resources and capabilities. A Device Access represents the permission for a specific device to use a Dedicated Network's reserved connectivity resources. The usage of resources can be tailored to each device within the constraints of the applicable Network Profile.

Information: [https://github.com/camaraproject/DedicatedNetworks](https://github.com/camaraproject/DedicatedNetworks)
The API definitions can be obtained here: 

## Dedicated Network API Usage

This API allows for requesting a Dedicated Network, which provides a set of capabilities and connectivity performance targets. The Dedicated Network may be requested for a particular geographical location and at a particular time window. Depending on the requested start time for the dedicated network, the network may first enter a reserved state.

### Request the creation of a dedicated network
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

### Obtain a list of dedicated networks
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

### Obtain the current information about a dedicated network
With **GET /networks/{networkId}**

### Delete a dedicated network
With **DELETE /networks/{networkId}**

## Dedicated Network Profiles API Usage

This API allows for discovering available network profiles, which are offered by the network provider to be used in conjunction of the Dedicated Network API. Network profiles describe the capabilities and performance targets of a dedicated network. A Network Profile represents a predefined set of network capabilities and performance characteristics that can be applied when creating a Network. It enables API Consumers to understand the capabilities they can expect when using the reserved network connectivity resources. A Network Profile is a validated, supported configuration that has been pre-approved between the API Provider and API Consumer.

A Network Profile contains information about:
- the maximum number of devices allowed,
- the aggregated throughput to be provided,
- a set of allowed QoS Profiles that devices can use when having access to the Dedicated Network.

### Obtain list of available dedicated network profiles
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

### Obtain list of available dedicated network profiles
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

### Obtain a dedicated network profiles
With **GET /profiles/{profileId}**

## Dedicated Network Accesses API Usage
This API allows for requesting network access for devices. A device is identified by the CAMARA device object, containing either an MSIDSN or a Network Access Identifier.
A Device Access represents the permission for a specific device to use a Dedicated Network's reserved connectivity resources. Only devices for which a Device Access resource has been created can use the connectivity resources allocated for that network. The usage of resources can be tailored to each device within the constraints of the applicable Network Profile.

### Create a device access to a dedicated network with given configuration
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

### Obtain a list of device accesses to dedicated networks
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

### Obtain a device access to the dedicated network
With **GET /accesses/{accessId}**

### Delete a device access to the dedicated network
With **DELETE /accesses/{accessId}**
