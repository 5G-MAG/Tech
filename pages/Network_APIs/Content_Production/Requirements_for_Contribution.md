---
layout: default
title: Requirements
parent: Content Production & Contribution
grand_parent: Network APIs
nav_order: 2
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Network Exposure and APIs Supporting Media Services and Applications**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Network Capabilities (Network Services) for Content Production & Contribution

This is a list of network capabilities required to realize the scenarios described in  [Network Capability Exposure and APIs for Content Production and Contribution Scenarios](https://5g-mag.github.io/Tech/pages/Network_APIs/Content_Production/Content_Production_Contribution.html).

## Media delivery with Quality of Service (QoS)
- Ability to request different QoS profiles for individual data flows coming from the same production device node
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

## Voice service for Intercom
- Ability to establish a voice service across the intercom devices deployed at the production location or between the production center and the production location.

{: .note}
Focus on the QoS for Intercom - a voice service offered by the network may not be so relevant (alternative solutions, WebRTC). But multicast, MCPTT may be of use.

## Out of scope
- Tag the combination device+stream+flow with a human-readable identifier that can be mapped to an IP address and port number (e.g. applying the NMOS framework).

# Considerations on Devices

## Device Identification
- Ability to uniquely identify a devices against the network operator

## Data flow identifier
- Ability to uniquely identify the different data flows within a device

