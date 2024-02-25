import pyautogui
import time
# pyautogui.useImageNotFoundException()

# pyautogui.hotkey('win','2')
# time.sleep(1)
# for i in range(1,5):
#     pyautogui.hotkey('ctrl','t')
#     time.sleep(0.1)
#     pyautogui.write('youtube.com')
#     time.sleep(0.1)
#     pyautogui.hotkey('del')
#     pyautogui.hotkey('enter')
#     time.sleep(2)
#     pyautogui.hotkey('ctrl','w')
#     time.sleep(0.1)

# pyautogui.hotkey('win','5')
def findmsedge():
    msedge = pyautogui.locateOnScreen('view.png')
    msedge = pyautogui.center(msedge)
    return msedge

# print(findmsedge())
pyautogui.hotkey('win','2')
time.sleep(1)
for i in range(1,10):
    target = findmsedge()
    pyautogui.moveTo(target)
    pyautogui.click()
    time.sleep(45)
    pyautogui.hotkey('ctrl','w')
    time.sleep(1)
    pyautogui.hotkey('f5')
    time.sleep(45)
    # pyautogui.moveTo(msedge)
    # time.sleep(1)
    # pyautogui.click()

pyautogui.hotkey('ctrl','t')
time.sleep(0.5)
pyautogui.write('https://www.youtube.com/')
time.sleep(0.5)
pyautogui.hotkey('del')
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.moveTo(1000,500)
time.sleep(5)
pyautogui.click()
