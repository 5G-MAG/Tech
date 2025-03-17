---
layout: default
title: MBS Service and System Aspects
parent: 5G Multicast Broadcast Services (MBS)
has_children: false
nav_order: 1
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Multicast Broadcast Services**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# MBS Service and System Aspects

## MBS communication services (TS 23.247)
TS 23.247 defines two new logical communication services:
*	**Multicast communication service**: A 5GS communication service in which the same service and the same specific content data are provided simultaneously to a dedicated set of UEs i.e. not all UEs in the coverage of the MBS service area are authorised to receive the data.
*	**Broadcast communication service**: A 5GS communication service in which the same service and the same specific content data are provided simultaneously to all UEs in a geographical area i.e. all compatible UEs in the coverage area are authorised to receive the data. The content provider and network may not be aware whether authorised UEs are actually receiving the data being delivered.

## MBS sessions (TS 23.247)
TS 23.247  defines MBS sessions as follows:
*	**MBS session**: A multicast or broadcast session.
*	**Broadcast MBS session**: An MBS session to deliver a broadcast communication service. A broadcast MBS session is characterised by the content to send and the geographical area over which to distribute it.
*	**Multicast MBS session**: An MBS session to deliver a multicast communication service. A multicast MBS session is characterised by the content to send, the list of UEs that may receive the service and optionally by a geographical area over which to distribute it.
Broadcast and multicast MBS sessions are time-bound. Their life-cycles are specified in clauses 4.2 and 4.3 of TS 23.247.
The geographical areas for which the multicast and broadcast MBS sessions are available is determined by the coverage area of the sites/sectors from which the broadcast service is transmitted. Refer to TS xxxxxx for more detail.

## MBS traffic delivery methods (TS 23.247)
![image](https://github.com/user-attachments/assets/25f15af6-49b1-4c75-b567-ce225fa3bc96)
![image](https://github.com/user-attachments/assets/5e09d1a7-cb89-4f81-9d31-fac6d01e9a73)
Caption: MBS traffic delivery methods adapted from TS 23.247 Figure 4.1 1. Left multicast, right broadcast 

Multicast–broadcast Protocol Data Units, referred to as MBS packets, are supplied to the MB UPF by upstream Network Functions and from there conveyed across the 5G Core Network (CN) using one of two different MBS traffic delivery methods:

* **5GC shared MBS traffic delivery method**: 5G CN receives a single copy of MBS data packets and delivers a single copy of those MBS data packets to all relevant  RAN nodes.
  * This method must be applied for broadcast MBS sessions.
  * This method may be applied to multicast MBS sessions.
  * MBS packet is forwarded by the MBUPF directly to the relevant NGRAN nodes at their N3mb reference point via a shared GTP tunnel.
  * Each MBS Session establishes its own separate set of shared tunnels as required – tunnels are not shared across different MBS sessions.
*	**5GC individual MBS traffic delivery method**: the 5G CN receives a single copy of MBS data packets and delivers separate copies of those MBS data packets to relevant RAN nodes via per-UE Protocol Data Unit (PDU) sessions. For this traffic delivery method each UE associated with a multicast session requires its own, dedicated PDU session.
  * This method is only applied to multicast MBS sessions.
  * Because an MNO network may contain an arbitrary mix of MBS-capable and MBS-incapable gNodeBs, the same MBS packet (originating from a multicast MBS session) may be conveyed to MBS-capable gNodeBs using the shared MBS traffic delivery method, and to MBS-incapable gNodeBs via one or more PDU Sessions using the individual MBS traffic delivery method.
  * MBS packets are forwarded by the MB-UPF to the UPF at reference point N19mb where they are delivered to the NG-RAN in a conventional PDU Session in a GTP tunnel at existing reference point N3, and thence to the target UE at reference point Uu. In this scenario, a separate PDU Session is required for each subscribed UE and the MBUPF is responsible for performing the necessary packet replication at this fan-out point.
