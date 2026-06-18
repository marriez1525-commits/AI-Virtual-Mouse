import pyautogui

pyautogui.FAILSAFE = False

class MouseController:

    def __init__(self):
        self.screen_w, self.screen_h = pyautogui.size()


    def move_cursor(self, x, y):
        """Move mouse cursor"""
        pyautogui.moveTo(x, y)

    def left_click(self):
        """Left click"""
        pyautogui.click()

    def right_click(self):
        """Right click"""
        pyautogui.rightClick()

    def double_click(self):
        """Double click"""
        pyautogui.doubleClick()

    def scroll(self, amount):
        """Scroll up/down"""
        pyautogui.scroll(amount)