import math


class GestureDetector:
    def __init__(self):
        self.prev_x = 0
        self.prev_y = 0
        self.smoothening = 5

    def detect_gesture(self, fingers, lmList):
        """
        Returns gesture type based on fingers state
        """

        if len(lmList) == 0:
            return "NO_HAND"

        # Only Index Finger Up → MOVE CURSOR
        if fingers == [0, 1, 0, 0, 0]:
            return "MOVE"

        # Index + Thumb close → LEFT CLICK
        if self.is_click(lmList, 4, 8):
            return "LEFT_CLICK"

        # Middle + Thumb close → RIGHT CLICK
        if self.is_click(lmList, 4, 12):
            return "RIGHT_CLICK"

        # Index + Middle up → SCROLL
        if fingers == [0, 1, 1, 0, 0]:
            return "SCROLL"

        # Thumb + Index distance → VOLUME
        if fingers == [1, 1, 0, 0, 0]:
            return "VOLUME"

        return "IDLE"

    def is_click(self, lmList, p1, p2, threshold=40):
        """
        Detect pinch gesture
        """

        x1, y1 = lmList[p1][1], lmList[p1][2]
        x2, y2 = lmList[p2][1], lmList[p2][2]

        distance = math.hypot(x2 - x1, y2 - y1)

        return distance < threshold