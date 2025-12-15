---
layout: default
title: Deployment profiles
parent: 5G Broadcast
nav_order: 0
has_children: true
---

<img src="../../assets/images/Banner_5GBC.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# 5G Broadcast - Deployment Profiles

## 5G Broadcast Receiver Profile A (example)

### Bands and bandwidth

The supported bandwidth for LTE-based 5G Broadcast in units of MHz are 6, 7 and 8.

The supported spectrum is a subset of the operating band n108 (as defined in clause 8.X):

Table 12.7.1-1 Subset of 5G terrestrial broadcast operating band n108 as minimum requirement.
Operating band on which subset is based	Uplink (UL) operating band
BS receive
UE transmit	Downlink (DL) operating band
BS transmit 
UE receive	Duplex Mode
	FUL_low   –  FUL_high
FDL_low  –  FDL_high

108
N/A	606 MHz	–	698 MHz	SDO


### Radio

Implementation of radio aspects in devices shall follow clause 7.3 and support the following features:

* MBMS-dedicated cells for 100% MBMS allocation
* Subcarrier spacings: 1.25 kHz, 2.5 kHz and 15 kHz.
* Service continuity for roaming/border situations
* Multiple services with different MCS within a carrier
* Support of MCS 1-26 (according to Table 7.1.7.1-1A. in 3GPP 36.213 18.2.0)
* Support for dual antenna reception
* Support of diversity reception with multiple antennas
* Multi-threading of 5G Broadcast and unicast, i.e. using unicast at the same time when receiving on 5G Broadcast

### Interfaces and protocols

Devices’ interfaces shall support the following delivery methods (according to 3GPP 26.346 18.0.0):

* MBMS Transparent Delivery Method
* MBMS Download Delivery Method

Devices shall support the following protocols (according to 3GPP 26.346 18.0.0):
* RTP (over transparent delivery method)
* DASH
* TSoverIP (over transparent delivery method)
* HLS (over transparent delivery method)
* FLUTE
* ROUTE (over transparent delivery method)

The following functionalities shall be supported:

* Service announcement (according to 3GPP 23.246 18.0.0)
* Bootstrap.multipart file (according to 3GPP 23.246 18.0.0)
* MBMS-URL (according to 3GPP 26.347 18.0.0)

### Codec

Devices shall support the following codecs:

* Audio: HE-AAC aacPlus, enhanced aacPlus, AC-3, AAC
* Video: H.264 High profile
* Video: H.265 (HEVC)
* Video: H.266 VVC
* CMAF, mp4, ISO BMFF
* MPEG-2 TS

### Miscellaneous

Devices shall support
* Free-to-air (FTA) mode
* Receive-only-mode (ROM)
* MFN support
* SFN support
* Service discovery strategy: 1. MBMS-URL, 2. Bootstrap.multipart file, 3. Service announcement
* PWS systems (according to clause 7.6) 

In case Time-Frequency-Interleaving and co-existence of Legacy Broadcast and 5G Broadcast in UHF are introduced in Release 19, both functionalities shall be supported.
