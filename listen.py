from pynput.mouse import Listener

def on_click(x, y):
    print("Position of current mouse {0}".format((x, y)))



with Listener(on_click=on_click) as l:
    l.join()