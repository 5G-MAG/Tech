---
layout: default
title: Explainer
parent: 5G Multicast Broadcast Services
has_children: false
nav_order: 0
---

<img src="../../assets/images/Banner_5MBS.png" /> 

# Explainer: Media distribution with 5G Multicast-Broadcast Services (MBS)
* 📑 A PDF version of this explainer is available here.
* 🚩 Latest version: April 2023

3GPP Release 17 brings Multicast–Broadcast Services (MBS) to the 5G System, based on 5G Core and New Radio. MBS allows the network to select the most suitable among point-to-multipoint (PTM) or point-to-point (PTP) delivery based on requirements set by either service providers or network operators and/or taking into account concurrent user demand.

## Multicast Services
A Multicast Service uses PTM and/or PTP delivery methods to transport traffic from a single source to User Equipment (UE) terminals within a multicast service area that have subscribed to the service. Multicast traffic is efficiently and reliably transported over the 5G core network to compatible base stations using the shared traffic delivery method. The individual traffic delivery method can serve multicast traffic to legacy base stations that do not support MBS. 

MBS-enabled base stations autonomously decide whether to use PTM or PTP delivery methods at the radio access network based on the number of concurrent subscriptions and the quality of the radio channel.

<figure>
  <img src="./images/figure_mbs_1.png" alt="" width="60%">
  <figcaption style="text-align: left; font-style: italic">To receive Multicast Services, UEs must first subscribe to a multicast group. Base stations 1 and 2 use the PTM delivery method to serve subscribed UEs within their reception footprints. Base station 2 additionally uses the PTP delivery method to serve UEs that require more robust delivery. Base station 3 (not supporting MBS) can deliver multicast packets via a conventional unicast PDU session unique to each subscribed UE.</figcaption>
</figure>

## Broadcast Services
A Broadcast Service uses only the PTM delivery method to transport traffic from a single source to multiple UEs within a broadcast service area. Any UE within the broadcast service area that has registered with the network can receive Broadcast Services. 

A single copy of the MBS traffic is efficiently transported over the 5G core network to each MBS-compatible base station in the service area using the shared traffic delivery method.

<figure>
  <img src="./images/figure_mbs_2.png" alt="" width="60%">
  <figcaption style="text-align: left; font-style: italic">A Broadcast Service is available to compatible UEs within the broadcast service area, always using the PTM delivery method.</figcaption>
</figure>

## What kinds of service could be offered with 5G MBS?
MBS supports the delivery of both operator and third-party media content. In particular, MBS User Services allow popular online television and radio services (e.g. live sport or national events) to be delivered efficiently to compatible equipment such as smartphones, smart TVs or car infotainment systems.
* Broadcast is suitable for localized services at the granularity of individual cells (e.g. services in venues, stadiums, exhibition centres).
* Multicast allows the efficient and scalable delivery of popular services while ensuring a similar quality of service (QoS) and reliability to that of unicast distribution. Quality of experience is independent of audience size and network congestion is mitigated. Multicast allows a group of UEs to receive services according to QoS requirements and/or prevailing channel conditions.

<figure>
  <img src="./images/figure_mbs_3.png" alt="" width="60%">
</figure>

## Additional characteristics
To minimize implementation impact and complexity, MBS reuses the existing (3GPP Release 15/16) radiolayer design for physical channels, reference signals, and sub-carrier spacings and cyclic prefixes.

### How is the coverage area of a service determined?
For both Multicast and Broadcast Services, individual cells may be added to or removed from the service
area. The Multicast Service is transmitted only in cells within the multicast service area in which there
are UEs that have joined an MBS session. Cells within the broadcast service area transmit the Broadcast
Service regardless of whether the service is requested or not.
For multicast, link adaptation selects the most appropriate modulation and coding scheme (MCS).
Beamforming is optimized for the UEs in the multicast group. For broadcast, each service is pre-assigned an
MCS, as there is no channel-state information feedback from UEs.
Single frequency network (SFN) operation is possible across sectors of the same base station for
multicast. For broadcast, SFNs can be implemented across base stations that are sufficiently close to each
other, transparent to UEs.

### How is reliability of reception managed?
For multicast, provision of UE feedback, support of retransmissions using PTP or PTM, link adaptation, and
beamforming, among other mechanisms, ensure reliability. For broadcast, services are delivered with no
guarantee of reception, however data repetition (slot-level) is possible for improved performance.

### How are mobility and service continuity managed?
For multicast, service continuity across cells is supported by handover between the base stations a UE
traverses. For broadcast, neighbour-cell information and cell-reselection mechanisms are available but may
not ensure lossless handover.

### Can MBS services be transmitted together with other types of traffic on the 5G network?
Mixed radio carriers can deliver multicast and/or broadcast services alongside other unicast data on the
same cell.

## Learn more...
A paper from [Qualcomm](https://ieeexplore.ieee.org/document/9772755) and a blog post from [Ericsson](https://www.ericsson.com/en/blog/2022/12/multicast-broadcast-group-communication) provide more details about MBS.
