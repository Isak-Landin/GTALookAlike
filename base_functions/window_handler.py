import pygetwindow
import pyautogui
import cv2
import time


def get_window_of_interest(name):
    windows = pygetwindow.getWindowsWithTitle(name)
    window = windows[0]

    return window


def calculate_region(window_id):
    window_region = (window_id.topleft[0], window_id.topleft[1], window_id.width, window_id.height)
    return window_region


def focus_window(window_id):
    if window_id.isActive is False:
        time.sleep(0.5)
        window_id.minimize()
        time.sleep(0.2)
        window_id.restore()

