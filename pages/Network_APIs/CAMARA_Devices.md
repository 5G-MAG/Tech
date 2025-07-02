---
layout: default
title: CAMARA Draft devics
parent: Network API Analysis
grand_parent: Network APIs
nav_order: 3
has_children: false
---










OTHER APIs not yet analysed

### [DeviceIdentifier](https://github.com/camaraproject/DeviceIdentifier)

#### Scope
- Service APIs for “Device Identifier API” (see API Backlog)
- It provides the customer with the ability to:
  - Retrieve the current identity (IMEI) of the mobile device being used by a given mobile subscriber
  - Retrieve the type (manufacturer and model) of the mobile device being used by a given mobile subscriber

### [DeviceLocation](https://github.com/camaraproject/DeviceLocation)

#### Scope
- Service APIs for “Device Location” (see APIBacklog)
- It provides the customer with the ability to:
  - verify the location of a device (location-verification).
  - retrieve the location of a device (location-retrieval).
  - subscribe and receive notifications about a device entering or leaving certain location (geofencing-subscriptions).
  - NOTE: The scope of this API family should be limited (at least at a first stage) to 4G and 5G.

### [DeviceStatus](https://github.com/camaraproject/DeviceStatus)

#### Scope
- Service APIs for “Device Status” (see APIBacklog)
- It provides the API consumer with the ability to:
  - check if a device is reachable or is not connected to the network
  - check if a device is roaming, and in which country
  - receive notifications if the connectivity or roaming status of the device changes
