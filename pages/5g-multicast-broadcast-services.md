---
layout: default
title: 5G Multicast Broadcast Services
has_children: true
nav_order: 4
---

<img src="../assets/images/Banner_5MBS.png" /> 

# 5G Multicast Broadcast Services - Tech Resources

* Check the [**Execution Plan**](https://github.com/orgs/5G-MAG/projects/44/views/7)
* Information on relevant [**Standards**](https://5g-mag.github.io/Standards/pages/5g-multicast-broadcast-services.html)
* **Reference Tools** available:
    * [**Project: 5G Multicast Broadcast Services**](https://5g-mag.github.io/Getting-Started/pages/5g-multicast-broadcast-services/)

## Overview
<iframe width="60%" height="520" src="https://drive.google.com/file/d/1DclW1VVZkyq9dLjdIdmm3qhhihZ-aF3t/preview"></iframe>

[DOWNLOAD THE PRESENTATION](https://drive.google.com/file/d/1DclW1VVZkyq9dLjdIdmm3qhhihZ-aF3t/preview){: .btn}

---

<img src="../assets/images/Banner_Explainers.png" width="50%" /> 

## Technical Explainers
* Check this **Explainer** on [**Media distribution with 5G Multicast-Broadcast Services (MBS)**](./5g-multicast-broadcast-services/explainer_1.html)

## Informative Videos

### User Services for the 5G Multicast-Broadcast Service (3GPP Release 17)
<iframe width="560" height="315" src="https://www.youtube.com/embed/73KINNxl_FA?si=Jbj6BID6uaXxFGOP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<img src="../assets/images/Banner_TechAnalysis.png" width="50%" /> 

In 2019, 3GPP identified a number of services across different industry verticals that share the requirement of conveying common data to multiple recipients at the same time - for example public safety, V2X, group communications and internet of things (IoT). 

As multicast and broadcast have the potential to deliver ‘common data’ services more efficiently than unicast 3GPP has since standardised these capabilities in the 5G system as 5G New Radio Multicast and Broadcast Services (5G-NR MBS). 5G-NR MBS will be substantially complete in Release 17 (Rel-17), with some (mainly service) aspects carrying over to Rel-18.

In principle, 5G-NR MBS equipped mobile networks would be able to use the most suitable delivery method (i.e. unicast, multicast or broadcast) for a given service depending its requirements and demand within the network. For example, if many user devices requested the same content at the same time in a given cell, the multicast or broadcast delivery methods could be used whereas in periods of lower demand, or more challenging wireless propagation conditions, unicast may be a better option. 

Media services, for example linear/live radio and TV, concurrently requested by a number of users, although not explicitly identified as a relevant use case have many characteristics in common with the use cases that were identified, and so may also benefit from 5G-NR MBS.

{: .note } Editor's note: Include the stack from SA4 to RAN1

These pages provide an introduction to 5G-NR MBS in the context of media distribution:

## [MBS Service Layer Aspects](./5g-multicast-broadcast-services/mbs-service-layer.html)

## [MBS Service and System Aspects](./5g-multicast-broadcast-services/mbs-service-system-aspects.html)

## [MBS RAN Aspects](./5g-multicast-broadcast-services/ran-aspects.html)

## [Aspects on Mobility for MBS Multicast Services](./5g-multicast-broadcast-services/Mobility_MBS_Multicast.html)

---

<img src="../assets/images/Banner_WorkTracking.png" width="50%" /> 

This is a summary of the work conducted by 5G-MAG members on this topic. Check the [**Execution Plan**](https://github.com/orgs/5G-MAG/projects/44/views/7) for details.

### In relation to Standards
* Documentation on MBS for media delivery and content scalability
* Documentation on architecture, features and procedures in the 5GC, RAN and MBS User Services components
* 3GPP Standardization tracker and relevant Work Items
* Support to standards with feedback from implementation

### In relation to Software
* Implementation of 5MBS User Services components
* Implementation of end-to-end 5MBS delivery chain for SDR-based hardware
