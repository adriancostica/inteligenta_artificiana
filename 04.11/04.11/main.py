import pyautogui
import keyboard
import time

deelayTime = 2
scrollTimes = 0

def clickAndSearch(imagePath, url):
    if pyautogui.locateOnScreen(imagePath, confidence=0.7) != None:
        camp_img = pyautogui.locateOnScreen(imagePath, confidence=0.7)
        pyautogui.click(camp_img)
        time.sleep(deelayTime)
        pyautogui.write(url)
        pyautogui.press("enter")
        time.sleep(deelayTime)

def click(imagePath):
    if pyautogui.locateOnScreen(imagePath, confidence=0.7) != None:
        camp_img = pyautogui.locateOnScreen(imagePath, confidence=0.7)
        pyautogui.click(camp_img)
        time.sleep(deelayTime)

def scrollDown():
    pyautogui.scroll(-345)

def cautare_google():
    clickAndSearch("./search_bar.png", "https://youtube.com")
    clickAndSearch("./search_bar_ytb.png", "zona it")
    click("./channelIco.png")
    #click("./subBtn.png")
    click("./videos.png")

def coordonate():
    print(pyautogui.position())

time.sleep(deelayTime)

def scrollAndClick():
    time.sleep(1)
    pyautogui.keyDown("CTRL")
    pyautogui.click(pyautogui.position())
    pyautogui.keyUp("CTRL")
    click("./closeBtn.png")
    click("./closeBtn2.png")
    time.sleep(2)
    click("./videos.png")
    for t in range(scrollTimes):
        scrollDown()

while 1:
    if keyboard.is_pressed('s'):
        cautare_google()
        time.sleep(2)
        while 1:
            if keyboard.is_pressed('p'):
                break
            scrollTimes = scrollTimes + 1
            pyautogui.moveTo(1331, 573)
            time.sleep(2)
            scrollAndClick()
    elif keyboard.is_pressed('p'):
        break
#cautare_google()