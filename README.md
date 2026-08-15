<div align="center">

# AI VIRTUAL MOUSE PLATFORM
### *Enterprise Spatial Computing & Computer Vision Interface*

**A unified, software-driven human-machine interaction framework engineered to translate spatial hand kinematics into low-latency system controls via computer vision and 3D landmark regression.**

---

</div>

## Executive Summary

The **AI Virtual Mouse Platform** offers an enterprise-grade alternative to physical input peripherals by establishing a contact-free, camera-based input framework. Operating over standard RGB video streams, the system continuously monitors 21 anatomical hand joints in real time. By evaluating spatial landmark dynamics and vector geometries, it simulates operating system hardware controls—including fluid cursor locomotion, sub-pixel jitter suppression, multi-type clicks, vertical page scrolling, and system audio scaling—without dedicated hardware peripherals.

Architected for contactless public kiosks, sterile surgical displays, accessibility engineering, and modern smart workstations, this software provides a hygienic, responsive, and cross-platform human-computer interface (HCI).

---

## Core Technological Architecture

* **Real-Time Vision Engine:** Ingests live video feeds, flips spatial canvases horizontally for intuitive mirror feedback, normalizes ambient light variations, and maps spatial coordinates to active screen dimensions.
* **3D Hand Skeletal Regression:** Utilizes deep learning regression frameworks to detect, segment, and track 21 three-dimensional skeletal joint coordinates per frame.
* **Kinematic Geometry & Vector Analysis:** Evaluates spatial relationships, multi-finger Euclidean joint distances, and relative angular movements to classify physical gestures accurately.
* **System Input Automation:** Interfaces directly with host operating system input buses to execute pointer locomotion and hardware event interrupts with minimal overhead.

---

## Technical Highlights & System Capabilities

* **Sub-Pixel Motion Smoothing:** Applies exponential moving average (EMA) filtration over successive frame coordinates to eliminate hand micro-tremors and optical noise, yielding smooth cursor trajectories.
* **Non-Linear Workspace Mapping:** Establishes an internal virtual interaction boundary within the camera field of view, enabling full-screen coverage without requiring expansive physical arm movements.
* **Hysteresis State Locking:** Integrates temporal frame buffers to validate gesture state changes, preventing false inputs caused by transient hand transitions.
* **Adaptive Illumination Normalization:** Incorporates contrast equalization preprocessing to maintain tracking stability across low-light, ambient, or backlit environments.

---

## Gesture Control Specifications

* **Cursor Locomotion:** Extending the index finger drives primary pointer movement across the display space.
* **Left Click & Drag:** Pinching the thumb and index finger executes a primary selection or sustains element dragging.
* **Double Click:** Executing two consecutive pinch sequences within a designated time window triggers double-click events to launch files or applications.
* **Right Click:** Bringing the index and middle fingers into close proximity activates context menus.
* **Vertical Page Scroll:** Extending both the index and middle fingers vertically translates document and browser views up or down.
* **Master Volume Control:** Adjusting the Euclidean distance between the thumb and pinky finger scales system audio linearly from minimum to maximum capacity.
* **Neutral Idle State:** Resting the hand in a closed fist or flat palm freezes cursor movement to prevent unintended interactions.

---

## Processing Pipeline

1. **Video Ingestion:** Captures raw RGB video frames at native rates using standard integrated or external webcams.
2. **Skeletal Joint Tracking:** Extracts three-dimensional joint coordinates across the hand structure.
3. **Spatial Geometry Analysis:** Measures vector lengths, angles, and inter-digit distances against defined gesture thresholds.
4. **Coordinate Transformation:** Interpolates camera frame coordinates to exact display monitor resolutions.
5. **System Command Dispatch:** Transmits gesture commands to operating system input drivers to simulate physical hardware mouse events.

---

## Future Platform Roadmap

* **Multimodal Natural Language Integration:** Combining spatial gesture navigation with vocal commands for multi-step system shortcuts.
* **Multi-Touch & Dual-Hand Workspaces:** Supporting dual-hand spatial gestures for 3D object rotation, viewport manipulation, and workspace switching.
* **Custom Gesture Calibration Framework:** Enabling users to record personalized hand configurations and map them to custom application triggers.
* **Gaze-Guided Target Selection:** Integrating eye-gaze direction for rapid target localization combined with hand gestures for precise selection.

---

## License & Distribution

Distributed under the **MIT License**. Free for personal, academic, commercial, and enterprise deployment.