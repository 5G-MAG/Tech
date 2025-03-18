---
layout: default
title: Requirements
parent: Audio Streaming App
grand_parent: Network APIs
nav_order: 1
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Network Exposure and APIs Supporting Media Services and Applications**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Network Capabilities (Network Services) for Audio Streaming Applications

## Quality of Service
Today, audio streaming services would have to be delivered over-the-top, i.e. without any defined quality of service (QoS). Measurements of such a service over today's mobile networks indicate that the QoS experienced by listeners may fall short of their expectations (e.g. latency and interruption-free audio playblack similar to conventional broadcast radio). Therefore, the following requirements are defined:  
- Ability to set quality of service requirements for a given location
- Ability to provision for realiably low-latency
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

