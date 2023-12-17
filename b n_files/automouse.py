import pyautogui as pa
import datetime
import random as rd

# print(datetime.datetime.now().minute)
pa.moveTo(rd.randint(10, 1000), rd.randint(10, 1000), duration=3)
while True:
    now = datetime.datetime.now()
    if now.minute % 20 == 0 and now.second == 0:
        pa.moveTo(rd.randint(10, 1000), rd.randint(10, 1000), duration=2)
        pa.moveTo(rd.randint(10, 1000), rd.randint(10, 1000), duration=2)
