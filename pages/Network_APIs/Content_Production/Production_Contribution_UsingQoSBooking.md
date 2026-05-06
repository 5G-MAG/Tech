---
layout: default
title: QoS Booking
parent: Using CAMARA APIs
grand_parent: Content Production & Contribution
nav_order: 1
has_children: false
---

<img src="../../../assets/images/Banner_NetworkAPIs.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Using CAMARA APIs: QoS Booking for Content Production & Contribution

Find more information about [**QoS Booking API**](../CAMARA_QoSBooking.html).

A user of a media application would like to request the assignment of a QoS Profile to a device for a given period of time and service area. The following steps are executed:

# Workflow and Architecture

This is a high-level figure with the entities involing APIs and the devices involved:

<figure>
  <img src="./images/figure_qosbooking.png" width="80%">
</figure>

## General Workflow

The following steps are executed:

<div class="proc-wrapper">

  <div class="p-header" style="background-color: #7c52e4;">
    <div class="p-circle" style="color: #7c52e4;">0</div> Pre-conditions
  </div>
  
  <div class="p-entry">
    <div class="p-actors">
      <span class="p-pill p-pill-asp">ASP</span>
      <div class="p-plus-sign">+</div>
      <span class="p-pill p-pill-csp">CSP</span>
    </div>
    <div class="p-content">
      On-boarding of the ASP and Negotiation<br>
      - &nbsp;Sign up and access credentials<br>
      - &nbsp;Selection / Request for QoS Profiles
    </div>
  </div>

  <div class="p-header" style="background-color: #f38d3c;">
    <div class="p-circle" style="color: #f38d3c;">1</div> Before using the network
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-asp">ASP</span></div>
    <div class="p-content-m">1.0a. Discovery of available and eligible QoS Profiles (optional)</div>
  </div>

  <div class="p-header" style="background-color: #74b85c;">
    <div class="p-circle" style="color: #74b85c;">2</div> During operation
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-asp">ASP</span></div>
    <div class="p-content-a">2.1. <u>Request</u> of <u>Creation</u> of QoS Session</div>
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-asp">ASP</span></div>
    <div class="p-content">2.2. Device establishes connection</div>
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-asp">ASP</span></div>
    <div class="p-content-a">2.3. Usage of API capabilities</div>
  </div>

  <div class="p-header" style="background-color: #cc0000;">
    <div class="p-circle" style="color: #cc0000;">3</div> Dismantling
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-asp">ASP</span></div>
    <div class="p-content-a">3.1a. <u>Deletion</u> of QoS Session</div>
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-csp">CSP</span></div>
    <div class="p-content">3.1b. Or the CSP simply tears the QoS session down</div>
  </div>

</div>

## Step 0: Pre-conditions
* The API invoker needs to have signed up with the API provider.
* qosProfiles have already been defined and made available by the network operator.
* Names of such qosProfiles have been disclosed to the user so they can be used when invoking APIs.

## Step 1: Before using the network
Details of the already arranged QoS Profile can be retrieve with **GET /qos-profiles/{name}**, using the [QoS Profiles API](../CAMARA_QoSProfiles.html).

## Step 2: During operation

### 2.1 Requests creation of QoS Booking

With **POST /device-qos-bookings** passing the `qosProfile`, `applicationServer`, `applicationServerPorts`, `device` object, `devicePorts`, `startTime`, `duration`, `serviceArea`.

### 2.2 Device establishes connection

### 2.3 Usage of API capabilities

A series of operations to delete the QoS session or extending its duration are available:

**POST /retrieve-device-qos-bookings** - Retrieve device QoS Bookings

**GET /device-qos-bookings/{bookingId}** - Obtain device QoS Booking details

## Step 3: Dismantling

When reaching the duration the QoS Booking may be teared down. A greceful way of tearing down will delete the QoS session by `id`.

**DELETE /device-qos-bookings/{bookingId}** deletes the QoS Booking

---

## 5G-MAG's Self-Assessment
* The QoS Booking APIs can be invoked before the actual usage of the network starts to ensure that the requested capabilities are "reserved" for the specific area, time window and device.
* During the event a device will have access to the QoS Booking.
* This API may be suitable for a setup where a single device requires access to network resources (e.g. MoJo). However this is impractical for a Media Production setup with multiple devices as not all of them may be running at the same time. Making different QoS bookings for each of them while not requiring access to network resources concurrently may result in inneficiencies.

Potential improvements:
- It is unclear how to associate devices to make use of the resources. As it stands, the device is granted the booking as soon as connected to the network under the service area and for the specified duration.
- It is unclear how to update the booking. In the event that a device would need to be exchanged, deleting and creating a new booking may lead to loosing the ability to reserve resources during operation.
