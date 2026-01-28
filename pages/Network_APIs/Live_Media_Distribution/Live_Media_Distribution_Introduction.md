---
layout: default
title: Live Media Distribution
parent: Network APIs
nav_order: 1
has_children: true
---

<img src="../../../assets/images/Banner_API.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Introduction: Live Media Distribution

For many people the internet is becoming their primary means of accessing TV and radio content, while for some the internet is already the only method they use.

As a result, content providers are increasingly interested in understanding how well their content is being delivered online, particularly when it is offered "over the top" (OTT), therefore with no ability to influence how networks would treat content to meet particlar quality of service (QoS) requirements. Similarly, network operators want insight into how well their networks are meeting consumers’ needs and expectations.

## Monitoring QoS
When it comes to monitoring QoS, content providers typically have sight of the two ends of the distribution chain: the source (often a CDN in this context) and the application running on a user device, such as a smartphone. For services delivered over Dynamic Adaptive Streaming over HTTP (MPEG-DASH), for example, it appears that QoS may be sufficiently described by the statistics of the time taken to deliver each segment i.e. the time to last byte (TTLB). This data can be readily obtained in the client app by timing how long it takes from each segment request to its receipt in full [ref].

If poor performance is detected the content provider can often rule out the CDN as a cause by inspecting the CDN logs.

Although content providers can also record radio access network (RAN) performance indicators such as cell ID, signal strength and quality, they have no direct visibility of the underlying network. Any issues not attributable to the CDN or insufficient signal are effectively lumped into the ‘network’, which appears to them as ‘The Cloud’.

**Figure goes here**

Content providers can measure ‘end to end’ performance via the client app and the CDN endpoints. Network operators have greater visibility of their network but may see the entire distribution chain.

Network operators, on the other hand, have far greater visibility of what is happening in their networks. Typically, however, for third party services where network operators don’t have access to the client app, they too typically lack visibility of the full distribution chain. In these cases, for example, interference to the uplink may prevent segment requests ‘reaching’ the network. Such events cannot be recorded by the network as an issue. From the operator’s perspective, the request simply does not exist, making it impossible to diagnose or attribute the underlying cause of any subsequent degraded experience.

# What we are doing

At 5G-MAG we’re investigating the possibility of logging relevant performance data through the client application and share it with the network operator. Standard ways of feeding back and sharing data would make the process easier and encourage such collaboration.

Please go to the following sections:
* [Reference Scenarios](./Live_Media_Distribution_Scenarios.html)
* [Workflows](./Live_Media_Distribution_Workflows.html)
* [Using Network APIs](./Live_Media_Distribution_UsingCAMARAAPIs.html)
