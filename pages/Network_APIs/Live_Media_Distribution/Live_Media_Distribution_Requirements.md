---
layout: default
title: Requirements
parent: Live Media Distribution
grand_parent: Network APIs
nav_order: 1
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Network Capabilities (Network Services) for Live Segmented Media Distribution

## Quality of Service
The following requirements are defined:
- Ability to request different QoS profiles for individual data flows being distributed across a target service area
- Ability to provision QoS profiles for reliable and consistent media segment transfer time on individual data flows to support interruption-free presentation by the media player with minimal buffering.
- Ability to configure new or re-configure existing QoS profiles to be selected during runtime

{: .note }
To be resolved:What does "during runtime" mean? Seems vague. Does it mean during a live media consumption session? I can see that might be applicable in the case of dynamic adaptation by the client, which is common for live video distribution but less common for live audio distribution.
Which party is responsible for the (re)selection of the QoS profiles? Is this intended to be application-driven or network-driven?

- Ability to identify the set of application data flows that fall within the scope of a particular QoS profile treatment

## Information monitoring, logging and/or Network assistance
- Ability to receive information from the network
  - real-time for QoS profile re-configuration

{: .note }
Again, what does real time mean in practice? Too vague at the moment. Maybe "During the course of a media consumption session"?

  - during runtime for troubleshooting 
  - after the session (logging information) for post-processing

## Geofencing
- Ability to verify whether a given UE is currently located inside or outside the target service area.
- Ability to receive notifications when individual UEs enter or leave the target service area.

{: .note }
RB: I don't think there is a need to track the current location of an individual UE on an ongoing basis via a network exposure API because the application running on the UE already has access to that information (with the user's permission).
