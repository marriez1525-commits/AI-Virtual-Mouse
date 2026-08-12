# 🖱️ AI Virtual Mouse

> Real-time touchless computer control using computer vision and hand-gesture recognition.

---

## 📌 Executive Summary

**AI Virtual Mouse** is a computer vision application that translates human hand gestures captured via a standard webcam into real-time system interactions. Built using **MediaPipe**, **OpenCV**, and **PyAutoGUI**, it eliminates the need for physical hardware peripherals by offering precise cursor motion, multi-type clicks, scrolling, and system audio control.

---

## 🛠️ Tech Stack & Dependencies

* **Core Language:** Python 3.10+
* **Computer Vision:** OpenCV (Open Source Computer Vision Library)
* **Landmark Detection:** Google MediaPipe Hands framework
* **System Automation:** PyAutoGUI
* **Numerical Processing:** NumPy

---

## 🚀 Key Features

* **Sub-Pixel Cursor Smoothing:** Exponential moving averages reduce hand jitter for fluid pointer movement.
* **Low Latency Processing:** Optimized frame pipelines ensure real-time gesture recognition.
* **Dynamic Coordinate Mapping:** Maps webcam frame dimensions directly to screen resolution.
* **Multi-Gesture Action Suite:** Native support for cursor navigation, single/double clicking, right clicking, scrolling, and volume manipulation.
* **Configurable Sensitivity:** Dynamic detection thresholds adapt to different lighting conditions and background variations.

---

## ✋ Gesture Control Matrix

| Gesture Configuration | Trigger Condition | System Action |
| :--- | :--- | :--- |
| **Index Finger Extended** | Landmark 8 position mapped to screen | Move Cursor |
| **Index + Thumb Pinch** | Distance between Landmark 4 & 8 < threshold | Left Click |
| **Index + Middle Pinch** | Distance between Landmark 8 & 12 < threshold | Right Click |
| **Index + Middle Extended** | Vertically aligned dual landmarks | Scroll Up / Down |
| **Thumb & Pinky Distance** | Scaled spatial Euclidean distance | Volume Control |

---

## ⚙️ Architecture & Pipeline Flow