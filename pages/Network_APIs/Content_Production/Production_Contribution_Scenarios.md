---
layout: default
title: Content Production & Contribution
parent: Network APIs
nav_order: 0
has_children: true
---

<img src="../../../assets/images/Banner_API.png" /> 

{: .warning }
This documentation is currently **under development and subject to change**. It reflects outcomes elaborated by 5G-MAG members. If you are interested in becoming a member of the 5G-MAG and actively participating in shaping this work, please contact the [Project Office](https://www.5g-mag.com/contact)

1. TOC
{:toc}

# Scenarios and Use Cases: Content Production and Contribution over Mobile Networks

Wireless connectivity plays a key role in content production and contribution scenarios such as production in studios, coverage of live in-venue (a football match) or on-the-move (the Tour-de-France) events, commentary stands (in a convention), newsgathering (breaking news in the street),...

These different setups may have unique infrastructure and equipment needs, and the provision of connectivity with variyng QoS requirements.

The use of wireless connectivity may differ as a trade-off between quality (or importance) of the content and connection reliability.

## A few key ideas, practical examples and trade-offs

The choice to use wireless connectivity is not limited to specific scenarios or production levels. Instead, it is a strategic trade-off, balancing cost, tolerance for technical glitches, risk of failure, and the quality and importance of the content. Examples are given below.

### Diversity in connectivity needs in the same deployment scenario

Media production scenarios often require a mix of connectivity solutions to meet a variety of needs. For example, during a football match, a production team uses high-quality cameras for the main broadcast, while a commentator stand might have additional wireless cameras for pre-game interviews. Wireless cameras are also deployed outside the stadium to capture interviews with the crowd at the entrance of the stadium.

Similarly, a major event like the coronation of King Charles III brought together numerous TV producers. They used a combination of dedicated, high-quality streams for the main ceremony and various other setups for newsgathering and interviews from journalists deployed around the site. This demonstrates how a single event can have multiple connectivity needs, from high-bandwidth main broadcasts to more flexible, on-the-go reporting. This is independent of the overall cost or budget of the whole event.

<figure>
  <img src="./images/figure_footballmatch.jpeg" width="30%">
  <figcaption>Note: Figure generated with Google Gemini</figcaption>
</figure>

### Immediacy Over Quality

When a sudden street event unfolds, the only way to cover it is with smartphones on a best-effort connection. Getting any live footage is far more valuable than dismissing the connection due to its unreliability. 
While the video might not be broadcast-quality, the immediate, raw footage from the scene is critical for covering the event as it happens.

<figure>
  <img src="./images/figure_mobilejournalism.jpeg" width="30%">
  <figcaption>Note: Figure generated with Google Gemini</figcaption>
</figure>

### Agility over Cost

For both sudden and partially-planned events, cellular bonding systems have emerged as cost-effective solutions to eliminate the need for e.g. dedicated satellite feeds, making live reporting from a wider range of locations economically viable. The equipment itself may be a major investment. The backpacks, modems, and SIM cards are not inexpensive and the news organization has to pay for a data plan for each SIM card and a service fee to the external company that provides the bonding infrastructure.

Cellular bonding is needed as a single best-effort public mobile network cannot guarantee reliability. The news organization will plan where to send the different journalists that will provide reports from remote locations during the news programme. Covering sudden events with cellular bonding equipment is also usual, which may achieve better reliability that the connectivity via a single smartphone.

<figure>
<img src="./images/figure_breakingnews.jpeg" width="30%">
  <figcaption>Note: Figure generated with Google Gemini</figcaption>
</figure>

### Dynamic Footage over Signal Stability

High-mobility cameras introduce the unique challenge of seamlessly mixing their footage (generally highly engaging) into a high-quality production that includes wired cameras with reliable connections. This means the wireless setup needs to be as stable as possible, whereas the nature of its constant motion, changing environments, and potential signal obstructions makes that challenging with frequent signal fades or brief drops in connectivity.

Despite these issues, the value of the unique camera perspective is prioritized. A camera on a referee provides an on-field view of the action and is critical for live replays and enhancing the narrative of the game. A camera on a motorbike in the Tour de France provides up-close views of the riders that a stationary camera could never capture.

<figure>
<img src="./images/figure_tourdefrance.jpeg" width="30%">
  <figcaption>Note: Figure generated with Google Gemini</figcaption>
</figure>

## Beyond best-effort connectivity: exposure of network capabilities

The fundamental trade-off in using wireless connectivity for media is that as a connection becomes more reliable, it enables more high-quality content to be delivered on it.
Historically, media was uplinked using highly reliable satellite and RF technologies. Today, the widespread availability of public mobile networks or LEO satellite constellations triggered a shift toward more agile tools like smartphones, cellular bonding packs or wireless modems. 

The exposure of network capabilities to applications representes an opportunity to exploit advanced network features beyond best-effort connectivity. Examples of network capabilities maz include on-demand quality, user equipment (UE) management, precise time synchronization,... Accessing and utilizing the desired features can be intricate and inconsistent across different networks. Several initiatives are taking shape to explore the opportunities behind Network APIs (exposing network capabilities to API consumers), offering high-level abstractions of underlying network functionalities to simplify resource utilization for non-network experts.
