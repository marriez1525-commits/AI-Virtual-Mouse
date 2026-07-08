# 🖱️ AI Virtual Mouse: Next-Gen Touchless Interface

Control your desktop interface seamlessly using real-time **hand gestures** captured through a standard webcam. By leveraging advanced **Machine Learning** pipelines and **Computer Vision** frameworks, this project completely maps human hand anatomy to digital mouse mechanics, offering a fluid, hardware-free navigation experience.

---

## 🚀 Key Features

* **⚡ Ultra-Low Latency Tracking:** Employs optimized processing pipelines to achieve real-time landmark detection and instantaneous screen updates.
* **🖱️ Jitter-Free Precision Cursor:** Implements an exponential moving average (EMA) smoothing algorithm to filter out natural hand tremors for smooth cursor drift.
* **👆 Comprehensive Gesture Engine:** Maps distinct anatomical finger triggers to standard mouse operations including left-click, right-click, double-click, and persistent dragging.
* **🔄 Smart Proportional Scrolling:** Allows dynamic page scrolling where the velocity of the scroll scales seamlessly with physical hand vertical movement.
* **🔊 Audio & System Control Scaling:** Modulates system master volume continuously by measuring Euclidean distance vectors between key finger landmarks.
* **🎯 Aspect-Ratio & Screen Mapping:** Features automatic coordinate translation from bounded webcam frame dimensions to match any native monitor screen resolution.

---

## ✋ Supported Gestures & Action Mapping

| Gesture Interaction | Visual Trigger Configuration | Triggered System Action |
| :--- | :--- | :--- |
| **Index Finger Extended** ☝️ | Index MCP-PIP-DIP aligned upward; all other fingers closed | **Precision Cursor Movement** 🧭 |
| **Thumb + Index Pinch** 🤏 | Spatial distance between Index Tip and Thumb Tip falls below threshold | **Left Mouse Click** 🖱️ |
| **Index + Middle Pinch** ✌️ | Spatial distance between Index Tip and Middle Tip falls below threshold | **Right Mouse Click** 🔘 |
| **Index + Middle Parallel Up** 🖐️ | Both Index and Middle fingers fully extended upward simultaneously | **Dynamic Page Scroll Mode** 🔄 |
| **Thumb + Pinky Separation** 🤙 | Variable scaling distance between Thumb Tip and Pinky Tip | **System Volume Modulation** 🔊 |

---

## 🛠️ Deep Tech Stack & System Architecture

The application decouples video acquisition, high-dimensional machine learning inference, and low-level system automation to maximize frame rates and responsiveness.

* **Language Platform:** Python 3.10+
* **Computer Vision Framework:** `OpenCV` (Video stream thread management, matrix frame conversions, and runtime rendering)
* **Anatomical Tracking Engine:** `MediaPipe Hands` (Single-shot pipeline tracking 21 explicit 3D hand coordinates with localized skeletal topology)
* **OS-Level Automation API:** `PyAutoGUI` (Native OS driver injection for virtualizing hardware mouse and keyboard interrupt requests)
* **Mathematical Operations Optimization:** `NumPy` (Vectorized multidimensional array operations for geometric distance calculations and coordinate mapping)

### 📊 End-to-End System Processing Pipeline