from PIL import ImageGrab, ImageOps
import pyautogui
import numpy
import time

playTheGame = (377, 465)
dinoPlace = (193, 471)

def Start():
    pyautogui.click(playTheGame)

def Jump():
    pyautogui.keyDown("space")
    time.sleep(0.1)
    print("Jumping...")
    pyautogui.keyUp("space")

def getBox():
    box = (dinoPlace[0]+100,
    dinoPlace[1],
    dinoPlace[0]+100,
    dinoPlace[1]
           )
    img = ImageGrab.grab(box)
    img = ImageOps.grayscale(img)
    arr = numpy.array(img)
    return arr.sun()

Start()
time.sleep(1)
Jump()

while True:
    place = getBox()
    if place < 296400:
        print("an object detected !")
        Jump()
