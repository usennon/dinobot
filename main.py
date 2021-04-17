import pyautogui
from PIL import Image, ImageGrab, ImageOps
from numpy import array

window = pyautogui.getWindowsWithTitle(title='Play T-Rex Dinosaur Game Online - elgooG - Opera')
window[0].activate()
pyautogui.press('up')

while True:
    x1, y1, a, b = 709, 520, 120, 36
    box = (x1, y1, x1 + a, y1 + b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    arr = array(gray.getcolors())
    value = arr.sum()
    print(value)
    if value != 4567:
        pyautogui.press('space')
