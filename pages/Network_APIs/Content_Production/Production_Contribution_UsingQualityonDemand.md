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
  .process-container {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: transparent;
    padding: 10px 0;
    max-width: 1000px;
    margin: 20px 0;
  }

  .phase-bar {
    display: flex;
    align-items: center;
    padding: 10px 18px;
    border-radius: 50px;
    font-weight: 700;
    margin-bottom: 18px;
    margin-top: 30px;
    color: #ffffff !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  .phase-num {
    background: #ffffff !important;
    border-radius: 50%;
    width: 26px;
    height: 26px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 12px;
    font-size: 0.9rem;
    font-weight: 900;
  }

  .row-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-left: 15px;
    margin-bottom: 16px;
  }

  .badge-stack {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 45px;
    font-size: 14px;
    font-weight: bold;
    color: #1a1a1a !important;
  }

  .p-badge {
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 800;
    color: #ffffff !important;
    text-align: center;
    width: 100%;
  }

  .p-asp { background-color: #00a3cc !important; }
  .p-csp { background-color: #314b6d !important; }

  /* Visible text for white background */
  .p-text-black { 
    color: #000000 !important; 
    font-size: 15px; 
    line-height: 1.5;
    font-weight: 450;
  }

  .p-text-gray { 
    color: #707070 !important; 
    font-size: 15px; 
    line-height: 1.5;
  }

  .p-text-red { 
    color: #e60000 !important; 
    font-size: 15px; 
    line-height: 1.5; 
    font-weight: 500; 
  }
  
  .p-text-red u { text-underline-offset: 3px; }
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

<div class="process-container">

  <div class="phase-bar" style="background-color: #7c52e4;">
    <div class="phase-num" style="color: #7c52e4;">0</div> Pre-conditions
  </div>
  
  <div class="row-item">
    <div class="badge-stack">
      <span class="p-badge p-asp">ASP</span>
      <div style="margin: 2px 0;">+</div>
      <span class="p-badge p-csp">CSP</span>
    </div>
    <div class="p-text-black">
      On-boarding of the ASP<br>
      - &nbsp;Sign up and access credentials<br>
      - &nbsp;Selection / Request for Network Profiles and Network Service Areas
    </div>
  </div>

  <div class="phase-bar" style="background-color: #f38d3c;">
    <div class="phase-num" style="color: #f38d3c;">1</div> Before using the network
  </div>

  <div class="row-item">
    <span class="p-badge p-asp">ASP</span>
    <div class="p-text-gray">
      1.0a. Discovery of available and eligible Network Profiles (optional)<br>
      1.0b. Discovery of available and eligible Network Service Areas (optional)
    </div>
  </div>

  <div class="row-item">
    <span class="p-badge p-asp">ASP</span>
    <div class="p-text-red">1.1. <u>Request</u> of <u>Reservation</u> for Dedicated Network</div>
  </div>

  <div class="row-item">
    <span class="p-badge p-csp">CSP</span>
    <div class="p-text-black">1.2. Assessment of Dedicated Network reservation and change of status</div>
  </div>

  <div class="row-item">
    <span class="p-badge p-asp">ASP</span>
    <div class="p-text-red">1.3. <u>Request</u> of Device <u>Access</u> for Dedicated Network</div>
  </div>

  <div class="phase-bar" style="background-color: #74b85c;">
    <div class="phase-num" style="color: #74b85c;">2</div> During operation
  </div>

  <div class="row-item">
    <span class="p-badge p-csp">CSP</span>
    <div class="p-text-black">2.1. Dedicated Network is activated</div>
  </div>

  <div class="row-item">
    <span class="p-badge p-asp">ASP</span>
    <div class="p-text-black">2.2. Device establishes connection</div>
  </div>

  <div class="row-item">
    <span class="p-badge p-asp">ASP</span>
    <div class="p-text-red">2.3. Usage of API capabilities</div>
  </div>

  <div class="phase-bar" style="background-color: #cc0000;">
    <div class="phase-num" style="color: #cc0000;">3</div> Dismantling
  </div>

  <div class="row-item">
    <div class="badge-stack">
      <span class="p-badge p-asp">ASP</span>
      <div style="margin: 2px 0;">+</div>
      <span class="p-badge p-csp">CSP</span>
    </div>
    <div class="p-text-black">
      <span class="p-text-red">3.1a. <u>Deletion</u> of Device Access and Dedicated Network</span><br>
      3.1b. Or the CSP simply tears the Dedicated Network down
    </div>
  </div>

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
