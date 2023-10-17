import pyautogui
import time
import random
import pyperclip

messages = [" #R#rMua đồ lam nghịch thiên#r#281", " #R#rMua Cửu khúc châu 150k#r#280 ", " #R#rBán rùa, lăng tiêu, mana giá rẻ hơn chợ#r#284 "," #BXin lũi nếu chat hơi nhìu#281"]
time.sleep(2)
for i in range(999):
    for line in messages:
        pyautogui.typewrite(str(random.randint(111111, 999999)))
        pyperclip.copy(line)
        pyautogui.hotkey("ctrl","v")
        time.sleep(3)
        pyautogui.press("enter")
        time.sleep(300)