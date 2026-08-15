<div align="center">

# 🖱️ AI VIRTUAL MOUSE PLATFORM
### *Next-Generation Touchless Spatial Computing Interface*

**A high-performance, contact-free human-computer interaction framework that translates spatial hand movements into precise real-time system controls using advanced computer vision and 3D landmark tracking.**

---

</div>

## 📌 Executive Summary

The **AI Virtual Mouse Platform** redefines human-computer interaction by replacing physical input devices with an intuitive, camera-driven gesture control framework. Operating over standard RGB video streams, the system tracks 21 distinct anatomical joints per hand in real time. By analyzing spatial landmark geometry and joint vectors, it simulates full hardware mouse functionality—including fluid cursor locomotion, sub-pixel jitter filtration, single/double clicking, right clicking, scrolling, and system media manipulation—without any physical contact.

Designed for touchless public kiosk navigation, sterile medical and surgical environments, accessibility engineering, and modern smart workspaces, this project delivers a secure, hygienic, and highly responsive human-machine interface.

---

## 🛠️ Technology Ecosystem & Core Mechanics

* **Real-Time Vision & Image Processing:** Ingests live webcam video feeds, performs automated frame flipping for intuitive mirror response, normalizes light exposure variations, and translates spatial coordinates onto screen coordinates.
* **3D Hand Skeletal Regression:** Leverages deep learning models to dynamically locate, segment, and continuously track 21 three-dimensional skeletal joint coordinates across every frame.
* **Kinematic Vector Mathematics:** Measures spatial relationships, multi-finger Euclidean joint distances, and relative angular movements to detect distinct physical gestures accurately.
* **Low-Level Operating System Integration:** Bridges gesture recognitions directly to host system drivers, enabling smooth pointer manipulation and immediate execution of operating system actions.

---

## ⚡ Key Technical Capabilities & Innovations

* **Sub-Pixel Motion Smoothing:** Incorporates mathematical filtering models to smooth out natural hand micro-tremors, preventing cursor shaking and producing steady pointer locomotion.
* **Non-Linear Workspace Boundary Mapping:** Defines an internal virtual boundary within the webcam's field of view, enabling users to comfortably reach all screen edges without extreme arm extensions.
* **Hysteresis & False-Trigger Prevention:** Employs temporal frame validation to ensure state changes (like clicking or scrolling) require brief, deliberate positional stability, eliminating unintended input actions.
* **Adaptive Light Normalization:** Automatically adjusts canvas contrast and color balances to ensure consistent tracking accuracy across low-light, ambient, or back-lit environments.

---

## ✋ Supported Spatial Gestures & Operations

* **Cursor Locomotion:** Extending the index finger tracks positional movement across the display with low latency.
* **Left Click & Object Dragging:** Pinching the index finger and thumb triggers a primary click or holds an element for continuous dragging.
* **Double Click:** Executing two consecutive pinch triggers in quick succession launches files, applications, or selects full text blocks.
* **Right Click Context Menu:** Bringing the index finger and middle finger together opens context-sensitive system menus.
* **Vertical Page Scrolling:** Extending both index and middle fingers vertically translates documents and web pages smoothly up or down.
* **Dynamic Master Volume Control:** Adjusting the spatial distance between the thumb and pinky finger scales system audio linearly from zero to maximum capacity.
* **Neutral Idle State:** Resting the hand in a closed fist or flat palm freezes cursor movement to prevent accidental interactions.

---

## ⚙️ Processing Pipeline

1. **Video Feed Acquisition:** Captures live RGB frame matrices at high rates directly from standard integrated or external USB webcams.
2. **Skeletal Joint Detection:** Extracts relative three-dimensional joint locations across the user's hand structure.
3. **Spatial Geometry Analysis:** Evaluates vector lengths, angles, and inter-finger distances against calibrated gesture profiles.
4. **Coordinate Transformation:** Translates camera frame coordinates into exact display screen pixels based on host monitor resolutions.
5. **System Command Execution:** Transmits immediate gesture commands directly to system input drivers to simulate physical hardware mouse events.

---

## 📈 Platform Future Expansion

* **Multimodal Voice Control Integration:** Combining spatial gesture navigation with vocal commands for complex system shortcuts.
* **Multi-Touch & Dual-Hand Workspaces:** Supporting dual-hand gestures for 3D object rotation, spatial viewport manipulation, and workspace switching.
* **On-the-Fly Custom Gesture Calibration:** Allowing users to record personal custom hand shapes and assign them to custom application shortcuts.
* **Gaze-Guided Target Selection:** Pairing eye-tracking for fast coarse target selection with spatial hand gestures for precise clicking action.

---

## 📄 License & Distribution

Distributed under the **MIT License**. Free for public, personal, commercial, and educational applications.