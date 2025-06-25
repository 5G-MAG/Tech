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

We collect here information about the following 3GPP APIs
 - [Connectivity Insights APIs](#connectivityinsights)

----

## [xx](xx)

### Description

xx

* xx.

* xx

* xx

### Overall usage

### Application Profiles API Usage

#### Create a profile which represent the network demands of an application
With **POST /application-profiles**

```
```

Type of response: An **applicationProfileId**

```
```

Parameters:
  - "packet delay budget": the maximum allowable one-way latency between the customer's device and the gateway from the operator's network to other networks. The end-to-end or round trip latency will be about two times this value plus the latency not controlled by the operator
  - "targetMinDownstreamRate": This is the target minimum downstream rate.
  - "targetMinUpstreamRate": This is the target minimum upstream rate
  - "packetlossErrorRate": The exponential power of the allowable error loss rate 10^(-N). For 5G network the 3GPP specification TS 23.203 defines the packet error loss rate QCI attribute.
  - "jitter" requirement aims to limit the maximum variation in round-trip packet delay for the 99th percentile of traffic, following ITU Y.1540 standards. It considers only acknowledged packets in a session, which are packets that receive a confirmation of receipt from the recipient (e.g., using TCP).

#### Update the profile
With **PATCH /application-profiles/{applicationProfileId}**
