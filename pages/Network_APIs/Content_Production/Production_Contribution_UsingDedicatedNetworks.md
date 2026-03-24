---
layout: default
title: Dedicated Networks
parent: Network APIs
grand_parent: Content Production & Contribution
nav_order: 0
has_children: false
---

<img src="../../../assets/images/Banner_NetworkAPIs.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Using CAMARA APIs: Dedicated Networks for Content Production & Contribution

Find more information about [**Dedicated Networks API**](../CAMARA_DedicatedNetworks.html).

A user of a media application would like to request a Dedicated Network, with a set of capabilities and connectivity performance targets. The resut is for a particular geographical location and at a particular time window. The following steps are executed:

## Architecture

<figure>
  <img src="./images/figure_dedicatednetworks.png" width="80%">
</figure>

## Workflow

<figure>
  <img src="./images/DedicatedNetworks_WF_1.png" width="80%">
</figure>

### Step 0: Pre-conditions
* qosProfiles have already been defined and made available by the network operator. This is related to the [**QoS Profiles API**](./CAMARA_QosProfiles.html).
* Network Profiles with the allowed number of devices which can be server concurrently together with the aggregated UL and DL throughput have been defined and made available by the network operator

### Step 1: Discover Network Profiles available
* **GET /profiles** to obtain a list of dedicated network profiles with the corresponding `id`.

### Step 2: Create a Dedicated Network
* **POST /networks** passing the Network Profile `profileId` from Step 1, `serviceTime` start and end and `serviceArea`.

### Step 3: Attach a Device to a Dedicated Network
* **POST /accesses** passing the Network Profile `networkId` from Step 2, a `device` object, and `qosProfile`.

### Step 4: During operation, delete a device access and attach a new device to a dedicated network or the same device to a different dedicated network
**DELETE /accesses/{accessId}** and **POST /accesses** should be used to detach or attach devices to a different dedicated network

## 5G-MAG's Self-Assessment

The Profiles and Networks APIs are to be invoked before the actual usage of the network to ensure that the requested capabilities are "reserved" for the specific area and time window.
During the event devices will have access to the Dedicated Network and should be allocated or de-allocated depending on the actual requirements.
This API is certainly adequate for a simple use case of 1 device requesting connectivity (MoJo) or multiple devices taking part in a Media Production setup.

What is the meaning of `maxNumberOfDevices`? An ideal situation would be to bring different devices to an event (including for backup) which are candidates to be assigned to a dedicated network. During operation only a maximum amount of devices can concurrently connect to the network and allocated resources accoding to the network profile.

One of the most interesting features in this API is the ability to define and create the network profile and later on attach/detach a device. This adds flexibility and avoids losing the dedicated resources when revoking a device.

Potential improvements:
- there is a dependency with qosProfiles and Network Profiles, which need to be present before being able to invoke Dedicated Networks. This is not an issue related to this API but worth considering as it would be useful if such profiles could be created/requested by the user and accepted by the network operator, rather than requiring another process.

---

