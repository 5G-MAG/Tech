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
  /* Color Variables - Default: Light Mode */
  :root {
    --p-text-main: #1a1a1a;
    --p-text-muted: #707070; /* Gray for optional steps */
    --p-text-alert: #cf222e; /* Red for key requests */
    --p-badge-csp: #24292f;
  }

  /* Automatic Dark Mode Support */
  @media (prefers-color-scheme: dark) {
    :root {
      --p-text-main: #e6edf3;
      --p-text-muted: #8b949e;
      --p-text-alert: #ff7b72;
      --p-badge-csp: #30363d;
    }
  }

  /* Theme-toggle support for just-the-docs theme */
  [data-theme='dark'] .proc-wrapper {
    --p-text-main: #e6edf3;
    --p-text-muted: #8b949e;
    --p-text-alert: #ff7b72;
    --p-badge-csp: #30363d;
  }

  .proc-wrapper {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    max-width: 1000px;
    margin: 20px 0;
    line-height: 1.5;
  }

  /* Phase Header Bars */
  .p-header {
    display: flex;
    align-items: center;
    padding: 10px 18px;
    border-radius: 50px;
    font-weight: 700;
    margin-bottom: 20px;
    margin-top: 30px;
    color: #ffffff !important;
  }

  /* Phase Number Circle */
  .p-circle {
    background: #ffffff !important;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 12px;
    font-size: 0.85rem;
    font-weight: 900;
  }

  /* Standard Entry Row */
  .p-entry {
    display: flex;
    align-items: flex-start; /* Keeps actor at the top of the text block */
    gap: 15px;
    margin-left: 15px;
    margin-bottom: 18px;
  }

  /* Actor Column (consistent width) */
  .p-actors {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 55px; /* Ensures text descriptions always align */
    flex-shrink: 0;
  }

  /* Badge Pills */
  .p-pill {
    padding: 2px 0;
    border-radius: 20px;
    font-size: 10px;
    font-weight: 800;
    color: #ffffff !important;
    text-align: center;
    width: 55px;
    display: block;
  }

  /* Actor Colors */
  .p-pill-asp { background-color: #00a3cc !important; }
  .p-pill-csp { background-color: var(--p-badge-csp) !important; }
  
  /* Collaborative Plus Sign (Step 0 only) */
  .p-plus-sign {
    font-weight: bold;
    font-size: 14px;
    margin: 1px 0;
    color: var(--p-text-main) !important;
  }

  /* Text Semantic Colors */
  .p-content { color: var(--p-text-main) !important; font-size: 15px; padding-top: 2px;}
  .p-content-m { color: var(--p-text-muted) !important; font-size: 15px; padding-top: 2px;}
  .p-content-a { color: var(--p-text-alert) !important; font-size: 15px; font-weight: 500; padding-top: 2px;}
  .p-content-a u { text-underline-offset: 3px; font-weight: 600; }
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
