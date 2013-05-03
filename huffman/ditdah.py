
import time
import win32api

spacebar = 32

start = {}
down = False
carryon = True

print('start mashing that spacebar')

while carryon:
    if win32api.GetKeyState(spacebar):
        down = True
        start = time.time()
    else:
        if down:
            down = False
            print(time.time() - start)

def followThatScanCode():
    # brute-force figure out which keycode is the spacebar
    for rep in range(50):
        print('get ready')

    liveones = []
    for key in range(130): # I think this is more codes than the keyboard has
        initial = win32api.GetKeyState(key)
        for rep in range(50):
            current = win32api.GetKeyState(key)
            print(current) # this should slow the old girl down a bit, eh what?
            if current != initial:
                print('{0} moved!')
                liveones.append(key)

    for rep in range(50):
        print('okay, chill out already')

# 
