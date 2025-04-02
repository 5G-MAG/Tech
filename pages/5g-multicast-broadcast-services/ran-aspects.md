---
layout: default
title: MBS RAN Aspects
parent: 5G Multicast Broadcast Services (MBS)
has_children: false
nav_order: 2
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Multicast Broadcast Services**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# MBS RAN Aspects

## RAN traffic delivery methods (TS 38.300/331 when complete)
On receiving an MBS packet from the 5GC via the shared MBS traffic delivery method, the gNodeB can choose between two different RAN delivery methods, as described below.

### Point-to-Multipoint (PTM) RAN delivery method
The PTM RAN delivery method is used only for MBS packets arriving at the gNodeB via the 5GC shared MBS traffic delivery method. gNodeBs then deliver a single copy of the MBS data packets over the radio interface to multiple UEs. The radio interface may use either delivery mode 1 (multicast) or delivery mode 2 (broadcast).
The PTM RAN delivery method is always used to deliver the MBS packets of a Broadcast MBS Session.
The PTM RAN delivery method may be used to deliver the MBS packets of a Multicast MBS Session. In some cases, however, the gNodeB may opt to use the PTP delivery method (see below)

### Point-to-Point (PTP) RAN delivery method
The PTP RAN delivery method may be used for MBS packets arriving at the gNodeB via either the 5GC shared MBS traffic delivery method or the 5GC individual MBS traffic delivery method. gNodeBs then deliver separate copies of the MBS data packets over the radio interface to individual UEs.
The PTP RAN delivery method is always used for conventional PDU Sessions carrying packets from a unicast session.
The PTP RAN delivery method is always used in combination with the 5GC individual MBS traffic delivery method.
The PTP RAN delivery method may be used in combination with the 5GC shared MBS traffic delivery method – for example in cases where specific UEs require more robust Modulation Coding Schemes (MCS) to achieve reliable reception, or if the number of UEs within a given gNodeB subscribing to the Multicast MBS Session is below a certain threshold. In such cases, the gNodeB replicates MBS packets into UE-specific Radio Resource Blocks.
The PTP RAN delivery method is not used for broadcast MBS sessions.

## RAN delivery modes
5G-NR MBS compatible gNodeBs support three different delivery modes at Layer 2: delivery mode 1 (multicast), delivery mode 2 (broadcast), and the unicast delivery mode, where the latter is italicised as it does not reflect a defined 3GPP’s term but is used in this document to describe the ‘default unicast’ delivery mode, absent 5G-NR MBS. 

### Unicast delivery mode

{: .note }
Is unicast delivery mode a term, which is used in 3GPP specifications? Could it be enough with point-to-point RAN delivery method or point-to-point delivery method. The word unicast can easily be confused with IP Unicast.

gNodeBs always use the unicast delivery mode for the point-to-point RAN delivery method. This includes the delivery of:
*	Unicast packets arriving at reference point N3 from a PDU Session.
*	MBS packets from a Multicast MBS Session arriving at reference point N3 in a PDU Session corresponding to 5GC individual MBS traffic delivery.
*	MBS packets from a Multicast MBS Session arriving at reference point N3mb using the 5GC shared MBS traffic delivery method when the gNodeB has chosen to use the point-to-point RAN delivery method.
The unicast delivery mode cannot be used for broadcast communication services.
Payloads delivered over the unicast delivery method are intended for specific UEs – they are not intended to be decoded by more than one UE. Payloads delivered over the unicast delivery method are therefore scrambled using a key known only to the gNodeB and the target UE. More specifically, the NG-RAN uses a UE-specific PDCCH with a CRC scrambled with a UE-specific RNTI (e.g., C-RNTI) to schedule a UE-specific PDSCH which is scrambled with the same UE-specific RNTI). 
Unicast can only be received by UEs in RRC_Connected state.

### Delivery mode 1 (Multicast)
A gNodeB uses delivery mode 1 for a Multicast MBS Session when it has chosen to use the PTM RAN delivery method.
Delivery mode 1 supports HARQ feedback, retransmissions, and basic mobility with service continuity. Support of these features allows multicast to offer a similar QoS compared with unicast and may therefore be considered to offer a high quality of service i.e. high reliability and low latency
Delivery mode 1 payloads are intended for multiple UEs served by a particular gNodeB. The payload is scrambled using a shared key known to the gNodeB and the UEs that have subscribed to the Multicast Session. The scrambling key is shared with each UE as part of its control plane interaction with the gNodeB when it subscribes to the MBS Session.
Delivery mode 1 can only be received by compatible UEs in RRC_Connected state.
Delivery mode 1 is not used for a broadcast MBS session. 

{: .note } Editor's note: Check the options for feedback (NACK,...)

### Delivery mode 2 (Broadcast)
gNodeBs always uses this transmission mode for a Broadcast MBS Session (which always uses the point-to-multipoint RAN delivery method).
Delivery mode 2 does not support HARQ feedback nor retransmissions. Service continuity, as a UE moves from one cell to another, is supported (the UE can read the MCCH/MTCH from neighbour cells), however lossless handover is not supported. Service breaks may therefore occur as the UE moves from one cell to another. Broadcast may therefore be considered to offer a lower quality of service than delivery mode 1 (Multicast). 
Delivery Mode 2 payloads are intended for any UE served by a particular gNodeB. The payload is scrambled using a shared key known to the gNodeB. The scrambling key is broadcast in the XXXX channel to all listening UEs.
Delivery mode 2 can be received by UEs in all RRC states (RRC_Connected, RRC_Idle and RRC_Inactive).
