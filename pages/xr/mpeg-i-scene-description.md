---
layout: default
title: MPEG-I Scene Description
parent: XR with MPEG-I SD
has_children: false
nav_order: 0
---

<img src="../../assets/images/Banner_XR.png" /> 

# Overview - MPEG-I Scene Description and glTF 2.0 Extensions
MPEG-I Scene Description (MPEG-I SD) is a standard developed by MPEG for immersive media.
It defines the structure and composition of a 3D scene, referencing and positioning 2D and 3D assets in the scene, and provides information for rendering the scene properly.

The MPEG-I Scene Description standard and glTF (Graphics Library Transmission Format) share a connection in the realm of 3D scenes and models. glTF was chosen as the base scene description technology.
Developed by the Khronos Group, glTF is an open standard that integrates media assets using technologies like OpenGL. In essence, glTF provides a way to describe 3D model geometry, appearance, scene hierarchy, and animation1.

MPEG-I Scene Description (ISO/IEC 23090-14) specifies how to reference and position 2D and 3D assets within a scene, enabling proper rendering and creating rich 3D scenes with real-time media delivery and interactivity.
Khronos has adopted the MPEG-I Scene Description extensions as defined in [https://github.com/KhronosGroup/glTF/blob/main/extensions/README.md](https://github.com/KhronosGroup/glTF/blob/main/extensions/README.md).

## Reference architecture:
MPEG-I SD defined the following reference architecture.

<figure>
  <img src="./images/mpeg-i-sd-0.png" alt="" width="80%">
</figure>

* The Presentation Engine replaces a traditional 2D media player. It is responsible for multi-modal rendering of a scene composed of audiovisuals and haptics media. It also provides information about the viewer's and object pose to optimize delivery.
* The Media Access Function (MAF) is responsible for the media access and processing functions. Media handling is delegated to the MAF by the Presentation Engine. The MAF constructs a suitable media pipeline to transform media from a delivery format into the formats used during rendering. the MAF uses MIME type and codec parameters to identify support for the media reconstruction and assemble the adequate media pipeline.
* The MAF API is used by the Presentation Engine to request immersive media in the scene.
* The Buffers are fed by the processed media with a format defined through the scene description document in SO/IEC 23090-14

## Vendor extensions to Khronos glTF 2.0

<figure>
  <img src="./images/mpeg-i-sd-1.png" alt="" width="80%">
</figure>

A first set of extensions (green in the figure) enable the timed framework including:
* [<span style="color:#00B050; font-weight:bold;">MPEG_media</span>](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/MPEG_media/README.md), which enables the referencing of external media streams that are delivered over protocols such as RTP/SRTP, MPEG-DASH, or others
* [<span style="color:#00B050; font-weight:bold;">MPEG_accessor_timer</span>](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/MPEG_accessor_timed/README.md), used in a scene that contains timed media and/or metadata to describe access to the dynamically changing data
* [<span style="color:#00B050; font-weight:bold;">MPEG_buffer_circular</span>](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/MPEG_buffer_circular/README.md), to extend the buffer into a circular buffer

A second group of extensions (blue in the figure) enables the inclusion of dynamic and temporal media including:
* [<span style="color:#0070C0; font-weight:bold;">MPEG_texture_video</span>](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/MPEG_texture_video/README.md). provides the possibility to link a texture object defined in glTF 2.0 to media and its respective track
* [<span style="color:#0070C0; font-weight:bold;">MPEG_audio_spatial</span>](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/MPEG_audio_spatial/README.md), to support spatial audio
* [<span style="color:#0070C0; font-weight:bold;">MPEG_mesh_linking</span>](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/MPEG_mesh_linking/README.md), provides the possibility to link a mesh to another mesh in a glTF asset
* [<span style="color:#0070C0; font-weight:bold;">MPEG_scene_dynamic</span>](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/MPEG_scene_dynamic/README.md), [<span style="color:#0070C0; font-weight:bold;">MPEG_viewport_recommended</span>](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/MPEG_viewport_recommended/README.md), and [<span style="color:#0070C0; font-weight:bold;">MPEG_animation_timing</span>](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/MPEG_animation_timing/README.md), which indicate that a particular form of timed data is provided to the Presentation Engine during the consumption of the scene and that it shall adapt to the changing information.

A third group of extensions enables the distribution of real-time immersive and interactive media content including:
* Augmented Reality anchor (<span style="color:#7030A0; font-weight:bold;">MPEG_anchor</span>), to support AR experiences where virtual content is inserted into the user's real environment
* Interactivity (<span style="color:#7030A0; font-weight:bold;">MPEG_scene_interactivity</span>, <span style="color:#7030A0; font-weight:bold;">MPEG_node_interactivity</span>), to describe interactivity at runtime with support for interactions between user and virtual objects and between virtual objects, with triggers based on proximity, visibility, collision or user input.
* Avatar (<span style="color:#7030A0; font-weight:bold;">MPEG_avatar</span>), to support the representation of 3D avatars.
* Lighting (<span style="color:#7030A0; font-weight:bold;">MPEG_lights_texture_based</span>, <span style="color:#7030A0; font-weight:bold;">MPEG_light_punctual</span>), to provide a realistic user experience including shadows and lighting.
* Haptics (<span style="color:#7030A0; font-weight:bold;">MPEG_haptic</span>), to support haptics based on the MPEG standard for Coded representation of Haptics by attaching haptic information to a node or to a mesh.
