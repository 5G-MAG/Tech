---
layout: default
title: CAMARA QoS Provisioning
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 8
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# CAMARA: QoS Provisioning API

## Description

The “Quality of Service (QoS) Provisioning” API offers a programmable interface for developers to request the assignment of a certain Quality of Service (QoS) profile to a specific device, indefinitely. This API sets up the configuration in the network so that the requested QoS profile is applied to the specified device whenever it is connected to the network, until the provisioning is deleted.

Information: [https://camaraproject.org/qod-provisioning/](https://camaraproject.org/qod-provisioning/) and [https://github.com/camaraproject/QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

The API definitions can be obtained here: [https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions](https://github.com/camaraproject/QualityOnDemand/tree/main/code/API_definitions)

## Relation of APIs

### QoS Provisioning API
  * **POST /qos-assignments** with the request body including a `device` object and `qosProfile`, this request will assign a QoS profile to a device. The response includes an `assignmentId`.
    * Dependency: Requires `qosProfiles` which can be retrieved from a previous call to the [**QoS Profiles API**](./CAMARA_QoSProfiles.html).
  * **GET /qos-assignments/{assignmentId}** - Querying for details about the QoS profile assignment
  * **DELETE /qos-assignments/{assignmentId}** - Revokes the assignment of a QoS profile to a device performed by a previous assignment operation.
  * **POST /retrieve-qos-assignment** with the request body including the `device` object, this request will return information about the QoS profile assignment for the device with an `assignmentId`.

---

## Workflow: Media application using the QoS Provisioning API to assign a QoS profile to a device

A user of a media application would like to request the assignment of a QoS Profile to a device. An example figure is shown using the QoS Provisioning in the context of Quality on Demand. The following steps are executed:

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

---

## 5G-MAG's Self-Assessment

This API would allow attaching a QoS Profile to a device any time it is connected to the network.
There is an issue as it is not possible to assign a different device to the existing QoS assignment. If a device would need to be replaced during operation, the existing QoS assignment would have to be deleted and a new assignment created. While doing so there is no guarantee that such new assignment is possible.

Potential improvements:
- Ability to update the device to which the QoS Profile applies.
- There is no information about the location or service area.
- Understanding opportunities to  in terms of duration and location/area would be useful as the user may be able to move and find a better coverage spot rather than being denied the establishment of QoS at the time and location in which it is requested.

---

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
