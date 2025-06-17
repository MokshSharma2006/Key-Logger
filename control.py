from pynput.mouse import Controller
from pynput.keyboard import Controller


def controlMouse():

    print("Mouse control started")

    mouse = Controller()
    mouse.position = (500, 200)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Hello, world!")

controlKeyboard()