---
layout: default
title: Handover for Multicast
parent: 5G Multicast Broadcast Services (MBS)
has_children: false
nav_order: 0
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Multicast Broadcast Services**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Aspects on Handover for MBS Multicast Services

## Handover between 2 cells supporting Multicast
Mobility procedures described in 3GPP TS 38.300 for multicast reception allow the UE to continue receiving multicast service(s) via PTM or PTP in a new cell after handover.

### Procedure
* Source gNB transfers to target gNB information about the MBS multicast sessions the UE has joined (UE context information).

* Source gNB may propose data forwarding for some MRBs to minimize data loss and may exchange the corresponding MRB PDCP Sequence Number with the target gNB during the handover preparation:
  * Lossless handover for multicast service is supported for the handover between MBS supporting cells if the UE is configured with PTP RLC AM entity in target cell MRB of a UE.
  * The network has to ensure DL PDCP COUNT value synchronization and continuity between the source cell and the target cell.
 
* During handover execution, the MBS configuration decided at target gNB is sent to the UE via the source gNB within an RRC container (3GPP TS 38.331).
When the UE connects to the target gNB, the target gNB sends an indication that it is an MBS-supporting node to the SMF in the Path Switch Request message (Xn handover) or Handover Request Acknowledge message (NG handover). 

* Upon successful handover completion, the source gNB may trigger the release of the MBS user plane resources towards the 5GC using the NGAP Distribution Release procedure for any multicast session for which there is no remaining 
joined UE in the gNB.

## Handover between 1 cell supporting Multicast and 1 cell not supporting Multicast
Mobility procedures described in 3GPP TS 38.300 for multicast reception allow the UE to continue receiving multicast service(s) via PTM or PTP in a new cell after handover.

### Procedure
* Target gNB sets up PDU Session Resources mapped to the MBS multicast session.
* The 5GC infers from the absence of an "MBS-support" indication from gNB in the Path Switch Request message (Xn handover) or Handover Request Acknowledge message (NG handover) that MBS multicast data packets delivery has to be switched to 5GC individual MBS traffic delivery (3GPP TS 23.247). 
* For mobility from MBS non-supporting cell to MBS-supporting cell, the existing Xn/NG handover procedures apply:
  * 5GC detecs that MBS multicast data packets delivery can be switched from 5GC Individual MBS traffic delivery to 5GC Shared MBS traffic delivery.
  * After Xn handover, the SMF triggers switching MBS multicast data packets delivery from 5GC Individual to 5GC Shared MBS traffic delivery by providing MBS Session IDs joined by the UE to the target gNB by means of the PDU Session Resource Modification procedure.
  * For NG handover, the SMF provides the MBS Session IDs joined by the UE to the target gNB by means of NGAP Handover Request.

## Handover between 1 cell not supporting Multicast and 1 cell supporting Multicast
Mobility procedures described in 3GPP TS 38.300 for multicast reception allow the UE to continue receiving multicast service(s) via PTM or PTP in a new cell after handover.

### Procedure
* Mobility from a multicast-supporting cell to a multicast non-supporting cell can be achieved by switching the MRB to a DRB in the source gNB before a handover.
