---
layout: default
title: QoS Booking and Assignment
parent: Using CAMARA APIs
grand_parent: Content Production & Contribution
nav_order: 2
has_children: false
---

<img src="../../../assets/images/Banner_NetworkAPIs.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Using CAMARA APIs: QoS Booking and Assignment for Content Production & Contribution

Find more information about [**QoS Booking and Assignment API**](../CAMARA_QoSBookingAssignment.html).

# Purpose

A user of a media application would like to request the assignment of a QoS Profile to a device for a given period of time and service area.

# Workflow and Architecture

This is a high-level figure with the entities involing APIs and the devices involved:

<figure>
  <img src="./images/figure_qosbookingassignment.png" width="80%">
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
    <div class="p-content-m">1.0. Discovery of available and eligible QoS Profiles (optional)</div>
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-asp">ASP</span></div>
    <div class="p-content-a">1.1. <u>Request</u> of <u>Creation</u> of QoS Booking</div>
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-csp">CSP</span></div>
    <div class="p-content">1.2. Assessment of QoS Booking reservation and change of status</div>
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-asp">ASP</span></div>
    <div class="p-content-a">1.3. <u>Request</u> of Device <u>Assignment</u> for the QoS Booking</div>
  </div>

  <div class="p-header" style="background-color: #74b85c;">
    <div class="p-circle" style="color: #74b85c;">2</div> During operation
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-csp">CSP</span></div>
    <div class="p-content">2.1. QoS Booking is activated</div>
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
    <div class="p-content-a">3.1a. <u>Release</u> of Device Assignment and <u>Deletion</u> of QoS Booking</div>
  </div>

  <div class="p-entry">
    <div class="p-actors"><span class="p-pill p-pill-csp">CSP</span></div>
    <div class="p-content">3.1b. Or the CSP simply tears the Dedicated Network down</div>
  </div>

</div>

## Step 0: Pre-conditions
* The API invoker needs to have signed up with the API provider.
* qosProfiles have already been defined and made available by the network operator.
* Names of such qosProfiles have been disclosed to the user so they can be used when invoking APIs.

## Step 1: Before using the network
Details of the already arranged QoS Profile can be retrieve with **GET /qos-profiles/{name}**, using the [QoS Profiles API](../CAMARA_QoSProfiles.html).

### 1.1 Requests creation of QoS Booking for a given number of devices

With **POST /qos-bookings** passing the `numDevices`, `qosProfile`, `startTime`, `duration`, `serviceArea`.

## Step 2: During operation

### 2.1 Assing the QoS Booking to a specific Device

**POST /qos-bookings/{bookingId}/devices/assign** passing the BookingId from the previous step and a `device` object to assign the QoS Booking to a specific device.

### 2.2 Device establishes connection

### 2.3 Usage of API capabilities

A series of operations to delete the QoS Booking and Assignment are available:

### QoS Booking and Assignment - QoS Booking API
  * **POST /qos-bookings** with a request body containing `numDevices`, `qosProfile`, `startTime`, `duration`, `serviceArea`, it triggers a new booking in advance and assign this reserved booking profile to one or more devices when the devices are ready. The response includes a `bookingId`.
    * Dependency: Requires `qosProfile` which can be retrieved from a previous call to the [**QoS Profiles API**](./CAMARA_QoSProfiles.html).
  * **GET /qos-bookings/{bookingId}** - gets booking information for the given bookingId
  * **DELETE /qos-bookings/{bookingId}** - Cancel an existing booking and release resources related to that booking.

### QoS Booking and Assignment - Device Assignment API
  * **POST /qos-bookings/{bookingId}/devices/assign** with a request body containing `device` object, allows the end user to assign one or more devices to the existing QoS Booking.
  * **GET /qos-bookings/{bookingId}/devices** - allows the end user to retrieve the list of devices assigned to the existing QoS Booking.
  * **POST /qos-bookings/{bookingId}/devices/release** with a request body containing `device` object - Release one or more already assigned devices. This is a synchronous call.
  * **POST /qos-bookings/retrieve** with a request body containing `device` object - Querying for QoS Booking resource information details for a device. Returns the QoS booking information for a given device. A device may have multiple bookings (for several times and locations), thus the response is an array

## Step 3: Dismantling

When reaching the duration the QoS Booking may be teared down. A greceful way of tearing down will delete the QoS session by `id`.

**DELETE /qos-bookings/{bookingId}** deletes the QoS Booking

---

## 5G-MAG's Self-Assessment
* QoS Booking can be invoked before the actual usage of the network starts to ensure that the requested capabilities are "reserved" for the specific area, time window and a given number of devices.
* Before or during the event a device will be assigned have access to the QoS booking.

Potential improvements:
- Unlike other similar APIs there is no information about the application server. It is unclear what would be the endpoint to which throughput, jitter, latency and other parameters would apply.
- The procedure is very similar to Dedicated Networks. There seems to be redundancy with QoS Booking
- The use of the same name "QoS Booking" is misleading with the other API called "QoS Booking"
