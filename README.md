<div align="center">

# 🖱️ AI VIRTUAL MOUSE PLATFORM
### *Enterprise Touchless Spatial Computing & Human-Computer Interface*

**A unified, software-driven human-machine interaction framework designed to translate spatial hand dynamics into high-precision, low-latency system controls using computer vision and 3D landmark regression.**

---

</div>

## 📌 Executive Summary

The **AI Virtual Mouse Platform** provides a modern alternative to traditional physical input hardware by establishing a contact-free, camera-based input engine. Operating over standard RGB video streams, the system continuously monitors 21 anatomical hand joints in real time. By analyzing spatial landmark kinematics and vector geometries, it simulates operating system hardware controls—including continuous cursor movement, sub-pixel jitter suppression, multi-type clicks, vertical page scrolling, and system audio scaling—without specialized hardware.

Engineered for touchless public interactive kiosks, sterile surgical environments, accessibility systems, and modern contactless workstations, this software delivers a hygienic, responsive, and cross-platform human-computer interface (HCI).

---

## 🛠️ Technological Architecture & Core Engine

* **Real-Time Computer Vision:** Ingests live video feeds, flips spatial canvases horizontally for intuitive mirror feedback, normalizes lighting variations, and maps spatial coordinates to screen dimensions.
* **3D Hand Skeletal Regression:** Utilizes machine learning frameworks to detect, segment, and track 21 three-dimensional skeletal joint coordinates per frame.
* **Kinematic Geometry & Vector Mathematics:** Evaluates spatial relationships, multi-finger Euclidean joint distances, and relative angular movements to classify physical gestures.
* **System Input Automation:** Interfaces directly with host operating system input buses to execute pointer locomotion and hardware event interrupts.

---

## ⚡ Technical Highlights & System Capabilities

* **Sub-Pixel Motion Smoothing:** Employs exponential moving average (EMA) filtration algorithms over successive frame coordinates to eliminate hand micro-tremors and optical noise, delivering fluid cursor trajectories.
* **Non-Linear Workspace Boundary Mapping:** Establishes an internal virtual interaction boundary within the camera field of view, allowing full screen coverage without requiring wide physical arm movements.
* **Hysteresis State Locking:** Integrates temporal frame buffers to validate gesture state changes, preventing false inputs caused by transient hand transitions.
* **Adaptive Illumination Normalization:** Incorporates contrast equalization preprocessing to maintain tracking stability across low-light, ambient, or backlit environments.

---

## ✋ Gesture Control Specifications

* **Cursor Locomotion:** Extending the index finger controls pointer movement across the active display space.
* **Left Click & Drag:** Pinching the thumb and index finger executes a primary select action or sustains element dragging.
* **Double Click:** Executing two consecutive pinch sequences within a designated time window triggers double-click events to launch files or applications.
* **Right Click:** Bringing the index and middle fingers into close proximity opens context menus.
* **Vertical Page Scroll:** Extending both the index and middle fingers vertically translates document and browser views up or down.
* **Master Volume Control:** Adjusting the Euclidean distance between the thumb and pinky finger scales system audio linearly from zero to maximum capacity.
* **Neutral Idle State:** Resting the hand in a closed fist or flat palm freezes cursor movement to prevent unintended interactions.

---

## ⚙️ Data Processing Pipeline

1. **Video Feed Acquisition:** Captures raw RGB video frames at native rates using standard integrated or external webcams.
2. **Skeletal Joint Tracking:** Extracts three-dimensional joint coordinates across the hand structure.
3. **Spatial Geometry Analysis:** Measures vector lengths, angles, and inter-digit distances against defined gesture thresholds.
4. **Coordinate Transformation:** Interpolates camera frame coordinates to exact display monitor resolutions.
5. **System Command Dispatch:** Transmits gesture commands to operating system input drivers to simulate physical hardware mouse events.

---

## 📈 Future Platform Roadmap

* **Multimodal Natural Language Engine:** Combining spatial gesture navigation with vocal commands for multi-step system shortcuts.
* **Multi-Touch & Dual-Hand Workspaces:** Supporting dual-hand spatial gestures for 3D object rotation, viewport manipulation, and workspace switching.
* **Custom Gesture Calibration Framework:** Allowing users to record personalized hand configurations and map them to custom application triggers.
* **Gaze-Guided Target Selection:** Integrating eye-gaze direction for rapid target location combined with hand gestures for precise selection.

---

## 📄 License & Distribution

Distributed under the **MIT License**. Free for personal, academic, commercial, and enterprise deployment.
