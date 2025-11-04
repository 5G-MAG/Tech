---
layout: default
title: MBS Broadcast over NTN
parent: Non-Terrestrial Networks
nav_order: 2
has_children: false
---

# Analysis - MBS Delivery Mode 2 (Broadcast) over NTN

Procedures for MBS Broadcast over NTN are those defined for MBS Broadcast in [Analysis MBS Broadcast - RAN Procedures](../5g-multicast-broadcast-services/Analysis_MBS_Broadcast_RAN.html)

{: .note } In threory SIB19 is designed for mobility and cell reselection, therefore the delivery of SIB19 would not be required for MBS Broadcast.

In addition, SIB27 is used to convey the Intended Service Area (ISA) for MBS within an NTN cell. 

### SIB 27 - Intended Service Area (ISA) for MBS Broadcast in NTN Cell

```
SIB27-r19 ::= SEQUENCE { 
 intendedServiceAreaList-r19 IntendedServiceAreaList-r19 OPTIONAL, -- Need R 
 lateNonCriticalExtension OCTET STRING OPTIONAL, 
 ... 
} 
IntendedServiceAreaList-r19 ::= SEQUENCE (SIZE (1..maxNrofMBS-Area-r19)) OF IntendedServiceAreaInfo-r19 
IntendedServiceAreaInfo-r19 ::= SEQUENCE { 
 intendedServiceAreaId-r19 MBS-IntendedAreaID-r19, 
 areaCoordinates-r19 CHOICE { 
 polygonArea-r19 OCTET STRING, 
 circleArea-r19 SEQUENCE { 
 center-r19 ReferenceLocation-r17, 
 radius-r19 INTEGER(0..65535) 
 } 
 } 
} 
MBS-IntendedAreaID-r19 ::= INTEGER (1..maxNrofMBS-Area-r19)
```
