import math

class GestureDetector:
    def __init__(self):
        pass
    def detect_gesture(self, fingers, lmList):
        if len(lmList) == 0:
            return "NO_HAND"

        # 💡 Prioritize MOVE Mode: Strict check for ONLY Index Finger up
        if fingers == [0, 1, 0, 0, 0]:
            return "MOVE"

        # Index + Thumb close → LEFT CLICK (Tightened threshold to 30 pixels)
        if fingers[1] == 1 and self.is_click(lmList, 4, 8, threshold=30):
            return "LEFT_CLICK"

        # Middle + Thumb close → RIGHT CLICK (Tightened threshold to 30 pixels)
        if fingers[2] == 1 and self.is_click(lmList, 4, 12, threshold=30):
            return "RIGHT_CLICK"

        # Index + Middle up → SCROLL
        if fingers == [0, 1, 1, 0, 0]:
            return "SCROLL"

        # Thumb + Index distance → VOLUME
        if fingers == [1, 1, 0, 0, 0]:
            return "VOLUME"

        return "IDLE"

    def is_click(self, lmList, p1, p2, threshold=30):
        x1, y1 = lmList[p1][1], lmList[p1][2]
        x2, y2 = lmList[p2][1], lmList[p2][2]
        distance = math.hypot(x2 - x1, y2 - y1)
        
        return distance < threshold