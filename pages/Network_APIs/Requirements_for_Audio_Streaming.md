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

# Network Capabilities (Network Services) for Content Production & Contribution

## Quality of Service
- Ability to apply different QoS profiles to individual data flows coming from the same production device node
- Ability to separate media/data flows coming from the same production device node
  - Delivery to endpoint (Application Media Server) may be identified by security/protocol/IP/port
- Ability to configure new or re-configure existing QoS profiles to be selected during runtime 
- Ability to select at runtime a QoS profile for a media flow
- Ability to receive ACK (success/fail)

## Information monitoring, logging and/or Network assistance
- Ability to receive information from the network
  - real-time for QoS profile re-selection and/or e.g. codec reconfiguration, bitrate reconfiguration
  - during runtime for troubleshooting 
  - after the session (logging information) for post-processing

## Time Synchronization
-	Ability to enable distribution of timing information

# To be solved by the production system (e.g. NMOS)
- Tag a device+stream+flow with a human-readable identifier that can be mapped to an IP address and port number




## Add section on devices?

## Connectivity related

### Device Identification
- Ability to obtain a device ID to uniquely identify a devices against the network operator

### Data flow identifier
- Ability to identify the different data flows (PDU session ID??) per device

