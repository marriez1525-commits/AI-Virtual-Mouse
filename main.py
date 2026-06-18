import cv2
import numpy as np
import pyautogui
from hand_tracking import HandTracker
from gesture_detector import GestureDetector

# Stop PyAutoGUI from crashing if mouse hits screen boundaries
pyautogui.FAILSAFE = False

# Initialize Camera and Objects
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

tracker = HandTracker()
detector = GestureDetector()
screen_w, screen_h = pyautogui.size()

# --- TUNING VARIABLES ---
smooth_factor = 3      
speed_multiplier = 1.5  
scroll_speed = 40       # 💡 Change this number to make scrolling faster or slower

# Bounding Box Margins
frame_margin_x = 110  
margin_top = 60       
margin_bottom = 120   

# Calculate the center line of the box for the joystick logic
box_center_y = margin_top + (480 - margin_bottom - margin_top) // 2

# Tracking Variables
plocX, plocY = 0, 0
clocX, clocY = 0, 0

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    frame = tracker.findHands(frame)
    lmList = tracker.findPosition(frame, draw=False)
    fingers = tracker.fingersUp(lmList)
    gesture = detector.detect_gesture(fingers, lmList)

    # DRAW THE CONTROL ZONE BOX
    cv2.rectangle(frame, (frame_margin_x, margin_top), 
                  (640 - frame_margin_x, 480 - margin_bottom), (0, 255, 0), 2)
    
    # DRAW A FAINT CENTER LINE (The Joystick Neutral Zone)
    cv2.line(frame, (frame_margin_x, box_center_y), (640 - frame_margin_x, box_center_y), (100, 100, 100), 1)

    # ---------------- 1. MOVE CURSOR ----------------
    if gesture == "MOVE" and len(lmList) != 0:
        x1, y1 = lmList[8][1], lmList[8][2]
        screen_x = np.interp(x1, [frame_margin_x, 640 - frame_margin_x], [0, screen_w])
        screen_y = np.interp(y1, [margin_top, 480 - margin_bottom], [0, screen_h])

        screen_x = screen_w / 2 + (screen_x - screen_w / 2) * speed_multiplier
        screen_y = screen_h / 2 + (screen_y - screen_h / 2) * speed_multiplier

        clocX = plocX + (screen_x - plocX) / smooth_factor
        clocY = plocY + (screen_y - plocY) / smooth_factor

        pyautogui.moveTo(np.clip(clocX, 0, screen_w), np.clip(clocY, 0, screen_h))
        plocX, plocY = clocX, clocY

    # ---------------- 2. LEFT / RIGHT CLICK ----------------
    elif gesture in ["LEFT_CLICK", "RIGHT_CLICK"]:
        if gesture == "LEFT_CLICK":
            pyautogui.click()
            cv2.putText(frame, "Left Click", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            pyautogui.rightClick()
            cv2.putText(frame, "Right Click", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # ---------------- 3. EASY JOYSTICK SCROLL ----------------
    elif gesture == "SCROLL" and len(lmList) != 0:
        y_current = lmList[8][2]
        
        # Dead zone around the center line to prevent micro-twitching
        dead_zone = 20 

        # If hand is in the TOP half of the box -> Scroll UP
        if y_current < (box_center_y - dead_zone):
            pyautogui.scroll(scroll_speed)
            cv2.putText(frame, "🔴 JOYSTICK: SCROLLING UP", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            
        # If hand is in the BOTTOM half of the box -> Scroll DOWN
        elif y_current > (box_center_y + dead_zone):
            pyautogui.scroll(-scroll_speed)
            cv2.putText(frame, "🔵 JOYSTICK: SCROLLING DOWN", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
            
        # Hand is resting in the middle dead-zone
        else:
            cv2.putText(frame, "⚪ JOYSTICK: NEUTRAL (STOPPED)", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # ---------------- 4. ZOOM IN / OUT ----------------
    elif len(fingers) >= 5 and fingers[1:] == [1, 1, 1, 1] and len(lmList) != 0:
        current_dist = ((lmList[20][1] - lmList[4][1])**2 + (lmList[20][2] - lmList[4][2])**2)**0.5
        global zoom_start_dist
        if 'zoom_start_dist' not in globals() or zoom_start_dist is None:
            zoom_start_dist = current_dist
            
        zoom_ratio = current_dist / zoom_start_dist
        
        if zoom_ratio > 1.15:  
            pyautogui.hotkey('ctrl', '-')
            zoom_start_dist = current_dist
            cv2.putText(frame, "ZOOM OUT", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)
        elif zoom_ratio < 0.85: 
            pyautogui.hotkey('ctrl', '+')
            zoom_start_dist = current_dist
            cv2.putText(frame, "ZOOM IN", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        else:
            cv2.putText(frame, "Zoom Mode Ready", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("AI Virtual Mouse Feed", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()