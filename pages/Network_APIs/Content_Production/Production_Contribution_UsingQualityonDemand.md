---
layout: default
title: Quality on Demand
parent: Using CAMARA APIs
grand_parent: Content Production & Contribution
nav_order: 1
has_children: false
---

<img src="../../../assets/images/Banner_NetworkAPIs.png" /> 

<style>
  .process-wrapper {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: transparent; /* Changed to transparent */
    padding: 24px;
    border-radius: 12px;
    color: #fff;
    max-width: 100%;
    margin: 20px 0;
  }
  .step-header {
    display: flex;
    align-items: center;
    padding: 10px 20px;
    border-radius: 50px;
    font-weight: 600;
    margin-bottom: 16px;
    margin-top: 24px;
    color: white !important;
  }
  .step-num {
    background: #fff;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 12px;
    font-size: 0.85rem;
    font-weight: bold;
  }
  .process-row {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-left: 10px;
    margin-bottom: 12px;
  }
  .badge {
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 800;
    min-width: 40px;
    text-align: center;
  }
  .badge-asp { background-color: #17a2b8; color: white; }
  .badge-csp { background-color: #384d62; color: white; }
  .text-gray { color: #8b949e; font-size: 14px; line-height: 1.6; }
  .text-highlight { color: #ff6b6b; font-size: 14px; line-height: 1.6; font-weight: 500; }
  .text-highlight ins { text-decoration: underline; text-underline-offset: 3px; }
</style>

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Using CAMARA APIs: Quality on Demand for Content Production & Contribution

Find more information about [**Quality on Demand API**](../CAMARA_QualityonDemand.html).

A user of a media application would like to request the creation of a QoS session for the connection between a device and an application server.

# Workflow and Architecture

This is a high-level figure with the entities involing APIs and the devices involved:

<figure>
  <img src="./images/figure_qualityondemand.png" width="80%">
</figure>

## General Workflow

The following steps are executed:

<div class="process-wrapper">

  <div class="step-header" style="background-color: #8957e5;">
    <div class="step-num" style="color: #8957e5;">0</div> Pre-conditions
  </div>
  <div class="process-row"><span class="badge badge-asp">ASP</span></div>
  <div class="process-row"><span class="badge badge-csp">CSP</span></div>
  <div class="process-row"><span class="badge badge-asp">ASP</span></div>

  <div class="step-header" style="background-color: #f0883e;">
    <div class="step-num" style="color: #f0883e;">1</div> Before using the network
  </div>
  <div class="process-row">
    <span class="badge badge-asp">ASP</span>
    <div class="text-gray">
      1.0a. Discovery of available and eligible Network Profiles (optional)<br>
      1.0b. Discovery of available and eligible Network Service Areas (optional)
    </div>
  </div>
  <div class="process-row">
    <span class="badge badge-asp">ASP</span>
    <div class="text-highlight">1.1. <ins>Request</ins> of <ins>Reservation</ins> for Dedicated Network</div>
  </div>
  <div class="process-row"><span class="badge badge-csp">CSP</span></div>
  <div class="process-row">
    <span class="badge badge-asp">ASP</span>
    <div class="text-highlight">1.3. <ins>Request</ins> of Device <ins>Access</ins> for Dedicated Network</div>
  </div>

  <div class="step-header" style="background-color: #3fb950;">
    <div class="step-num" style="color: #3fb950;">2</div> During operation
  </div>
  <div class="process-row"><span class="badge badge-csp">CSP</span></div>
  <div class="process-row"><span class="badge badge-asp">ASP</span></div>
  <div class="process-row">
    <span class="badge badge-asp">ASP</span>
    <div class="text-highlight">2.3. Usage of API capabilities</div>
  </div>

  <div class="step-header" style="background-color: #f85149;">
    <div class="step-num" style="color: #f85149;">3</div> Dismantling
  </div>
  <div class="process-row">
    <span class="badge badge-asp">ASP</span>
    <div class="text-highlight">3.1a. <ins>Deletion</ins> of Device Access and Dedicated Network</div>
  </div>
  <div class="process-row"><span class="badge badge-csp">CSP</span></div>

</div>

## Step 0: Pre-conditions
* The API invoker needs to have signed up with the API provider.
* qosProfiles have already been defined and made available by the network operator.
* Names of such qosProfiles have been disclosed to the user so they can be used when invoking APIs.

## Step 1: Before using the network
Details of the already arranged QoS Profile can be retrieve with **GET /qos-profiles/{name}**, using the [QoS Profiles API](../CAMARA_QoSProfiles.html).

An example of the QoS Profile, including status:

```
[
  {
    "name": "voice",
    "description": "QoS profile for video streaming",
    "status": "ACTIVE",
    "targetMinUpstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "maxUpstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "maxUpstreamBurstRate": {
      "value": 10,
      "unit": "bps"
    },
    "targetMinDownstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "maxDownstreamRate": {
      "value": 10,
      "unit": "bps"
    },
    "maxDownstreamBurstRate": {
      "value": 10,
      "unit": "bps"
    },
    "minDuration": {
      "value": 12,
      "unit": "Days"
    },
    "maxDuration": {
      "value": 12,
      "unit": "Days"
    },
    "priority": 20,
    "packetDelayBudget": {
      "value": 12,
      "unit": "Days"
    },
    "jitter": {
      "value": 12,
      "unit": "Days"
    },
    "packetErrorLossRate": 3,
    "l4sQueueType": "non-l4s-queue",
    "serviceClass": "real_time_interactive"
  }
]
```

## Step 2: During operation

### 2.1 Requests creation of QoS session

With **POST /sessions** passing the `device` object, `applicationServer` IP, `applicationServerPorts`, `devicePorts`, `qosProfile` and `duration`.

### 2.2 Device establishes connection

### 2.3 Usage of API capabilities

A series of operations to delete the QoS session or extending its duration are available:

**GET /sessions/{sessionId}** - Get QoS session information

**DELETE /sessions/{sessionId}** - Delete a QoS session

**POST /sessions/{sessionId}/extend** - Extend the duration of an active session

**POST /retrieve-sessions** - Get QoS session information for a device

## Step 3: Dismantling

When reaching the duration the QoS session may be teared down. A greceful way of tearing down will delete the QoS session by `id`.

**DELETE /sessions/{sessionId}** deletes a QoS session

---

## 5G-MAG's Self-Assessment
* A session may be created by establishing a level of QoS between the device and the application server for a given duration.
* It is assumed that the QoD API is invoked with the complete knowledge of device, application server, and at the given location.
* No information is given to the user on the availability of resources in an area.
* It is not possible to ensure availability of the QoS session before invoking at the location. A service area cannot be defined/requested, it is unclear whether this would be successful or not.
* On device failure, the QoS session needs to be deleted with no guarantee that a new one can be created.

Potential improvements:
- There is no information about the location or service area.
- Understanding opportunities to book QoS sessions in terms of duration and location/area would be useful as the user may be able to move and find a better coverage spot rather than being denied the establishment of QoS at the time and location in which it is requested.
