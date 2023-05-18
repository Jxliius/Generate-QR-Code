import os
import keyboard

while True:
    if keyboard.read_key() == "r":
        print("You pressed r")
    if keyboard.read_key() == 'ä':
        os.system('clear')