---
layout: default
title: Requirements
parent: Live Media Distribution
grand_parent: Network APIs
nav_order: 1
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Network Exposure and APIs Supporting Media Services and Applications**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Network Capabilities (Network Services) for Live Segmented Media Distribution

## Quality of Service
The following requirements are defined:
- Ability to request different QoS profiles for individual data flows being distributed across a target service area
- Ability to provision individual data flows for realiably low latency (distribution delay)
- Delivery to endpoint (Application Media Server) may be identified by security/protocol/IP/port
- Ability to configure new or re-configure existing QoS profiles to be selected during runtime 
- Ability to receive ACK (success/fail)

## Information monitoring, logging and/or Network assistance
- Ability to receive information from the network
  - real-time for QoS profile re-configuration
  - during runtime for troubleshooting 
  - after the session (logging information) for post-processing

## Geofencing
- To verify and/or retrieve the location of a UE
- To receive notifications from UEs entering or leaving certain locations/areas (e.g. for determining the content appropriate for the current editorial region).

