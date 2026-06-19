# 🖱️ AI Virtual Mouse

Control your computer using **hand gestures** captured through a webcam. This project uses **MediaPipe Hand Tracking** and **OpenCV** to replace traditional mouse interactions with real-time hand gestures.

---

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

---

## 🛠️ Technologies Used

- Python 3.10
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI

---

## 📂 Project Structure

```
AI-Virtual-Mouse/
│
├── main.py                  # Main application
├── hand_tracking.py         # Hand detection & landmark extraction
├── gesture_detector.py      # Gesture recognition logic
├── volume_controller.py     # Volume control (optional)
├── requirements.txt
└── README.md
```

---

## ✋ Supported Gestures

| Gesture | Action |
|----------|--------|
| Index Finger Up | Move Cursor |
| Thumb + Index Pinch | Left Click |
| Index + Middle Finger Pinch | Right Click |
| Two Fingers Up | Scroll |
| Volume Gesture | Control System Volume |

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI-Virtual-Mouse.git
```

Move into the project directory

```bash
cd AI-Virtual-Mouse
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## 📦 Requirements

```
opencv-python
mediapipe==0.10.9
numpy
pyautogui
```

or

```bash
pip install opencv-python mediapipe==0.10.9 numpy pyautogui
```

---

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

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub!
