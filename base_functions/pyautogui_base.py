import pyautogui


def find_image_center_move_click(image, region, confidence):
    image_looked_for = find_image(image=image, region=region, confidence=confidence)
    center = center_coordinates(image_looked_for)
    move_to_coordinates(center)
    click()


def center_coordinates(region):
    center = pyautogui.center(region)
    return center


def find_image(image, region, confidence):
    looked_for = pyautogui.locateOnScreen(image, region=region, confidence=confidence)
    return looked_for


def move_to_coordinates(coordinates, duration):
    pyautogui.moveTo(coordinates, duration=duration)


def click():
    pyautogui.click()