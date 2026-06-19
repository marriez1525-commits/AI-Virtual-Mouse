# 🖱️ AI Virtual Mouse

Control your computer using **hand gestures** captured through a webcam. This project uses **MediaPipe Hand Tracking** and **OpenCV** to replace traditional mouse interactions with real-time hand gestures.

## 🚀 Features

- 🖐️ Real-time hand tracking
- 🖱️ Move mouse cursor using index finger
- 👆 Left click gesture
- 👉 Right click gesture
- 🔄 Scroll using hand gesture
- 🔊 Volume control support (extendable)
- ⚡ Smooth and real-time performance
- 📷 Webcam-based interaction
- 🎯 Accurate finger landmark detection

## 🛠️ Technologies Used

- Python 3.10
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI

## ✋ Supported Gestures

| Gesture | Action |
|----------|--------|
| Index Finger Up | Move Cursor |
| Thumb + Index Pinch | Left Click |
| Index + Middle Finger Pinch | Right Click |
| Two Fingers Up | Scroll |
| Volume Gesture | Control System Volume |



## 💡 How It Works

1. Webcam captures live video.
2. MediaPipe detects hand landmarks.
3. Finger positions are extracted.
4. Gestures are recognized.
5. Corresponding mouse actions are executed using PyAutoGUI.

---
## 📈 Future Improvements

- 🎙️ Voice commands
- 🤚 Multi-hand support
- 🎚️ Brightness control
- 📂 Drag and Drop gesture
- 📸 Screenshot gesture
- 🔒 Custom gesture mapping
- 🎮 Gaming mode
- 🧠 AI-based gesture customization



