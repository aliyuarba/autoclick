import pyautogui
import time
import random

pyautogui.hotkey('win','3')
time.sleep(0.1)
for i in range(1,101):
    pyautogui.write(str(i))
    # time.sleep(0.01)
    pyautogui.hotkey('enter')