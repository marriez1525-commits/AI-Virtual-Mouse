# AI Virtual Mouse: Next-Generation Touchless Human-Computer Interaction Platform

> A high-performance, real-time computer vision framework designed to translate free-hand spatial gestures into system-level OS actions using advanced landmark tracking and frame-by-frame spatial telemetry.

---

## 📌 Executive Summary

The **AI Virtual Mouse Platform** provides a modern alternative to traditional hardware input peripherals by leveraging real-time computer vision, frame-based landmark spatial analysis, and operating system automation. Operating over standard RGB video streams captured via low-cost webcams, the system continuously tracks hand skeletal structures, classifies geometric configurations, and converts positional dynamics into zero-latency cursor locomotion, click triggers, scroll states, and media manipulation.

Designed for accessibility, hygienic public-terminal interfaces, and hands-free computing environments, this software leverages **Google MediaPipe** for robust 21-point hand skeleton reconstruction and **OpenCV** for low-latency matrix manipulation and video capture pipelines.

---

## 🛠️ Core Technology Stack & Dependencies

The system architecture relies on an optimized stack designed to maximize frame rates and minimize computational overhead on standard consumer hardware:

* **Core Runtime:** Python 3.10+ (Selected for asynchronous I/O support and optimized C-binding bridges)
* **Computer Vision Pipeline:** OpenCV (Open Source Computer Vision Library) v4.x — Handles frame ingestion, matrix transformations, color-space conversions (BGR to RGB), and real-time canvas rendering.
* **Landmark Reconstruction Engine:** Google MediaPipe Hands ML Framework — Utilizes a two-stage pipeline consisting of a palm detection model and a 3D hand skeleton regression model to track 21 key points per hand.
* **OS-Level Automation:** PyAutoGUI & pynput — Intercepts application output to drive system input buses, simulating raw hardware driver interrupts across cross-platform OS environments.
* **Linear Algebra & Spatial Computing:** NumPy — Accelerates vector math, Euclidean distance evaluations, and multi-dimensional array operations.

---

## 🚀 Key Architectural Capabilities

### 1. Exponential Moving Average (EMA) Jitter Reduction
Raw webcam inputs inherently suffer from sensor noise, ambient light flicker, and micro-hand tremors. The platform integrates an adjustable exponential moving average smoothing filter over successive frame coordinate outputs to yield steady, continuous cursor trajectories without artificial input delay:

$$\vec{P}_{smooth}(t) = \alpha \cdot \vec{P}_{raw}(t) + (1 - \alpha) \cdot \vec{P}_{smooth}(t-1)$$

### 2. Adaptive Region of Interest (ROI) & Boundary Mapping
To avoid requiring the user to physically sweep across the entire camera field of view, the software establishes an inner virtual interaction box. Coordinates within this sub-region are dynamically scaled using non-linear interpolation matrix equations to cover 100% of the active display resolution.

### 3. Hysteresis & False-Positive Suppression
Gesture classification uses temporal frame buffers and threshold hysteresis. A state transition (e.g., from *Move State* to *Left Click Trigger*) requires consistent geometric landmark bounds over a configurable window of consecutive frames, preventing accidental inputs caused by intermediate transition movements.

### 4. Dynamic Lighting Adaptation
Through automated histogram equalization and adaptive frame thresholding using OpenCV pre-processing layers, the system maintains consistent landmark localization precision under low-light or uneven back-lit conditions.

---

## ✋ Comprehensive Gesture Control Matrix

The interaction module continuously tracks relative vector distances, spatial angles, and visibility confidence factors across key anatomical hand points:

| Gesture Profile | Structural Landmark Trigger | Spatial Condition | Operating System Output |
| :--- | :--- | :--- | :--- |
| **Cursor Locomotion** | Landmark 8 (Index Tip) Extended | Index finger raised; all other digits retracted beyond baseline threshold | Continuous Screen Pointer Coordinates |
| **Left Click** | Distance between Landmark 4 (Thumb Tip) & 8 (Index Tip) | Relative spatial Euclidean distance $< \Delta_{click}$ | Primary Single Click / Drag Selection |
| **Double Click** | Consecutive Left Click Gestures | Dual spatial pinch triggers within a 300ms window | Primary Double Click (File / App Launch) |
| **Right Click** | Distance between Landmark 8 (Index Tip) & 12 (Middle Tip) | Relative spatial Euclidean distance $< \Delta_{click}$ | Context Menu Trigger |
| **Vertical Scroll** | Extended Index (8) & Middle (12) Fingers | Parallel vertical translation of dual vectors | System Vertical Mouse Wheel Translation |
| **Media Volume Control** | Distance between Landmark 4 (Thumb) & 20 (Pinky) | Dynamic vector length mapped along a continuous linear range | Master System Volume Interpolation ($0\% - 100\%$) |
| **Idle / Neutral State** | Closed Fist / Flat Palm Resting | No active vector triggers identified within boundary | Input Hold / Zero Cursor Locomotion |

---

## ⚙️ Software Pipeline & Data Flow Architecture

The data processing pipeline processes incoming frame matrices sequentially through isolated processing nodes: