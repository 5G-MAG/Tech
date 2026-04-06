---
layout: default
title: 5G Broadcast
has_children: true
nav_order: 3
---

<img src="../assets/images/Banner_5GBroadcast.png" /> 

# 5G Broadcast: TV, Radio and Emergency Alerts - Documentation

## Introduction

<iframe width="60%" height="520" src="../docs/Tech_5GBroadcast.pdf"></iframe>

[Download the Slidedeck](../docs/Tech_5GBroadcast.pdf){: .btn .btn-blue }

## Execution Plan

[Go to the Execution Plan Kanban Board](https://github.com/orgs/5G-MAG/projects/44/views/7){: .btn .btn-blue }

<div id='kanban-display' style='font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;'>
<p style='font-size: 12px; color: #586069; margin-bottom: 20px;'>Last Sync: {{ site.data.roadmaps.last_updated }}</p>

{% assign target_label = "Topic: 5G Broadcast" %}

<h3 style='border-bottom: 1px solid #eaecef; padding-bottom: 8px; margin-top: 30px; color: #24292e;'>Work in Progress</h3>
    {% for item in site.data.roadmaps.all_items %}
      {% if item.status == "Work in Progress" and item.labels contains target_label %}
        <div style="margin-bottom: 12px; padding: 15px; border: 1px solid #d1d5da; border-radius: 8px; background-color: #ffffff; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <a href="{{ item.url }}" style="text-decoration: none; color: #0366d6; font-size: 15px; font-weight: 600; display: block;">{{ item.title }}</a>
        </div>
      {% endif %}
    {% endfor %}

<h3 style='border-bottom: 1px solid #eaecef; padding-bottom: 8px; margin-top: 30px; color: #24292e;'>Completed</h3>
    {% for item in site.data.roadmaps.all_items %}
      {% if item.status == "Completed" and item.labels contains target_label %}
        <div style="margin-bottom: 12px; padding: 15px; border: 1px solid #d1d5da; border-radius: 8px; background-color: #ffffff; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <a href="{{ item.url }}" style="text-decoration: none; color: #0366d6; font-size: 15px; font-weight: 600; display: block;">{{ item.title }}</a>
        </div>
      {% endif %}
    {% endfor %}
</div>

---

## Information related to Standards

[Standards: LTE-based 5G Broadcast](../../Standards/pages/lte-based-5g-broadcast.html){: .btn .btn-blue }

[Standards: Multimedia Delivery Protocols](../../Standards/pages/multimedia-content-delivery.html){: .btn .btn-blue }

[Standards: DVB-I Services over 5G Systems](../../Standards/pages/dvb-i-5g.html){: .btn .btn-blue }


---

## Technical Documentation

The following resources are available:

### General information about 5G Broadcast

* [**LTE-based 5G Terrestrial Broadcast for TV and radio distribution**](../docs/Explainer_LTEbased_5G_Terrestrial_Broadcast.pdf)
* [**Spectrum for LTE-based 5G Terrestrial Broadcast**](../docs/Explainer_Spectrum_for_LTEbased_5G_Terrestrial_Broadcast.pdf)

#### VideoTech

* [**5G Media Streaming over eMBMS (3GPP Release 17)**](./videos.html#5g-media-streaming-over-embms-3gpp-release-17)

### Analysis of Time-Frequency Interleaving for 5G Broadcast
* [**Time and Frequency Interleaving for broadcast services in 3GPP Systems**](../docs/Time_and_Frequency_Interleaving_for_broadcast_services_in_3GPP_Systems.pdf)

###  Deployment Profiles and Operational Parameters
* [**5G Broadcast Deployment Profiles**](./5gbroadcast/deployment_profiles.html).
* [**5G Broadcast Operational Parameters in Use**](./5gbroadcast/parameters_in_use.html).
