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

1. TOC
{:toc}

# Using CAMARA APIs (and Network Services) for Content Production & Contribution

This is a list of CAMARA APIs suitable to be used in the context of Connectivity Quality Management: [Network API Initiatives under analysis including CAMARA Project and 3GPP APIs](../Network_API_Initiatives.html).

Their mapping to the context of Content Production & Contribution is below.

## How to book QoS before being at or at the location?

First step is the ability to discover QoS profiles available at a given location and time. This step requires:
  * Mechanism to obtain available QoS profiles
  * Indication of a service area and/or time/duration

<table>
  <tr>
    <td markdown="span" align="left"><b>Mechanism to obtain available QoS profiles<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSProfiles.html">QoS Profiles API</a></b> the QoS profile parameters available in the network can be retrieved. No information about the service area is linked to such request.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_DedicatedNetworks.html">Dedicated Networks - Network Profiles API</a></b> it is possible to obtain the list of available Network Profiles which link the QoS Profile with additional information on the aggregated UL/DL throughput for a maximum number of devices.</td>
  </tr>
</table>

<table>
  <tr>
    <td markdown="span" align="left"><b>Identification of a service area and/or time/duration<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">In general the available profiles are listed for the network, not for a specific location or time/duration.</td>
  </tr>
</table>

With the information in the previous step, it should be possible to book QoS (to reserve network resources) for a given application or device for the intended service area and/or time/duration. This step requires:
  * Mechanism to create a booking linking a profile to a service area and time/duration.
  * The previous mechanism including information about the application server and/or device.

<table>
  <tr>
    <td markdown="span" align="left"><b>Mechanism to create a booking linking a profile to a service area and time/duration<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_DedicatedNetworks.html">Dedicated Networks - Network Profiles API</a></b> it is possible to request the creation of a dedicated network linking a QoS profile with a service area and time/duration. Therefore, this would comprise the booking of resources for a specific QoS Profile, a maximum number of devices which can make use of it, the service area and the time/duration.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_NetworkSliceBooking.html">Network Slice Booking API</a></b> it is possible to request the creation of a session with the expected service time, service area, and QoS profile. The number of devices can be specified in the QoS profile.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSBooking.html">QoS Booking API</a></b> it is possible to request the creation of a QoS booking specifying the QoS profile, application server details, device details, service area and time/duration.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSBookingAssignment.html">QoS Booking & Assignment - QoS Booking API</a></b> it is possible to request the creation of a QoS booking specifying the QoS profile, number of devices, service area and time/duration.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSProvisioning.html">QoS Provisioning API</a></b> it is possible to request the creation of a QoS booking specifying the QoS profile and the device. No information about the service area nor time/duration are provided.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QualityonDemand.html">Quality on Demand API</a></b> it is possible to request the creation of a QoS booking specifying the QoS profile, application server details, device details, and time/duration. No information about the service area is provided.</td>
  </tr>
</table>

### How to book QoS once already at the location?

All the mechanisms described above would allow the booking of QoS when already at the location. However, the <b><a href="../CAMARA_QoSProvisioning.html">QoS Provisioning API</a></b> and <b><a href="../CAMARA_QualityonDemand.html">Quality on Demand API</a></b> are particularly targetted to this scenario given it is not possible to define the service area in which they are applicable beforehand.

### How to book QoS for a known device?

All the mechanisms described above would allow to exploit network resources for any device. However, the <b><a href="../CAMARA_QoSBooking.html">QoS Booking API</a></b>, <b><a href="../CAMARA_QoSProvisioning.html">QoS Provisioning API</a></b> and <b><a href="../CAMARA_QualityonDemand.html">Quality on Demand API</a></b> would imply knowledge of the devices for which the booking is requested.

### How to book QoS for unknown devices?

All the mechanisms described above would allow to exploit network resources for any device. However, if devices are not known yet at the time of booking, it is possible to use the <b><a href="../CAMARA_DedicatedNetworks.html">Dedicated Networks - Network Profiles API</a></b>, <b><a href="../CAMARA_NetworkSliceBooking.html">Network Slice Booking API</a></b> and <b><a href="../CAMARA_QoSBookingAssignment.html">QoS Booking & Assignment - QoS Booking API</a></b> to request the booking of resources without committing to use a particular device.

## How to use the network resources?

First step is to have booked the network resources either for any device, a given number of devices or a concrete device. This implies following one of the steps below:
* Assingment and management of the booked network resources to a device
* Direct usage of the network resources when a device just connects to the network

<table>
  <tr>
    <td markdown="span" align="left"><b>Assingment of the booked network resources to a particular device<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSBookingAssignment.html">QoS Booking and Assignment - Device Assignment API</a></b> it is possible to assign a device to an existing QoS booking.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_DedicatedNetworks.html">Dedicated Network - Accesses API</a></b> it is possible to assign a device to an existing network profile</td>
  </tr>
</table>

<table>
  <tr>
    <td markdown="span" align="left"><b>Direct usage of the network resources when a device just connects to the network<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_NetworkSliceBooking.html">Network Slice Booking API</a></b> it is possible to use the network resources when a device connects to the network.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSBooking.html">QoS Booking API</a></b> it is possible to use the network resources when a device connects to the network.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSProvisioning.html">QoS Provisioning API</a></b> it is possible to use the network resources when a device connects to the network.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QualityonDemand.html">Quality on Demand API</a></b> it is possible to use the network resources when a device connects to the network.</td>
  </tr>
</table>

## How to exchange devices during runtime?

In the event that a device need to be exchanged or the booked resources should be assing to a different device, the following alternatives exist:
* Creating a new booking for a new device before releasing the current device
* Separation of the QoS booking w.r.t. to the device, enabling re-assignment of QoS booking.

<table>
  <tr>
    <td markdown="span" align="left"><b>Creating a new booking for a new device before releasing the current device<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSBooking.html">QoS Booking API</a></b> a new booking for a specific device should be created.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSProvisioning.html">QoS Provisioning API</a></b> a new booking for a specific device should be created.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QualityonDemand.html">Quality on Demand API</a></b> a new booking for a specific device should be created.</td>
  </tr>
</table>

{: .warning }
With the previous mechanisms there is no guarantee that new resources are available. Releasing the previous device will also imply no guarantee that those will remain available for a new booking.

<table>
  <tr>
    <td markdown="span" align="left"><b>Separation of the QoS booking w.r.t. to the device, enabling re-assignment of QoS booking<b/></td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_DedicatedNetworks.html">Dedicated Network - Accesses API</a></b> it is possible to request the assignment or release of a device to an existing network profile</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_NetworkSliceBooking.html">Network Slice Booking API</a></b> it is possible to bring a new device which will exploit the booked network resources.</td>
  </tr>
  <tr>
    <td markdown="span" align="left">By means of the <b><a href="../CAMARA_QoSBookingAssignment.html">QoS Booking & Assignment - Device Assignment API</a></b> it is possible to request the assignment or release of devide to an existing QoS booking.</td>
  </tr>
</table>

## How to obtain notifications about the abiliy of a network to support the requirements of an application?

These are different alternatives, including reception of a one-shot notification (e.g. for checking whether the network is able to meet certain requirements at a given instant of time) and a subcription to receive notifications (more useful during runtime).

### A one-shot notification
The pre-requisite is to create an Application Profile by invoking the [**Application Profiles API**]((../CAMARA_ApplicationProfiles.html)) with a series of user-defined network quality thresholds.
Following this step, the [**Connectivity Insights API**](../CAMARA_ConnectivityInsights.html) can be invoked which reply contains a message about the confidence of the network in meeting the network quality thresholds.

### Subscribing to regular notifications
The pre-requisite is to create an Application Profile by invoking the [**Application Profiles API**]((../CAMARA_ApplicationProfiles.html)) with a series of user-defined network quality thresholds.
Following this step, the [**Connectivity Insights Subscriptions API**](../CAMARA_ConnectivityInsightsSubscriptions.html) can be invoked to receive regular notifications (up to a defined limit) about the confidence of the network in meeting the network quality thresholds.
