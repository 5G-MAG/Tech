x---
layout: default
title: Workflow for Content Production & Contribution
parent: Network APIs
nav_order: 0
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Network Exposure and APIs Supporting Media Services and Applications**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Required interactions to exploit network capabilities
  
## PRE-CONDITIONS
  * The production company has set up an agreement for Network Capability usages. As result, the production company obtained information, used for authentication. During the process of agreement negotiation, a set of relevant network capabilities have been identified (e.g. using an API catalogue). As result, the production company is authorized to use certain network capabilities (when available).
  * The production crew has access to one, or several, Network API Platforms. This platform is accessible through any device/connectivity (e.g. a website accessible through the open internet, or command prompt, a dedicated app, etc …).
    * Note: For the Network API Platform access, the crew has prepared obtained key access tokens/key/credentials/payment-details in advanced
  * The production crew have a set of credentials (SIM/eSIM) of the network devices will connect to. The network provides, by default, best-effort connectivity.
 
## BEFORE THE EVENT: 
 
Step 1) : Preparing your device, configuring application clients & servers and configuring client/server flows
  * Devices have already best effort connectivity 
  * Through app specific [AppAPI], the client app is properly connected to the Application Server. e.g. Haivision app with BBC server, or LiveU app with LiveU server, etc …
    * Note: be careful with trademarks, maybe only use Haivision as they are members.
 
Step 2) : Event planning and pre-booking
  * a) Through the Network API Platform, the production crew can discover the capabilities the network can offer (for which the production company is eligible for).
    * Example: QoD available, connectivity monitoring available, Timing as a service available, edge compute instantiation, …
  * b) Through the Network API Platform, the production crew requests network services for every of the planned SIM cards in advance. Possible services (Network Capabilities) are:
    * Quality on Demand
      * One or several QoS profiles for each SIM card (QOS Profiles are mapped to 5QIs) 
      * Example: A sim may be pre booked for One uplink video / One uplink audio / one downlink data / …
    * Time as a service
      * Access stratum based or PTP based
    * Note: Booking is done based on :
      * Geographical area
      * Schedule (starting time and closing time of the event)
  * c) Through the Network API Platform, the production receives a booking offer responding to the service request.
  * d) Through the Network API Platform the production accepts the service booking offer (involving payment/contract/SLA aspects)[TL6] .
  * e) Through the production receives connection IDs to be used for every reserved SIM/services
 
## DURING THE EVENT :
 
Step 3) : Local configuration
  * a) Production crew arrives in the venue, plugs the SIM cards and turn on the devices, connectivity is enabled based on the booked network services (See step 2).
  * b) The production crew uses [AppAPI] to configure the different services, matching the connection ID delivered in step 2-e).
    * Example: QoD service: A camera for which  one video + one audio is pre-booked. The [AppAPI] is used to properly configure the bitrate of the audio and video output, and the provided IDs.
    * Example: Time Sync service: A camera for which access to global clock is requested. The [AppAPI] is used to properly configure the time parameters and the provided IDs.
 
Independent steps that can be triggered during the life of the event:
  * The production crew can use [GwAPI] to monitor that the flows are coming and are properly using the reserved resource.
  * The production crew receives notification through [GwAPI] indicating potential issues (throughput, delay, …)
  * The production crew through [GwAPI] can request a change of the current configuration
    * Same validation steps as from 2-b to 2-e will be conducted after requesting the change
    * Changes can be:
      * Switch profile A from SIM card A to SIM card B
      * Increase or decrease the capacity of an existing profile
      * Remove or add a profile to a SIM card
      * Enable/Disable time service on a SIM card
      * etc …
      * Note: Connection ID are not expected to change when a reconfiguration occurs.
      * Note: When a service is added and created from scratch, step 3) should be done again.
 
## END OF THE EVENT :
 
Step 4) : release resources
  * The production crew through [GwAPI] releases the booked resources.
 
