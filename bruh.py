import speech_recognition as sr
import pydirectinput
import time
import pyautogui


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=9999)
        said = " "

        try:
            said = r.recognize_google(audio)
            print(said)
            

        except:
            print("can't hear ya dud")

    return said 

i = 0
while i < 9999:
    text = get_audio()

    if "left" in text:
        pydirectinput.keyDown('a')
        time.sleep(1)
        pydirectinput.keyUp('a')

    if "silent" in text:
        pydirectinput.keyDown('shift')
        time.sleep(5)
        pydirectinput.keyUp('shift')

    if "right" in text:
        pydirectinput.keyDown('d')
        time.sleep(1)
        pydirectinput.keyUp('d')

    if "up" in text:
        pydirectinput.keyDown('w')
        time.sleep(1)
        pydirectinput.keyUp('w')

    if "down" in text:
        pydirectinput.keyDown('s')
        time.sleep(1)
        pydirectinput.keyUp('s')

    if "jump" in text:
        pydirectinput.keyDown('space')
        time.sleep(1)
        pydirectinput.keyUp('space')

    if "long up" in text:
        pydirectinput.keyDown('w')
        time.sleep(5)
        pydirectinput.keyUp('w')

    if "long left" in text:
        pydirectinput.keyDown('a')
        time.sleep(5)
        pydirectinput.keyUp('a')

    if "long right" in text:
        pydirectinput.keyDown('d')
        time.sleep(5)
        pydirectinput.keyUp('d')

    if "long down" in text:
        pydirectinput.keyDown('s')
        time.sleep(5)
        pydirectinput.keyUp('s')

    if "inspect" in text:
        pydirectinput.keyDown('f')
        pydirectinput.keyUp('f')

    if "back" in text:
        pydirectinput.keyDown('r')
        time.sleep(1)
        pydirectinput.keyUp('r')

    if "crouch" in text:
        pydirectinput.keyDown('ctrl')
        time.sleep(1)
        pydirectinput.keyUp('ctrl')

    if "Crouch" in text:
        pydirectinput.keyDown('ctrl')
        time.sleep(1)
        pydirectinput.keyUp('ctrl')

    if "use" in text:
        pydirectinput.keyDown('e')
        pydirectinput.keyUp('e')

    if "menu" in text:
        pydirectinput.keyDown('esc')
        pydirectinput.keyUp('esc')

    if "mom" in text:
        pydirectinput.keyDown('alt')
        pydirectinput.keyUp('f4')
        time.sleep(3)
        pydirectinput.keyUp('f4')
        pydirectinput.keyDown('alt')

    if "mum" in text:
        pydirectinput.keyDown('alt')
        pydirectinput.keyDown('f4')
        time.sleep(3)
        pydirectinput.keyUp('f4')
        pydirectinput.keyUp('alt')

