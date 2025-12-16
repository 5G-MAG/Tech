---
layout: default
title: Advanced Media Delivery
parent: 5G Media Streaming
has_children: false
nav_order: 1
---

<img src="../../assets/images/Banner_5GMS.png" /> 

# Advanced Media Delivery - Overview

## Common Media Client Data (CMCD)

* Metrics Reporting Provisining API via M1 defined in TS 26.510, 8.11, with `scheme` property defined in TS 26.512, 7.8. Service Access Information provided to Media Session Handler via M5.
* In-band client reporting on M4 (Media Stream Handler - Application Server) defined in TS 26.512, 10.5
* Client data reporting on M3 (Application Server - Application Function) defined in TS 26.512, 11.4.3
* Inband client reporting in DASH, defined in TS 26.512, Annex G.5

### Alternatives
* Configuration of Reporting via Service URL defined in TS 26.512, 12.4
* Configurations and settings API for Media Player via M7d (5GMSd-Aware Application) and M11d (Media Session Handler) defined in clause 13.2.4 of TS 26.512

### Event exposure to NWDAF or Event Consumer AF
* Event exposure on R5/R6 defined in clause 18.3.3 of TS 26.512

## Coded Multisource Media Format (CMMF)
