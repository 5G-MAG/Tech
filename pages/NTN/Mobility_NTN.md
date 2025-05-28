---
layout: default
title: Mobility Aspects NTN
parent: Non-Terrestrial Networks
nav_order: 2
has_children: false
---

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members as part of **WI: Content Delivery over NTNs** and **WI: Multicast Broadcast Services**
We welcome and encourage contributions from the broader community. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

# Aspects on Mobility for NTN
Non-Terrestrial Networks (NTNs) may use satellites, for example, to provide connectivity over large geographical areas. In particular, NTNs may deliver Internet and media content to poorly served areas as well as to moving platforms (e.g. cars, trains, aeroplanes) beyond the reach of terrestrial infrastructure.
The following describes some of the different ways in which NTNs can be deployed so as to support service continuity when both UEs and satellites are moving relative to one another. It then goes on to describe handover procedures that can be used with such NTN deployments to minimise service interruption time under these dynamic conditions.

## Single NTN operator
In this deployment model the satellite infrastructure is managed by a single NTN operator. Satellite-to-satellite handovers are considered for two types of scenarios: quasi-earth fixed beam and earth moving beams. In both cases frequent handovers are expected due to motion.

### Satellite-to-satellite handover with Quasi-Earth fixed beam for NGSO
The target mapped cell will be served by a single beam and a frequent handover (time-based) is expected due to the satellite motion. Two different types of handover are considered:
* a) Soft switch handover, where the Mapped Cell is served by two overlapping beams in different carrier frequencies during the switching phase.
* b) Hard switch handover, where the Mapped Cell is served by only one beam at any point in time.

Case a) has the advantage of a negligible service interruption time (in the order of milliseconds) whereas for b) the service interruption time can exceed hundreds of milliseconds in worst case to allow beam layout configuration, radio baseband resource association to beam and UE downlink synchronization. On the other hand, a) requires additional margin resources (feeder link carrier frequency, service link carrier frequency) to support the overlapping beam whereas for b) the same resources are reused between the switching beams (feeder link carrier frequency, service link carrier frequency).
Note that the IP address of the UE is preserved in this scenario.
When using point-to-multipoint communication, all the UEs of the multicast group may start experiencing poor radio conditions during the switching phase, since the source satellite is close to the minimum elevation angle for the UEs. For this reason, an appropriate mode of transmission should be considered during the switching phase to enable reliability and in-sequence delivery of IP packets. As an example, in Figure 17 the UEs served by point-to-multipoint are switched to point-to-point to guarantee reliability and in-sequence data receptions at T1 + ΔT.
This behaviour should be suitable for applications that cannot tolerate packet loss. Some mechanisms should be implemented to avoid congestion during handover. Note that one gNodeB could handle both satellites in the case of a Transparent Payload deployment, while there would be a different gNodeB (involving dedicated signalling) in the case of Regenerative Payload. Depending on the deployment type, this can involve more dedicated signalling (different gNodeB in Regenerative Payload) or common signalling (same gNodeB in Transparent Payload or inter-beam handover within the same satellite). In the case of the same gNodeB in Transparent Payload or inter-beam handover within the same satellite (Regenerative Payload), this deployment reduces the service interruption time and reduces signalling overhead by involving only lower layers (Physical and MAC layer) for uplink synchronization and time alignment.
Quasi-Earth fixed beam deployment model involves some onboard complexity of the satellite to support steerable beamforming techniques, but it reduces the complexity of the network to handle mobility and to allocate resources (beam, frequency plan, etc.). This scenario can be applicable to intra-satellite beam handover, similar to Transparent Payload (two satellites managed by the same gNodeB).

### Satellite-to-satellite handover with Earth-Moving beam for NGSO
A frequent (location-driven) handover is expected due to the satellite motion. The UE in the edge of the beam starts to proceed with the handover. When the UE is located at a distance d from the Beam Reference Centre, where D1 ≤ d ≤ D2, the UE can start performing the handover to the next beam (due to satellite motion). In the best case, the resulting service interruption is in the range of hundreds of milliseconds.
Note that the IP address of the UE is preserved across handover in this scenario.
When using point-to-multipoint communication, only the UE of the multicast group that is at the edge of the beam starts to experience poor radio link conditions, since the source satellite is close to the minimum elevation angle with respect to this UE. An appropriate mode of transmission should be considered during the handover phase to support service continuity.
For example, switching the edge UEs to PTP transmission mode (while the other UE members of the same multicast group remain in PTM mode) should be suitable for applications that are intolerant of packet loss. Note that this implies a new requirement that the gNodeB needs to become aware of each multicast PDU session’s packet loss tolerance in order to make this decision appropriately.
The handover is performed gradually by the UEs that are members of the multicast group. Compared to the quasi-Earth fixed beam deployment model, not all the UEs of the multicast group perform the handover at the same time. However, handovers occur more frequently with Earth moving beam. Depending on the deployment, this can involve more dedicated signalling (different gNodeB in Regenerative Payload) or common signalling (same gNodeB in Transparent Payload or inter-beam handover within the same satellite). In the case of same gNodeB in Transparent Payload or inter-beam handover within the same satellite (Regenerative Payload), this deployment reduces the service interruption time, and it reduces signalling overhead by involving only lower layers (Physical and MAC layer) for uplink synchronization and time alignment.
The Earth moving beam deployment model involves lower onboard complexity of the satellite for beamforming techniques, but it increases the complexity of the end-to-end system to handle mobility and to allocate resources (beam, frequency plan, etc.). This scenario can be applicable for intra-satellite beam handover as explained in the point above, similar to Transparent Payload (two satellites managed by the same gNodeB)

## Common NTN & TN operator
In this deployment model, the same operator owns the TN and NTN infrastructure. The same 5G Core is shared with both TN and NTN Access Network infrastructure. The handover between them does not involve a logical interface.
### TN-NTN or NTN-TN handover for PTM
In terms of service interruption, i.e., the time taken to switch from one access network to another, this is suitable for real-time multicast applications that are sensitive to non-availability of the access network and that need to receive packets reliably (i.e., without any loss) and in the correct order. The network Round-Trip Time (RTT) between a Terrestrial Radio Access base station and a Non-Terrestrial Radio Access base station needs to be assessed. Dual connectivity UEs may also be considered.

## Independent NTN and TN operators
In this deployment model, two different operators own the TN and NTN infrastructure respectively, so the two different systems, each with its own 5G Core, are separate.
### Roaming between different Network Operators for TN and NTN
Two options are envisaged for roaming:
* a) Roaming interface at Core Network level: This assumes an interface between the Core Networks of the two systems. The mobility between both networks would require UE registration and authentication, which may involve additional latency for the mobility procedure. For applications needing to ensure end-to-end delivery of in-sequence data packets without packet loss by maintaining session continuity, a home-routed roaming architecture may be required to maintain IP continuity. This may be required by reliable multicast application protocols where a logical channel is established between the peers before exchanging data, for example FLUTE running on top of ALC/LCT.
* b) RAN sharing agreement between both systems: This assumes both Core Networks have direct interfaces with both TN and NTN radio infrastructure to enable a roaming agreement. A RAN sharing deployment can offer lower latency for mobility between both access networks, since the UE does not need to register and authenticate again and can preserve IP continuity. This is therefore suitable for applications that require in-sequence data delivery for application session continuity. The network RTT between the Terrestrial Radio Access base station and the Non-Terrestrial Radio Access base station needs to be assessed.
