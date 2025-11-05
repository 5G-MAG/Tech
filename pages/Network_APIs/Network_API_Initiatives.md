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

## CAMARA APIs for Communication Quality Management

### Information
- CAMARA Repositories in GitHub: [Link](https://github.com/orgs/camaraproject/repositories?q=sort%3Aname-asc)
- API Backlog: [Link](https://github.com/camaraproject/WorkingGroups/blob/main/APIBacklog/documentation/APIbacklog.md)
- Proposed new APIs: [Link](https://github.com/camaraproject/WorkingGroups/pulls)

### [Quality On Demand APIs](./CAMARA_QualityonDemand.html)
### [Application Profiles APIs](./CAMARA_ApplicationProfiles.html)
### [Dedicated Networks APIs](./CAMARA_DedicatedNetworks.html)
### [Connectivity Insights APIs](./CAMARA_ConnectivityInsights.html)

TBC
### [QoS Booking APIs](./CAMARA_QoSBooking.html)
### [Network Slice Booking APIs](./CAMARA_NetworkSliceBooking.html)

### Relevant QoS Parameters

#### Quality On Demand

Name | Description  
-- | --
**targetMinUpstreamRate** | This is the target minimum upload speed for the QoS profile. It represents the minimum rate that the network attempts to deliver. Please note that this is a target value—the network might not always be able to provide this rate under all conditions. It helps ensure that applications like video calls or live streaming perform consistently.
**maxUpstreamRate** | The maximum best effort data
**maxUpstreamBurstRate** |  When defined, this is the maximum upstream burst rate for the QoS profile, that will enable the network to burst data at a higher rate than the maxUpstreamRate for a period of time.
**targetMinDownstreamRate** |  This is the target maximum upload speed for the QoS profile. It represents the maximum rate that the network attempts to deliver. Please note that this is a target value—the network might not always be able to provide this rate under all conditions. It helps ensure that applications like video calls or live streaming perform consistently.
**maxDownstreamRate** | The maximum best effort rate
**maxDownstreamBurstRate** | When defined, this is the maximum downstream burst rate for the QoS profile, that will enable the network to burst data at a higher rate than the maxDownstreamRate for a period of time. This can result in improved user experience when there is additional network capacity. For instance, when a user is streaming a video, the network can burst data at a higher rate to fill the buffer, and then return to the maxUpstreamRate once the buffer is full.
**minDuration** | The shortest time period that this profile can be deployed.
**maxDuration** | The maximum time period that this profile can be deployed. Overall session duration must not exceed this value. This includes the initial requested duration plus any extensions.
**priority** | Priority levels allow efficient resource allocation and ensure optimal performance for various services in each technology, with the highest priority traffic receiving preferential treatment. The lower value the higher priority. Not all access networks use the same priority range, so this priority will be scaled to the access network's priority range.
**packetDelayBudget** | The packet delay budget is the maximum allowable one-way latency between the customer's device and the gateway from the operator's network to other networks. By limiting the delay, the network can provide an acceptable level of performance for various services, such as voice calls, video streaming, and data. The end-to-end or round trip latency will be about two times this value plus the latency not controlled by the operator
**jitter** | The jitter requirement aims to limit the maximum variation in round-trip packet delay for the 99th percentile of traffic, following ITU Y.1540 standards. It considers only acknowledged packets in a session, which are packets that receive a confirmation of receipt from the recipient (e.g., using TCP). This requirement helps maintain consistent latency, essential for real-time applications such as VoIP, video calls, and gaming.
**packetErrorLossRate** | This field specifies the acceptable level of data loss during transmission. The value is an exponent of 10, so a value of 3 means that up to 10⁻³, or 0.1%, of the data packets may be lost. This setting is part of a broader system that categorizes different types of network traffic (like phone calls, video streams, or data transfers) to ensure they perform reliably on the network.

#### Quality On Demand - Experimental parameters - L4S

**NOTE**: l4sQueueType is experimental and could change or be removed in a future release.
Specifies the type of queue for L4S (Low Latency, Low Loss, Scalable Throughput) traffic management. L4S is an advanced queue management approach designed to provide ultra-low latency and high throughput for internet traffic, particularly beneficial for interactive applications such as gaming, video conferencing, and virtual reality. For more details, refer to the [L4S standard](https://datatracker.ietf.org/doc/rfc9330/)
        
**NOTE**: serviceClass is experimental and could change or be removed in a future release.
The name of a Service Class, representing a QoS Profile designed to provide optimized behavior for a specific application type. While DSCP values are commonly associated with Service Classes, their use may vary across network segments and may not be applied throughout the entire end-to-end QoS session. This aligns with the serviceClass concept used in HomeDevicesQoQ for consistent terminology. Service classes define specific QoS behaviors that map to DSCP (Differentiated Services Code Point) values or Microsoft QoS traffic types. The supported mappings are:
- 1. Values aligned with the [RFC4594](https://datatracker.ietf.org/doc/html/rfc4594) guidelines for differentiated traffic classes.
- 2. Microsoft [QOS_TRAFFIC_TYPE](https://learn.microsoft.com/en-us/windows/win32/api/qos2/ne-qos2-qos_traffic_type) values for Windows developers.

#### QoS Booking APIs

Makes use of the QoS Profiles retrieved by the QoS Profiles API (part of Quality on Demand APIs).

#### Network Slice Booking

Name | Description  
-- | --
**MaxNumofTerminals** | 
**DLThroughputPerTerminal** | 
**ULThroughputPerTerminal** | 
**DLLatency** | DLLatency is an attribute specifies the required DL packet transmission latency (millisecond) through the 5G network.
**ULLatency** | ULLatency is an attribute specifies the required UL packet transmission latency (millisecond) through the 5G network.

#### Dedicated Networks

Name | Description  
-- | --
**maxNumberOfDevices** | 
**aggregatedUlThroughput** | 
**aggregatedDlThroughput** | 
**DLLatency** | DLLatency is an attribute specifies the required DL packet transmission latency (millisecond) through the 5G network.
**ULLatency** | ULLatency is an attribute specifies the required UL packet transmission latency (millisecond) through the 5G network.

#### Connectivity Insights

Name | Description  
-- | --
**packetDelayBudget** | the maximum allowable one-way latency between the customer's device and the gateway from the operator's network to other networks. The end-to-end or round trip latency will be about two times this value plus the latency not controlled by the operator
**targetMinDownstreamRate** | This is the target minimum downstream rate.
**targetMinUpstreamRate** | This is the target minimum upstream rate.
**packetlossErrorRate** | The exponential power of the allowable error loss rate 10^(-N). For 5G network the 3GPP specification TS 23.203 defines the packet error loss rate QCI attribute.
**jitter** | Aims to limit the maximum variation in round-trip packet delay for the 99th percentile of traffic, following ITU Y.1540 standards. It considers only acknowledged packets in a session, which are packets that receive a confirmation of receipt from the recipient (e.g., using TCP).
**signalStrength** | rough indication of the end user device radio signal conditions
**connectivityType** | the access technology connecting the user device to the operator network

## 3GPP APIs for Quality of Service

We collect here information about the following 3GPP APIs

### NEF
- [Nnef_AFSessionWithQoS]()
- [Nnef_ChargeableParty]()
- [Nnef_BDTPNegotiation]()

### PCF
- [Npcf_PolicyAuthorization]()
- [Npcf_BDTPolicyControl]()
