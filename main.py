import time
from pytesseract import pytesseract
import cv2
from PIL import ImageGrab
import pyperclip
import ctypes
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

while True:
    time.sleep(1)
    if ImageGrab.grabclipboard() is not None and type(ImageGrab.grabclipboard()) is not list:
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        curr_window = user32.GetForegroundWindow()
        thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
        klid = user32.GetKeyboardLayout(thread_id)
        ImageGrab.grabclipboard().save('test.png')
        img = cv2.imread('test.png')
        config = r'--oem 3 --psm 6'
        if klid == 67699721:
            pyperclip.copy(pytesseract.image_to_string(img, config=config))
        elif klid == 68748313:
            pyperclip.copy(pytesseract.image_to_string(img, config=config, lang='rus'))
