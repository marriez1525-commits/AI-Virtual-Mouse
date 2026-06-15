import numpy as np


class Utils:

    def __init__(self):
        self.prev_x = 0
        self.prev_y = 0

    def smooth_cursor(self, x, y, alpha=0.5):
        """
        Smooth cursor movement (removes shaking)
        """
        x = self.prev_x + (x - self.prev_x) * alpha
        y = self.prev_y + (y - self.prev_y) * alpha

        self.prev_x, self.prev_y = x, y

        return x, y

    def map_coordinates(self, x, y,
                         cam_w=640, cam_h=480,
                         screen_w=1920, screen_h=1080):

        """
        Map camera coordinates to screen coordinates
        """

        screen_x = np.interp(x, [0, cam_w], [0, screen_w])
        screen_y = np.interp(y, [0, cam_h], [0, screen_h])

        return screen_x, screen_y

    def calculate_distance(self, p1, p2):

        """
        Calculate Euclidean distance
        """
        return ((p2[0] - p1[0]) ** 2 +
                (p2[1] - p1[1]) ** 2) ** 0.5