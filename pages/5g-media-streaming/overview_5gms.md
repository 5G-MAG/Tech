---
layout: default
title: 5GMS Overview
parent: Streaming & Media Delivery
has_children: false
nav_order: 0
---

<img src="../../assets/images/Banner_Streaming.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# 5G Media Streaming - Overview

In the context of 3GPP standards, 5G Media Streaming (5GMS) is defined as a framework designed to enable high-quality, efficient delivery of media. The architecture supports services from mobile network operators and third parties including both Downlink (5GMSd) and Uplink (5GMSu) Media Streaming. The 5GMS architecture is functionally divided into independent components enabling deployments with various degrees of integration between 5G MNOs and Content Providers.

5GMS is not a separate network but a functional extension of the standard 5G System Architecture. It is the bridge that allows 5G networks to move away from being a "data pipe" and instead become an active, optimized platform for professional and user-generated media content.

<img src="./images/5GMS_General.png" width="60%">

The main functional entities are:

* **5GMS Application Provider**: The entity that uses the 5G network to deliver content. It provides a 5GMS Aware-Application on the UE to make use of 5GMS Client and network functions via 5GMS interfaces and APIs.

* **5GMS Application Function (5GMS AF)**: A specialized application function dedicated to the management and optimization of media streaming sessions.

* **5GMS Application Server (5GMS AS)**:  A specialized application server which primary job is to store, cache, and deliver media content to the User Equipment (UE) or to receive and ingest media from the UE

* **5GMS Client**: The functional part of the user's device (UE) that handles the media session and the player/streamer logic.

A list of relevant specifications can be found in the link below.

[Specifications](https://hub.5g-mag.com/Standards/pages/5g-media-streaming.html){: .btn .btn-blue }

# 5G Unicast Downlink Media Streaming (5GMSd)

To deliver downlink streaming services, the network is the origin of the media and the UE acts as the consumption device.
 
<img src="./images/5GMS_Downlink.png" width="60%">

The main functional entities are:

* **5GMSd Application Provider**: The external entity responsible for the "source" side of the media—creating, encoding, and formatting the content. It utilizes 5GMSd interfaces to deliver this media to the user's application.

* **5GMSd AS**: The hosting environment for media content. It can be a single server or a distributed network, such as a Content Delivery Network (CDN), to optimize delivery.

* **5GMSd AF**: The control-plane entity providing management functions to the device’s Media Session Handler and the Application Provider. It also acts as the bridge to the 5G Core, interacting with the PCF or NEF.

* **5GMSd Client**: The primary receiver on the device for downlink streaming services. It can be implemented with exposing APIs (M6d/M7d) for external use or as a self-contained entity where those interfaces are internal. It consists of two sub-components:

  * **Media Session Handler**: The "control brain" on the device. It coordinates with the 5GMSd AF to set up and manage sessions while gathering data like Quality of Experience (QoE) and consumption metrics.

  * **Media Player**: The "data engine" on the device. It communicates with the 5GMSd AS to fetch and play the actual media stream. It provides playback controls to the app and session status to the Session Handler.

* **5GMSd-Aware Application**: An external app (e.g., a streaming service) that holds the provider's specific logic. Uses standardized APIs to initiate and manage media sessions.

The 5GMSd Client may include several subfunctions which are depicted below:

<table>
  <tr>
    <td markdown="span" align="center" style="width:40%"><img src="./images/5GMS_MediaPlayer.png" width="60%"><a/></td>
    <td markdown="span" align="center" style="width:40%"><img src="./images/5GMS_MediaSessionHandler.png" width="60%"><a/></td>
  </tr>
  <tr>
    <td markdown="span" align="center">Subfunctions of the Media Player</td>
    <td markdown="span" align="center">Subfunctions of the Media Session Handler</td>
  </tr>
</table>

## Interfaces for 5GMSd

The interfaces are:

| Interface | Name | Description |
| :--- | :--- | :--- |
| **M1d** | **5GMSd Provisioning API** | External API exposed by the **5GMSd AF**; allows the Application Provider to configure the system for downlink streaming and receive feedback. |
| **M2d** | **5GMSd Ingest API** | Optional external API exposed by the **5GMSd AS**; used for uploading content when the AS is hosted within a trusted Data Network. |
| **M3d** | Internal Interface | An **unspecified internal API** used for information exchange between the 5GMSd AF and AS regarding content hosting. |
| **M4d** | **Media Streaming APIs** | The primary data-plane APIs exposed by the **5GMSd AS** to the **Media Player** for streaming media content. |
| **M5d** | **Media Session Handling API** | Control-plane APIs between the **5GMSd AF** and **Media Session Handler** for session control, QoE reporting, and security (auth/auth). |
| **M6d** | **UE Media Session Handling APIs** | Internal UE APIs that allow the **5GMSd-Aware App** and the **Media Player** to access 5GMS session functions. |
| **M7d** | **UE Media Player APIs** | Internal UE APIs used by the **5GMSd-Aware App** and **Session Handler** to control playback and media engine functions. |
| **M8d** | **Application API** | An external interface for "service-level" exchange (like metadata or login) between the **App** and the **Provider**. This is **not specified** by 3GPP. |

## Key Features for 5GMSd and APIs

The following features are defined for 5GMSd.

Feature | Description | Procedure | APIs 
--- | --- | --- | ---
**Content hosting** | 3GPP TS 26.501 4.0.2 | 3GPP TS 26.501 5.4 | 3GPP TS 26.510 + 26.512
**Network assistance** | 3GPP TS 26.501 4.0.5 | 3GPP TS 26.501 5.9 | 3GPP TS 26.510 + 26.512
**Dynamic policies** | 3GPP TS 26.501 4.0.6 | 3GPP TS 26.501 5.8 | 3GPP TS 26.510 + 26.512
**Consumption reporting** | 3GPP TS 26.501 4.0.8 | 3GPP TS 26.501 5.6 | 3GPP TS 26.510 + 26.512
**QoE metrics reporting** | 3GPP TS 26.501 4.0.9 | 3GPP TS 26.501 5.5 | 3GPP TS 26.510 + 26.512
**Edge processing** | 3GPP TS 26.501 4.0.10 | 3GPP TS 26.501 8 | 3GPP TS 26.510 + 26.512
**eMBMS delivery** | 3GPP TS 26.501 4.0.11 | 3GPP TS 26.501 5.10 | 3GPP TS 26.510 + 26.512
**Data collection, reporting and exposure** | 3GPP TS 26.501 4.0.12 | 3GPP TS 26.501 5.11 | 3GPP TS 26.510 + 26.512

## Creation of Provisioning Session
Note that before the required features of the 5GMS System can be used by 5GMS Clients, they are first provisioned by a 5GMS Application Provider creating one or more _Provisioning Sessions_. The 5GMSd Application Provider can then specify one or more 5GMSd features in the Provisioning Session.

The Provisioning Session information may include Content Hosting Configurations, Content Preparation Templates, Server Certificates, Policy Templates, a Consumption Reporting Configuration, Metrics Reporting Configurations, Edge Resources Configurations and Event Data Processing Configurations.

## Retrieval of Service Access Information
The Service Access Information is the set of parameters and addresses which are needed by the 5GMSd Client to activate and control the reception of a downlink streaming session, and to report service/content consumption and/or QoE metrics. 
The Service Access Information may be provided together with other service announcement information using M8d. Alternatively, the 5GMSd Client fetches the Service Access Information from the 5GMSd AF.
