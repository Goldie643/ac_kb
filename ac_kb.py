from pynput import keyboard
from playsound import playsound
import string

spam = []

sounds_dir = "sounds/"

def on_press(key):
    try:
        playsound(sounds_dir+key.char+".wav",False)
    except:
        pass
        # print("Bad character")

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

while True:
    continue