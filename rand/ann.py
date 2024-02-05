import random
import pyautogui as pg
import time

animal=('Howle','yedava')
time.sleep(5)

for i in range(100):
    a=random.choice(animal)
    pg.write(a)
    pg.press('enter')