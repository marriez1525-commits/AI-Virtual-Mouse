import cv2
import numpy as np
import pyautogui
from hand_tracking import HandTracker
from gesture_detector import GestureDetector

# Stop PyAutoGUI from crashing if mouse hits screen boundaries
pyautogui.FAILSAFE = False

# Initialize Camera and Objects
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

tracker = HandTracker()
detector = GestureDetector()
screen_w, screen_h = pyautogui.size()

# --- TUNING VARIABLES (Adjust these to your preference!) ---
smooth_factor = 3      # Lower = faster/snappier, Higher = smoother/slower (Try 2 or 3)
speed_multiplier = 1.5  # Increase this to make the cursor move even faster!

# Bounding Box Margins (Shifted up to let you reach the bottom taskbar easily)
frame_margin_x = 110  
margin_top = 60       
margin_bottom = 120   

# Tracking Variables for Modes
plocX, plocY = 0, 0
clocX, clocY = 0, 0
scroll_start_y = None
zoom_start_dist = None

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    frame = tracker.findHands(frame)
    lmList = tracker.findPosition(frame, draw=False)
    fingers = tracker.fingersUp(lmList)
    gesture = detector.detect_gesture(fingers, lmList)

    # DRAW THE PERFECTLY PROPORTIONED CONTROL ZONE BOX
    cv2.rectangle(frame, (frame_margin_x, margin_top), 
                  (640 - frame_margin_x, 480 - margin_bottom), (0, 255, 0), 2)

    # ---------------- 1. MOVE CURSOR (With Speed Multiplier) ----------------
    if gesture == "MOVE" and len(lmList) != 0:
        x1, y1 = lmList[8][1], lmList[8][2]

        # Map camera box to screen coordinates
        screen_x = np.interp(x1, [frame_margin_x, 640 - frame_margin_x], [0, screen_w])
        screen_y = np.interp(y1, [margin_top, 480 - margin_bottom], [0, screen_h])

        # Apply Speed Multiplier from the center of the screen
        screen_x = screen_w / 2 + (screen_x - screen_w / 2) * speed_multiplier
        screen_y = screen_h / 2 + (screen_y - screen_h / 2) * speed_multiplier

        # Smooth the movement using Linear Interpolation (Lerp)
        clocX = plocX + (screen_x - plocX) / smooth_factor
        clocY = plocY + (screen_y - plocY) / smooth_factor

        # Clip to screen boundaries safely
        clocX = np.clip(clocX, 0, screen_w)
        clocY = np.clip(clocY, 0, screen_h)

        pyautogui.moveTo(clocX, clocY)
        plocX, plocY = clocX, clocY
        
        # Reset mode baselines when moving
        scroll_start_y = None
        zoom_start_dist = None

    # ---------------- 2. LEFT CLICK ----------------
    elif gesture == "LEFT_CLICK":
        pyautogui.click()
        cv2.putText(frame, "Left Click", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        scroll_start_y = None
        zoom_start_dist = None

    # ---------------- 3. RIGHT CLICK ----------------
    elif gesture == "RIGHT_CLICK":
        pyautogui.rightClick()
        cv2.putText(frame, "Right Click", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        scroll_start_y = None
        zoom_start_dist = None

    # ---------------- 4. ULTRA-SMOOTH SCROLL ----------------
    elif gesture == "SCROLL" and len(lmList) != 0:
        y_current = lmList[8][2]

        if scroll_start_y == None:
            scroll_start_y = y_current  # Lock starting point when gesture activates

        # Calculate tracking offsets
        travel_distance = scroll_start_y - y_current

        # Lift hand up -> Scroll UP smoothly
        if travel_distance > 15:
            scroll_amount = int(np.interp(travel_distance, [15, 100], [10, 80]))
            pyautogui.scroll(scroll_amount)
            cv2.putText(frame, f"Scrolling UP (+{scroll_amount})", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        # Lower hand down -> Scroll DOWN smoothly
        elif travel_distance < -15:
            scroll_amount = int(np.interp(travel_distance, [-15, -100], [10, 80]))
            pyautogui.scroll(-scroll_amount)
            cv2.putText(frame, f"Scrolling DOWN (-{scroll_amount})", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        else:
            cv2.putText(frame, "Scroll Lock Mode", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # ---------------- 5. ZOOM IN / OUT (Fixed Hotkeys & Logic) ----------------
    elif len(fingers) >= 5 and fingers[1:] == [1, 1, 1, 1] and len(lmList) != 0:
        # Measure Euclidean distance between Thumb tip (4) and Pinky tip (20)
        current_dist = ((lmList[20][1] - lmList[4][1])**2 + (lmList[20][2] - lmList[4][2])**2)**0.5
        
        if zoom_start_dist == None:
            zoom_start_dist = current_dist
            
        zoom_ratio = current_dist / zoom_start_dist
        
        # Flare fingers wide open -> ZOOM OUT
        if zoom_ratio > 1.15:  
            pyautogui.hotkey('ctrl', '-')
            zoom_start_dist = current_dist  # Reset baseline
            cv2.putText(frame, "ZOOM OUT", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)
            
        # Crunch fingers into a claw shape -> ZOOM IN
        elif zoom_ratio < 0.85: 
            pyautogui.hotkey('ctrl', '+')
            zoom_start_dist = current_dist  # Reset baseline
            cv2.putText(frame, "ZOOM IN", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        else:
            cv2.putText(frame, "Zoom Mode Ready", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # ---------------- VOLUME / IDLE ----------------
    elif gesture == "VOLUME":
        cv2.putText(frame, "Volume Mode", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        scroll_start_y = None
        zoom_start_dist = None
        
    else:
        scroll_start_y = None
        zoom_start_dist = None

    # Render Frame Feed
    cv2.imshow("AI Virtual Mouse Feed", frame)
    
    # Hit 'ESC' to exit program smoothly
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()