---
layout: default
title: Mobility MBS Multicast over NTN
parent: Non-Terrestrial Networks
nav_order: 1
has_children: false
---

{: .warning } This documentation is currently **under development and subject to change**. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Aspects on Mobility for MBS Multicast over NTN

The scenarios under study are the following:
* **Scenario 1**: Support of Lossless Handover for MBS Multicast Service for a group of users under the coverage of a satellite when mobility is triggered by the satellite moving.
* **Scenario 2**: Support of Lossless Handover for MBS Multicast Service for a group of users under the coverage of a satellite when mobility is triggered by at least on user within the group of users or the entire group of users.

## Scenario 1
A group of users is consuming content provided via an MBS Multicast Service within the coverage area of a satellite (a beam). Due to satellite motion, coverage of the existing satellite/beam will be lost and the group of users will be illuminated by another satellite/beam. During this process handover delays should be minimized while the entire group of users is transfered to another satellite.

### Discussion
Although PTM to PTM mobility is supported by MBS Multicast Services as explained in [Aspects on Mobility for MBS Multicast Services](../5g-multicast-broadcast-services/Mobility_MBS_Multicast.html), mobility in this case is triggered by the satellite motion, not by the user. In addition, the PTM traffic delivery on the entire cell has to be transfered to another cell.

One possibility would entail transfering each user first to PTP, then execute NTN mobility procedures and bring users back to PTM on the new cell. However this is not resource-efficient. The OAM can predict satellite movement and therefore can predict in advance whenever to start illuminating the beam of the target satellite. Based on these knowledges, the network can trigger Conditional Handover for the Group of Multicast Users and force switching their Multicast session on the PTP leg during the handover preparation and handover execution to ensure lossless handover for Multicast UEs.

TBC
