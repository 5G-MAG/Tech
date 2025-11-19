---
layout: default
title: Using CAMARA APIs
parent: Content Production & Contribution
grand_parent: Network APIs
nav_order: 2
has_children: false
---

<img src="../../../assets/images/Banner_API.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Using CAMARA APIs (and Network Services) for Content Production & Contribution

This is a list of CAMARA APIs suitable to be used in the context of Connectivity Quality Management: [Network API Initiatives under analysis including CAMARA Project and 3GPP APIs](../Network_API_Initiatives.html).

## How to book QoS when already at the location?
Booking resources in advance is possible by using other APIs, which will then allow to obtain QoS at a given location and time... More details in the next sub-section.

### Creating a QoS session with "Quality on Demand"
It is possible to create a QoS session by invoking the [**Quality on Demand API**](../CAMARA_QualityonDemand.html) passing a [**QoS Profile**](../CAMARA_QoSProfiles.html), details of the application server (e.g. the end-point of the uplink video contribution) and device, the service time.
This is assumed to be invoked when already at the location.

### Provisioning QoS for a device
It is possible to provision QoS for a device by invoking the [**QoS Provisioning API API**](../CAMARA_QoSProvisioning.html) passing a [**QoS Profile**](../CAMARA_QoSProfiles.html), and details of the device. This QoS profile will be assigned to the device anytime it is connected to the network.

## How to book in advance network resources for a single device, in a given area and period of time?

### Setting up a "Dedicated Network"
This scenario can be covered by invoking the [**Dedicated Networks API**](../CAMARA_DedicatedNetworks.html). This involves retrieving available **Network Profiles** in the network with some additional information on the aggregated UL/DL throughput for a maximum number of devices (in this case it will be for a single one). The parameters the "dedicated network" support are indicated per [**QoS Profile**](../CAMARA_QoSProfiles.html).
After this, a request can be created with such Network Profile, the service time start and end as well as the service area.
Once this is established, a device can be attached to access such "dedicated network" when required within the service area and for the specificed duration.

### Booking QoS with "QoS Booking"
It is possible to book QoS by invoking the [**QoS Booking API**](../CAMARA_QoSBooking.html) passing a [**QoS Profile**](../CAMARA_QoSProfiles.html), details of the application server (e.g. the end-point of the uplink video contribution) and device, the service time and service area.
A device connecting to the network at the given time and within the service area will be able to expoit the QoS booking.

### Booking a "Network Slice"
It is possible to book a "network slice" by invoking the [**Network Slice Booking API**](../CAMARA_NetworkSliceBooking.html) with additional QoS parameters linked to the network slice.
A device connecting to the network at the given time and within the service area will be able to expoit the "network slice" properties.

## How to book in advance network resource for a media production scenario involving multiple devices in a given area and period of time?

### Setting up a "Dedicated Network"
This scenario can be covered by invoking the [**Dedicated Networks API**](../CAMARA_DedicatedNetworks.html). This involves retrieving available **Network Profiles** in the network with some additional information on the aggregated UL/DL throughput for a maximum number of devices (in this case it will be for a single one). The parameters the "dedicated network" support are indicated per [**QoS Profile**](../CAMARA_QoSProfiles.html).
After this, a request can be created with such Network Profile, the service time start and end as well as the service area.
Once this is established, a device can be attached to access such "dedicated network" when required within the service area and for the specificed duration.
Several devices can be attached to the same profile. Or multiple profiles can be created with devices being assinged/revoked during runtime.

This API is particularly interesting as the booking of resources will not be revoked when a device is exchanged or released.

### Setting up a "QoS Booking and Assignment"
This scenario can be covered by invoking the [**QoS Booking and Assignment API**](../CAMARA_QoSBookingAssignment.html). This involves indicating a number of devices that will be part of the QoS booking, the [**QoS Profile**](../CAMARA_QoSProfiles.html), start time, duration and service area.

Once the booking is created, devices can be assinged and releases.

This API is particularly interesting as the booking of resources will not be revoked when a device is exchanged or released.

## How to obtain a notification about the abiliy of a network to support the requirements of my application?

These are different alternatives.

### A one-shot notification
The pre-requisite is to create an Application Profile by invoking the [**Application Profiles API**]((../CAMARA_ApplicationProfiles.html)) with a series of user-defined network quality thresholds.
Following this step, the [**Connectivity Insights API**](../CAMARA_ConnectivityInsights.html) can be invoked which reply contains a message about the confidence of the network in meeting the network quality thresholds.

### Subscribing to regular notifications
The pre-requisite is to create an Application Profile by invoking the [**Application Profiles API**]((../CAMARA_ApplicationProfiles.html)) with a series of user-defined network quality thresholds.
Following this step, the [**Connectivity Insights Subscriptions API**](../CAMARA_ConnectivityInsightsSubscriptions.html) can be invoked to receive regular notifications (up to a defined limit) about the confidence of the network in meeting the network quality thresholds.
