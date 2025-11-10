---
layout: default
title: CAMARA Application Profiles
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 1
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: Application Profiles API

## Description

The application profiles allow developers to specify all relevant information about their application for both network and compute resource requirements, supporting CAMARA APIs and network decision making.

Used in the of the [Connectivity Insights APIs](./CAMARA_ConnectivityInsights.html).

This API enables defining, reading, and managing application requirements,including:
* Network quality thresholds (latency, jitter, loss, throughput)
* Compute resource thresholds (CPU, GPU, memory, storage)

Information: [https://github.com/camaraproject/ApplicationProfiles/](https://github.com/camaraproject/ApplicationProfiles/)

The API definitions can be obtained here: [https://github.com/camaraproject/ApplicationProfiles/tree/main/code/API_definitions](https://github.com/camaraproject/ApplicationProfiles/tree/main/code/API_definitions)

## Relation of APIs
### Application Profiles API
  * **POST /application-profiles** with the request body containing user-defined network quality thresholds. Used to define network monitoring intents for optimal end user application experience. Response is an `applicationProfileId`.
  * **PATCH /application-profiles/{applicationProfileId}** - Update the complete set of network quality thresholds for an application with the new set of thresholds to ensure good end user experience
  * **GET /application-profiles/{applicationProfileId}** - Read an Application Profile
  * **DELETE /application-profiles/{applicationProfileId}** - Delete an application profile

### Parameters

* Network Quality Thresholds
  * `packetDelayBudget` - the maximum allowable one-way latency between the customer's device and the gateway from the operator's network to other networks. The end-to-end or round trip latency will be about two times this value plus the latency not controlled by the operator
  * `targetMinDownstreamRate` - the target minimum downstream rate.
  * `targetMinUpstreamRate` - the target minimum upstream rate
  * `packetLossErrorRate` - the exponential power of the allowable error loss rate 10^(-N). For 5G network the 3GPP specification TS 23.203 defines the packet error loss rate QCI attribute.
  * `jitter`  - this requirement aims to limit the maximum variation in round-trip packet delay for the 99th percentile of traffic, following ITU Y.1540 standards. It considers only acknowledged packets in a session, which are packets that receive a confirmation of receipt from the recipient (e.g., using TCP).

* Compute Resources
  * `targetMinCPU`
  * `targetMinMemory`
  * `gpuVendorType`
  * `gpuModelName`
  * `targetMinGPU`
  * `targetMinGPUMemory`
  * `targetMinEphemeralStorage`
  * `targetMinPersistentStorage`

---

## Workflow for a media application creating an Application Profile

### Step 1: Creation of Application Profile
* Create an application profile using the **Application Profiles API**.

### Further steps
* The Application Profile created can be used by other APIs.

## 5G-MAG's Self-Assessment

The APIs is likely to be invoked well before the actual use of the network with the required values of performance and compute resources.
Once an `applicationProfileId` is obtained, it can be used by other APIs.

Potential improvements:
- the list of parameters and unit/accuracy should be checked for typical media applications.

---

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
      "unit": "Bps"
    },
    "targetMinUpstreamRate": {
      "value": 10,
      "unit": "Bps"
    },
    "packetLossErrorRate": 3,
    "jitter": {
      "value": 12,
      "unit": "Minutes"
    }
  },
  "computeResources": {
    "targetMinCPU": 0.5,
    "targetMinMemory": {
      "value": 10,
      "unit": "Kb"
    },
    "gpuVendorType": "Nvidia",
    "gpuModelName": "string",
    "targetMinGPU": 1,
    "targetMinGPUMemory": {
      "value": 10,
      "unit": "Kb"
    },
    "targetMinEphemeralStorage": {
      "value": 10,
      "unit": "Kb"
    },
    "targetMinPersistentStorage": {
      "value": 10,
      "unit": "Kb"
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
