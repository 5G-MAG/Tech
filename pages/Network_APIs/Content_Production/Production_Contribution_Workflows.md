---
layout: default
title: Workflows and Requirements
parent: Content Production & Contribution
grand_parent: Network APIs
nav_order: 2
has_children: false
---

<img src="../../../assets/images/Banner_API.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Workflows and Requirements for Content Production & Contribution

[**Scenarios and Use Cases**](../Production_Contribution_Scenarios.html) describe two reference scenarios. The workflows in relation to the booking and usage of network capabilities are described here with a focus on quality of service (QoS).

This section contains information on:
* [**Pre-conditions and commonalities**](#pre-conditions-and-commonalities)
* [**Workflow for Single-device Connectivity**](#single-device-connectivity-single-camera-live-video-production-mobile-journalism-mojo-newsgathering-uplink-video)
* [**Workflow for Multi-device Connectivity**](#multi-device-connectivity-outside-broadcast-small-scale-video-production-remote-production)
* [**Dynamic management of network capabilities during runtime**](#dynamic-management-of-network-capabilities-during-runtime)
* [**Requirements**](#requirements)

## Pre-conditions and commonalities

Before invoking any API, it is assumed that:

* The production crew has a set of credentials (SIM/eSIM) for the network device nodes will connect to.
* By default, the network provides "best-effort" connectivity and devices can already exploit "best-effort" connectivity.
* The production company has set up an agreement with a network operator for usage of certain **network capabilitues** made available via an API. The production crew has obtained key access tokens/keys/credentials/payment details in advance authorising their use (when available).
* The production crew (on location or located in the production centre) has access to one or more **Network API Platforms**. These platforms are accessible by any device/connectivity (e.g. Internet-accessible website portal, command line tools, dedicated application, etc.).
* API Consumers will be able to select from available profiles, service areas, and parameters offered by the API Provider.

## Collaboration scenarios for the provisioning of network capabilities

### Collaboration scenario #1: Direct invoking Network APIs
The **Network API Platform** of a Network Operator is accessed directly from **API Consumers**, either deployed with the Studio Production or the Location Production functions. The API consumer can be a Web Portal, e.g. offered by the CSP. Alternatively, the API consumers can be embedded production devices like a Vision Mixer or a production orchestration solution ([NMOS](https://specs.amwa.tv/nmos/branches/main/docs/Technical_Overview.html)  concept). The API consumer functions can be integrated in media servers, responsible for receiving the video stream from the application client.

<img src="./images/figure_collaboration_1.png" width="60%">

### Collaboration scenario #2: Invoking Network APIs via an Aggregator
The **Network API Platform** of a Network Operator is accessed via an **Aggregator API Platform**. The Aggregator Platforms harmonize capabilities offered by different Network Providers and routes customer requests to them.

<img src="./images/figure_collaboration_2.png" width="60%">

## Consolidation of requirements on network interactions
The basic requirements for this scenario are:

### **Ability to DISCOVER network resources**, at a given location and time/duration.
  * This step is required to obtain information about the ability or not to reserve (and use) network resources for the intended location and time/duration.
  * A QoS template may be used to define the required QoS parameters between the application (device) and application server.
  * It should be able to indicate an aggregate of network resources corresponding to the number of devices with the same QoS requirements. For a single device, the aggregate would be just one device.

<table>
  <tr>
    <td markdown="span" align="left"><b>DISCOVERY API<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">Invoked with: QoS template, location/area, time/duration, number of devices intended to use resources concurrently</td>
  </tr>
  <tr>
    <td markdown="span" align="left">Response: Ability or not to reserve such resources.</td>
  </tr>
</table>

Remarks on the **location**:
* The user should be able to indicate the location where the network resources are to be used by means of coordinates for an area (array of points) or a single point.
* It is unlikely that the user-defined area corresponds to the operator-defined area.
* A more general API could be invoked with the user-defined area as input and a operator-defined area identifier as output.

### **Ability to RESERVE network resources**, by indicating location and time/duration.
  * Network resources can be reserved for the intended location and time/duration.
  * A QoS template may be used to define the required QoS parameters between the application (device) and application server.
  * It should be able to reserve an aggregate of network resources corresponding to the number of devices with the same QoS requirements. For a single device, the aggregate would be just one device.

<table>
  <tr>
    <td markdown="span" align="left"><b>RESERVATION API<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">Invoked with: QoS template, location, time/duration, number of devices intended to use resources concurrently</td>
  </tr>
  <tr>
    <td markdown="span" align="left">Response: Effective reservation of resources for the specified location and duration. A range of reservation IDs corresponding to the number of devices which can concurrently use such resources.</td>
  </tr>
</table>

### **Ability to ASSIGN the device to the reserved network resources**, by linking a _reservation ID_ with a _device ID_.
  * The devices for which resources are reserved are known in advance. However better flexibility would be given if the resources are not linked to a specific device at reservation. The device finally using the network resources may change between the reservation of network resources and their actual usage. A change of the device while in operation may also be needed (e.g. for replacement by a back-up device).

<table>
  <tr>
    <td markdown="span" align="left"><b>ASSIGNMENT API<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">Invoked with: reservation ID and device ID</td>
  </tr>
  <tr>
    <td markdown="span" align="left">Response: ACK and an assingment ID per device.</td>
  </tr>
</table>

### **Ability to activate/deactivate the USAGE of the network resources**, either automatically when the device is connected to the network or manually. Activating the usage of network resources just when the device obtains connectivity is not ideal. For instance, a device should use best-effort connectivity in the event of a problem (need to exchange a device) while a new device is assigned the network resources.

<table>
  <tr>
    <td markdown="span" align="left"><b>USAGE API<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">Invoked with: Assingment ID</td>
  </tr>
  <tr>
    <td markdown="span" align="left">Response: ACK the activation of the resources for the current assignment</td>
  </tr>
</table>

### **Ability to activate/deactivate NOTIFICATIONS on the usage of the network resources**.

<table>
  <tr>
    <td markdown="span" align="left"><b>NOTIFICATIONS API<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">Invoked with: Assignment ID, periodicity of notifications, sink for notifications</td>
  </tr>
  <tr>
    <td markdown="span" align="left">Response: ACK the activation of the notification</td>
  </tr>
</table>

# Single-device Connectivity (Single Camera Live Video Production, Mobile Journalism (MoJo), Newsgathering, Uplink Video)

## Before the Event

### Phase A: Preparing devices, configuring application clients and servers, and configuring client/server flows

<img src="./images/Workflow_Step_1.png" width="60%">

* Production device nodes are generally UEs which establish connectivity to servers in the Data Network. 
* An **application-specific API** (e.g. from the media equipment provider) enables client/server communication to configure media-related parameters and procedures.

<table>
  <tr>
    <td markdown="span" align="left"><b>Practical example<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">A typical setup can consist of a smartphone used to capture video which is then send to a server in the cloud for uplink streaming. The provider of such a service, or the user, would have configured the IP addresses, ports, and other parameters between the user application and the application server through such application-specific API. For a cellular backpack, a similar configuration should be followed.</td>
  </tr>
</table>

### Phase B: Event planning and pre-booking

<img src="./images/Workflow_Step_2.png" width="60%">

Through the Network API Platform:

1. The production crew (already on location or while traveling to the event) can discover the capabilities the network can offer in a particular location and at a particular time. Example: QoD available, connectivity monitoring available.

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke DISCOVERY API<b/></td>
  </tr>
</table>

2. The production crew requests network services for the devices (identified by its SIM cards) in advance. The booking of resources is done based on:
  * Geographical area
  * Schedule (starting time and closing time, or duration, of the event)

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke RESERVATION API<b/></td>
  </tr>
</table>

3. The production manager receives a booking reference responding to the service request.
4. The production manager accepts the service booking offer (involving payment).
5. The production manager receives **network access IDs** to be used by the production device UEs to access the network and the requested capabilities for the specified location and duration.
    * Each network access ID ultimately resolves to a Data Network Name (DNN) and optionally a network slice identifier (S-NSSAI).

<table>
  <tr>
    <td markdown="span" align="left"><b>Practical example<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">This should be seen as nothing very different to going to the portal of your network operator to e.g. add a bonus for more data, activate/deactivate roaming opetions, and other services within your existing contract. If the contract includes the ability to select extra connectivity services (e.g. Quality of Service) those should be selectable from such or a similar portal.</td>
  </tr>
</table>
     
## During the event

<img src="./images/Workflow_Step_3.png" width="60%">

### Phase C: Configuration and Usage of the network capabilities
1. The production crew arrives at the event and can start using the booked network services (See phase B).

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke ASSIGNMENT API<b/></td>
  </tr>
</table>

2. The production device makes use of the network capabilities according to the network access IDs reveived. The media related parameters can be adapted using an application-specific API, citing the network access IDs delivered in step B.5).

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke USAGE API<b/></td>
  </tr>
</table>

<table>
  <tr>
    <td markdown="span" align="left"><b>Practical example<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">In a typical scenario, the journalist arrives to the location where the uplink video contribution should start. The network desired network conditions can be checked and booked on the spot so the transmission can start with the desired QoS. If known in advanced, the booking may have been done before arriving to the event. If network conditions are guaranteed (i.e. the booked service is being used), the media flow can be optimized by passing the details to the media application. For instance, if the network is able to guarantee X Mbps, the user can configure an encoder so it stays within margins avoiding packet loss.</td>
  </tr>
</table>
     
## After the event

### Phase D: Location teardown
1. Through the Network API Platform, the production crew releases the booked resources when the event finishes.

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke RESERVATION API<b/></td>
  </tr>
</table>

---

## Multi-device connectivity (Outside Broadcast, Small-Scale Video Production, Remote Production)

## Before the Event

### Phase A: Preparing devices, configuring application clients and servers, and configuring client/server flows

<img src="./images/Workflow_Step_1.png" width="60%">

* Some production device nodes are UEs; others are connected to the Data Network:
  * Example production device nodes connected to the RAN: wireless cameras, wireless camera control units, wireless microphones, wireless talkback intercom, etc.
  * Example production device nodes connected to the Data Network: vision mixer, sound mixer, etc. 
* An **application-specific API** (e.g. from the media equipment provider) enables communication between the production network orchestrator and the production device nodes to configure media-related parameters and procedures.

<table>
  <tr>
    <td markdown="span" align="left"><b>Practical example<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">A typical setup can consist of several cameras, intercom, video return, mixers,... all interconnected and/or providing content to e.g. a vision mixed in the cloud. Connectivity should be established for all the equipment, which configuration is done via the application-specific API.</td>
  </tr>
</table>

### Phase B: Event planning and pre-booking

<img src="./images/Workflow_Step_2.png" width="60%">

Through the Network API Platform:
1. The production crew (on location or from the production centre) can discover the capabilities the network can offer in a particular location and at a particular time (for which the production company is eligible for). Example: QoD available, connectivity monitoring available, Timing as a service available, edge compute instantiation, etc.

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke DISCOVERY API<b/></td>
  </tr>
</table>

2. The production crew requests network services for the devices (identified by its SIM cards) in advance. Possible services (network capabilities) are:
   1. *Quality-on-Demand*
      * One or several QoS profiles for each SIM card (QoS profiles are mapped to 5QIs) 
      * Example: A sim may be pre booked for one uplink video / one uplink audio / one downlink data / etc.
   2. *Time-as-a-service*
      * Provided either by access stratum or Precision Time Protocol (PTP).
  
   The booking of resources is done based on:
      * Geographical area
      * Schedule (starting time and closing time, or duration, of the event)

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke RESERVATION API<b/></td>
  </tr>
</table>

3. The production manager receives a booking reference responding to the service request.
4. The production manager accepts the service booking offer (involving payment/contract/SLA aspects).
5. The production manager receives **network access IDs** to be used by the production device UEs to access the network and the requested capabilities for the specified location and duration.
    * Each network access ID ultimately resolves to a Data Network Name (DNN) and optionally a network slice identifier (S-NSSAI).

<table>
  <tr>
    <td markdown="span" align="left"><b>Practical example<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">This should be seen as nothing very different to going to the portal of your network operator to e.g. add a bonus for more data, activate/deactivate roaming opetions, and other services within your existing contract. If the contract includes the ability to select extra connectivity services (e.g. Quality of Service) those should be selectable from such or a similar portal. For a planned event taking place at a known location and for a given duration, the booking of network resources can be done beforehand by indicating the requirements, number of devices, QoS requirements for each of the devices or a group of them,...</td>
  </tr>
</table>

## During the event

<img src="./images/Workflow_Step_3.png" width="60%">

### Phase C: Configuration and Usage of the network capabilities
1. The production crew arrives in the venue, plugs the SIM cards and turn on the devices, connectivity is enabled based on the booked network services (See phase B).

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke ASSIGNMENT API<b/></td>
  </tr>
</table>

3. The production crew initiates the setup of the location production by interacting with the production network orchestrator.
4. The production network orchestrator configures the production device nodes using an application-specific API, citing the network access IDs delivered in step B.5).

   * Example: QoD service: A camera for which  one video + one audio is pre-booked. The application-specific API is used to properly configure the bitrate of the audio and video output, and the provided IDs.
   * Example: Time Sync service: A camera for which access to global clock is requested. The application-specific API is used to properly configure the time parameters and the provided IDs.

5. The production device makes use of the network capabilities according to the network access IDs reveived.

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke USAGE API<b/></td>
  </tr>
</table>

<table>
  <tr>
    <td markdown="span" align="left"><b>Practical example<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">Once at the location, connectivity needs to be established among the devices. Once this is ready, the setup will have the ability to exploit the pre-booked network resources.</td>
  </tr>
</table>

Note: the steps in phase C are repeated whenever a service is added and created from scratch.
 
## After the event

### Phase D: Location teardown
1. Through the Network API Platform, the production crew releases the booked resources when the event finishes.

# Dynamic management of network capabilities during runtime

A series of actions can be expected "During the Event" as changes, reconfiguration or additional requests may need to be processed.

## Monitoring and notifications
* The production crew should use the Network API Platform to monitor that the flows are coming and are properly using the reserved resources.
* The production crew should receive notifications through the Network API Platform indicating potential issues (throughput, delay, etc.).

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke NOTIFICATION API<b/></td>
  </tr>
</table>

## Reconfiguration for a given device
* The production crew through the Network API Platform should request a change of the current configuration assinged to a device
* The production crew through the Network API Platform should request an update/modification of the originally booked resources (e.g. increase or decrease the thoughput associated to an existing profile). Same validation steps as from B.2 to B.5 will be conducted after requesting the change. Note that the network access IDs are not expected to change when a reconfiguration occurs.

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke RESERVATION API<b/></td>
  </tr>
</table>

## Back-up devices
* The production crew through the Network API Platform should switch/update a device while being able to use the original booking of a different device.

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke ASSIGNMENT API<b/></td>
  </tr>
</table>

## Dynamic prioritization of QoS for different media flows

In a setup with multiple camras, the media producer would like to ensure that there is always a subset of those being prioritized with the highest QoS profile. While each individual camera should be entitled to exploit such high QoS profile (i.e. the original booking should take into account that X devices will be requesting QoS profile Y), not all of them will be using such profile concurrently. Therefore:
* The production crew though the Network API Platform should dynamically attach/detach a device to a QoS profile.

<table>
  <tr>
    <td markdown="span" align="left"><b>Requirement to invoke ASSIGNMENT API<b/></td>
  </tr>
</table>

* The network operator should secure that a subset of devices can concurrently request a given QoS profile and that all other devices remain eligible to access such profile when it is no longer used.

### Basic example: Definition of QoS Profiles

A media production requires 4 devices (e.g. cameras, smartphones). The output video quality of the cameras can switch from being "On Air" (high quality video), "Preview" (lower quality video which can quickly scale up when needed to be "On Air"), "Standby" (a minimum quality video for monitoring a scene in a video gallery).

Therefore, first step is to define such QoS profiles which cameras can use.

<table>
  <tr>
    <td markdown="span" align="left"><b>QoS Profile name</b></td>
    <td markdown="span" align="left"><b>Parameters</b></td>
  </tr>
  <tr>
    <td markdown="span" align="left">QoS_OnAir - QoS Profile for High Quality Video</td>
    <td markdown="span" align="left">Uplink throughput = 10 Mbps</td>
  </tr>
  <tr>
    <td markdown="span" align="left">QoS_Preview - QoS Profile for Previw Quality Video</td>
    <td markdown="span" align="left">Uplink throughput = 5 Mbps</td>
  </tr>
  <tr>
    <td markdown="span" align="left">QoS_Standby - QoS Profile for Standby</td>
    <td markdown="span" align="left">Uplink throughput = 2 Mbps</td>
  </tr>
</table>

### Basic example: Identification of elegible devices-profiles

Among the 4 devices:
* Only one device is expected to use the QoS_OnAir profile during runtime. The rest will be either in QoS_Preview or QoS_Standby. When the media producer decides to switch the On-Air camera, there are temporarily two devices assigned with a QoS_OnAir profile.
* Only one device is expected to use the QoS_Preview profile during runtime. The QoS_Preview profile is used for devices, which are about to be switched to the OnAir profile. Typically, the camera operator gets notified with the Preview selection, that its camera is next to be on air.
* Cameras, which are providing their video “just” to the production gallery, are assigned with QoS_Standby profile.

<table>
  <tr>
    <td markdown="span" align="left"><b>Device</b></td>
    <td markdown="span" align="left"><b>Eligible QoS Profiles</b></td>
  </tr>
  <tr>
    <td markdown="span" align="left">Device C1</td>
    <td markdown="span" align="left">QoS_OnAir, QoS_Preview and QoS_Standby</td>
  </tr>
  <tr>
    <td markdown="span" align="left">Device C2</td>
    <td markdown="span" align="left">QoS_OnAir, QoS_Preview and QoS_Standby</td>
  </tr>
  <tr>
    <td markdown="span" align="left">Device C3</td>
    <td markdown="span" align="left">QoS_OnAir, QoS_Preview and QoS_Standby</td>
  </tr>
  <tr>
    <td markdown="span" align="left">Device C4</td>
    <td markdown="span" align="left">QoS_OnAir, QoS_Preview and QoS_Standby</td>
  </tr>
</table>

Note that the intention of this pre-booking is to make sure that 4 devices can be attached to 3 different QoS profiles during runtime. However not all the devices and profiles are used concurrently.

### Basic example: Assignment of QoS Profile during runtime

With the assumptions above:
* The production crew through the Network API Platform should request a change of the assinged device from one QoS profile to another.

From the network resources point of view, there will be:
* A maximum of 2 devices concurrently assigned a QoS_OnAir profile (20 Mbps) plus 2 other devices with the QoS_Standby profile (4 Mbps) - peak throughput is 24 Mbps.
* Most of the time a maximum of 1 device will be assigned a QoS_OnAir profile (10 Mbps) plus 3 other devices with the QoS_Standby profile (6 Mbps) - peak thoughput is 16 Mbps.
* Only when the camera is about to be assinged QoS_OnAir there will be a transition by the QoS_Preview profile - 1 QoS_OnAir (10 Mbps) + 1 QoS_Preview (5 Mbps) + 2 QoS_Standby (4 Mbps) - peak throughput is 19 Mbps.

# Requirements

## Media delivery with Quality of Service (QoS)

Requirement | API  
-- | --
Ability to request different QoS profiles for individual data flows coming from the same production device node |
Ability to separate media/data flows coming from the same production device node |
Delivery to endpoint (Application Media Server) may be identified by security/protocol/IP/port |
Ability to configure new or re-configure existing QoS profiles to be selected during runtime |
Ability to select at runtime a QoS profile for a media flow |
Ability to receive ACK (success/fail) |

## Information monitoring, logging and/or Network assistance

Requirement | API
-- | --
Ability to receive information from the network |
Real-time information for QoS profile re-selection and/or e.g. codec reconfiguration, bitrate reconfiguration |
Information during runtime for troubleshooting |
Information after the session (logging information) for post-processing |

## Time Synchronization

Requirement | API  
-- | --
Ability to enable distribution of timing information | 

### Voice service for Intercom

Requirement | API 
-- | --
Ability to establish a voice service across the intercom devices deployed at the production location or between the production center and the production location | 

{: .note}
Focus on the QoS for Intercom - a voice service offered by the network may not be so relevant (alternative solutions, WebRTC). But multicast, MCPTT may be of use.

# Considerations on Devices

## Identification of devices

Requirement | API 
-- | --
Devices should be uniquely identifiable during operation |
Devices should be dynamically added or deleted during operation and attachable to given network capabilities |
Each device should only access the network capabilities which have been assigned during booking |

## Device on-boarding and API consumer on-boarding

Requirement | API 
-- | --
TBD How to obtain credentials |

## Discovery of network capabilities

Requirement | API 
-- | --
TBD How to discover network capabilities |
