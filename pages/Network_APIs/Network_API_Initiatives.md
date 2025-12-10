---
layout: default
title: Network API Analysis
parent: Network APIs
nav_order: 3
has_children: true
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Network API Initiatives under analysis

This analysis contains information on:
* [**CAMARA APIs for Communication Quality Management**](#camara-apis-for-communication-quality-management)
* [**Details on the DEVICE object**](#details-on-the-device-object)
* [**Details on the APPLICATION SERVER**](#details-on-the-application-server)
* [**Relevant QoS parameters**](#relevant-qos-parameters)

## CAMARA APIs for Communication Quality Management

### Application Profiles API
* Analysis of [**Application Profiles**](./CAMARA_ApplicationProfiles.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/application-profiles/](https://camaraproject.org/application-profiles/) and [https://github.com/camaraproject/ApplicationProfiles](https://github.com/camaraproject/ApplicationProfiles)

### Connectivity Insights API
* Analysis of [**Connectivity Insights**](./CAMARA_ConnectivityInsights.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/connectivity-insights/](https://camaraproject.org/connectivity-insights/) and [https://github.com/camaraproject/ConnectivityInsights](https://github.com/camaraproject/ConnectivityInsights)

### Connectivity Insights Subscriptions API
* Analysis of [**Connectivity Insights Subscriptions**](./CAMARA_ConnectivityInsightsSubscriptions.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/connectivity-insights-subscriptions/](https://camaraproject.org/connectivity-insights-subscriptions/) and [https://github.com/camaraproject/ConnectivityInsights](https://github.com/camaraproject/ConnectivityInsights)

### Dedicated Networks API
* Analysis of [**Dedicated Networks**](./CAMARA_DedicatedNetworks.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/dedicated-networks/](https://camaraproject.org/dedicated-networks/) and [https://github.com/camaraproject/DedicatedNetworks](https://github.com/camaraproject/DedicatedNetworks)

### Network Slice Booking API
* Analysis of [**Network Slice Booking**](./CAMARA_NetworkSliceBooking.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/network-slice-booking/](https://camaraproject.org/network-slice-booking/) and [https://github.com/camaraproject/NetworkSliceBooking](https://github.com/camaraproject/NetworkSliceBooking)

### QoS Booking APIs 
* Analysis of [**QoS Booking**](./CAMARA_QoSBooking.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/qos-booking/](https://camaraproject.org/qos-booking/) and [https://github.com/camaraproject/QoSBooking](https://github.com/camaraproject/QoSBooking)

### QoS Booking and Assignment APIs 
* Analysis of [**QoS Booking and Assignment**](./CAMARA_QoSBookingAssignment.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/qos-booking-and-assignment/](https://camaraproject.org/qos-booking-and-assignment/) and [https://github.com/camaraproject/QoSBooking](https://github.com/camaraproject/QoSBooking)

### QoS Profiles API
* Analysis of [**QoS Profiles**](./CAMARA_QoSProfiles.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/qos-profiles/](https://camaraproject.org/qos-profiles/) and [https://github.com/camaraproject/QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

### QoS Provisioning API
* Analysis of [**QoS Provisioning**](./CAMARA_QoSProvisioning.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/qod-provisioning/](https://camaraproject.org/qod-provisioning/) and [https://github.com/camaraproject/QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

### Quality On Demand API
* Analysis of [**Quality On Demand**](./CAMARA_QualityonDemand.html) by 5G-MAG
* CAMARA Project: [https://camaraproject.org/quality-on-demand/](https://camaraproject.org/quality-on-demand/) and [https://github.com/camaraproject/QualityOnDemand](https://github.com/camaraproject/QualityOnDemand)

## Details on the `device` object
A device object in the sense of CAMARA APIs is defined as:

```
"device": {
    "phoneNumber": "+123456789",
    "networkAccessIdentifier": "123456789@domain.com",
    "ipv4Address": {
      "publicAddress": "203.0.113.0",
      "publicPort": 59765
    },
    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
  },
```

However, as indicated in the [Production and Contribution Scenarios](https://hub.5g-mag.com/Tech/pages/Network_APIs/Content_Production/Production_Contribution_Scenarios.html#media-connectivity-flows-single-device-connectivity), a device in the context of a Mobile Journalism or Media Production scenario may be:

* A single UE (e.g. a smartphone) equipped with a single SIM card (or eSIM) connected to the mobile network.
* A single device (e.g. a smartphone) equipped with 2 UEs each with 1 SIM card (or eSIM) connected to a different carrier of the same mobile network or different mobile networks.
* A device with multiple UEs (e.g. a cellular bonding backpack) equipment with multiple SIM cards each one connected to a different carrier of the same mobile network or connected to different mobile networks.

Identifying such as device by a telefone number may not be practical (or relevant) as the device is used exclusively for data.

## Details on the Application Server
A media application running in a device (as per the sense in the section above) may run different processes each one associated to a different Application Server IP:port address. For instance, an application for Mobile Journalism may be running uplink video towards an AS and receiving return video from a different IP:port. These two different media flows, though belonging to the same device, would require the allocation of different network resources and performance.

## Relevant QoS Parameters

### Application Profiles
* `packetDelayBudget`- the maximum allowable one-way latency between the customer's device and the gateway from the operator's network to other networks. The end-to-end or round trip latency will be about two times this value plus the latency not controlled by the operator
* `targetMinDownstreamRate` - the target minimum downstream rate.
* `targetMinUpstreamRate` - the target minimum upstream rate
* `packetLossErrorRate` - the exponential power of the allowable error loss rate 10^(-N). For 5G network the 3GPP specification TS 23.203 defines the packet error loss rate QCI attribute.
* `jitter`  - this requirement aims to limit the maximum variation in round-trip packet delay for the 99th percentile of traffic, following ITU Y.1540 standards. It considers only acknowledged packets in a session, which are packets that receive a confirmation of receipt from the recipient (e.g., using TCP).

### QoS Profiles
* `packetDelayBudget`- the maximum allowable one-way latency between the customer's device and the gateway from the operator's network to other networks. The end-to-end or round trip latency will be about two times this value plus the latency not controlled by the operator
* `targetMinDownstreamRate` - the target minimum downstream rate.
* `targetMinUpstreamRate` - the target minimum upstream rate
* `packetLossErrorRate` - the exponential power of the allowable error loss rate 10^(-N). For 5G network the 3GPP specification TS 23.203 defines the packet error loss rate QCI attribute.
* `jitter`  - this requirement aims to limit the maximum variation in round-trip packet delay for the 99th percentile of traffic, following ITU Y.1540 standards. It considers only acknowledged packets in a session, which are packets that receive a confirmation of receipt from the recipient (e.g., using TCP).
* `minDuration`
* `maxDuration`
* `priority`
* `l4sQueueType`

#### Network Slice QoS Profile
* `maxNumOfDevices`- is the maximum number of devices that can be connected to the slice
* `downStreamRatePerDevice` - is the maximum downstream rate allowed for each device connected to the slice. It indicates the individual device capability required for the slice.
* `upStreamRatePerDevice` - is the maximum upstream rate allowed for each device connected to the slice. It indicates the individual device capability required for the slice.
* `downStreamDelayBudget` - is the maximum allowable downlink packet transmission latency (millisecond). By limiting the delay, the network can provide an acceptable level of performance for various services, such as voice calls, video streaming, and data.
* `upStreamDelayBudget`  - is the maximum allowable uplink packet transmission latency (millisecond). By limiting the delay, the network can provide an acceptable level of performance for various services, such as voice calls, video streaming, and data.

## 3GPP APIs for Quality of Service

We collect here information about the following 3GPP APIs

### NEF
- [Nnef_AFSessionWithQoS]()
- [Nnef_ChargeableParty]()
- [Nnef_BDTPNegotiation]()

### PCF
- [Npcf_PolicyAuthorization]()
- [Npcf_BDTPolicyControl]()
