<div align="center">

# 🖱️ AI VIRTUAL MOUSE PLATFORM
### *Next-Generation Spatial Computing & Computer Vision Interface*

**Transform your standard web camera into an ultra-low-latency, contact-free human-computer interface using continuous 3D hand skeletal tracking, spatial coordinate kinematics, and geometric gesture recognition.**

---

</div>

## 📌 Executive Overview

The **AI Virtual Mouse Platform** bridges physical human interaction and digital execution through high-precision spatial computer vision. Built upon **Google MediaPipe** and **OpenCV**, this enterprise-grade framework tracks 21 distinct 3D anatomical joints per hand in real time to simulate hardware mouse mechanics—including dynamic cursor locomotion, sub-pixel jitter filtration, single/double clicking, scrolling, and system media control—without physical peripherals.

Designed for touchless public kiosk control, sterile surgical displays, accessibility engineering, and immersive media navigation, the architecture delivers a flexible, software-driven human-machine interface (HMI).

---

## 🛠️ Technology Stack & Core Architecture

| Domain | Layer / Framework | Primary Function |
| :--- | :--- | :--- |
| **Runtime Environment** | Python 3.10+ | Asynchronous loop management & low-level OS bindings |
| **Vision Framework** | OpenCV (v4.x) | High-speed frame capture, BGR-to-RGB conversion, canvas drawing |
| **ML Landmark Engine** | MediaPipe Hands | 21-point 3D hand skeleton regression & joint coordinate extraction |
| **System Interface** | PyAutoGUI / pynput | Cross-platform event injection & hardware interrupt simulation |
| **Kinematics & Vector Math** | NumPy | Multi-dimensional array processing, distance scalar metrics, moving averages |

---

## ⚡ Technical Highlights & Algorithmic Engineering

* **Sub-Pixel Kinematic Smoothing:** Utilizes an Exponential Moving Average (EMA) algorithm over frame coordinates to eliminate hand micro-tremors and optical noise:
  
  $$\vec{P}_{\text{smooth}}(t) = \alpha \cdot \vec{P}_{\text{raw}}(t) + (1 - \alpha) \cdot \vec{P}_{\text{smooth}}(t-1)$$

* **Non-Linear ROI Bounds Mapping:** Maps an internal, dynamic camera boundary to 100% of the host monitor display resolution, preventing extreme arm reach during screen edge navigation.
* **Hysteresis State Locking:** Employs temporal frame validation buffers to ensure gesture state changes require consistent positional stability, eliminating false triggers caused by transient hand movements.
* **Illumination Normalization:** Integrates OpenCV histogram equalization to preserve landmark detection accuracy across varied lighting environments.

---

## ✋ Precision Gesture Control Matrix