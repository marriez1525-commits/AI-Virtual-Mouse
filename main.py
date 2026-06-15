import cv2
import numpy as np
import pyautogui

from hand_tracking import HandTracker
from gesture_detector import GestureDetector

# Initialize
cap = cv2.VideoCapture(0)
tracker = HandTracker()
detector = GestureDetector()

screen_w, screen_h = pyautogui.size()

while True:

    success, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame = tracker.findHands(frame)

    lmList = tracker.findPosition(frame)

    fingers = tracker.fingersUp(lmList)

    gesture = detector.detect_gesture(fingers, lmList)

    # ---------------- MOVE CURSOR ----------------
    if gesture == "MOVE" and len(lmList) != 0:

        x1 = lmList[8][1]
        y1 = lmList[8][2]

        # Map camera to screen
        screen_x = np.interp(x1, [0, 640], [0, screen_w])
        screen_y = np.interp(y1, [0, 480], [0, screen_h])

        pyautogui.moveTo(screen_x, screen_y)

    # ---------------- LEFT CLICK ----------------
    elif gesture == "LEFT_CLICK":
        pyautogui.click()

    # ---------------- RIGHT CLICK ----------------
    elif gesture == "RIGHT_CLICK":
        pyautogui.rightClick()

    # ---------------- SCROLL ----------------
    elif gesture == "SCROLL":
        pyautogui.scroll(50)

    # ---------------- VOLUME ----------------
    elif gesture == "VOLUME":
        pass  # will be handled in volume_controller.py

    # ---------------- DISPLAY ----------------
    cv2.imshow("AI Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()