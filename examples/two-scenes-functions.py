from microbit import *
import neopixel
import music

lights = neopixel.NeoPixel(pin16, 10)

# define your colours
red = (100, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 100)
white = (100, 100, 100)

def scene1():
    '''
    SCENE 1:
    'the rabbit walked towards the spooky castle'
    '''
    display.show(1)
    # lights
    for i in range(0, 5):
        lights[i] = red
    for i in range(5, 10):
        lights[i] = white
    lights.show()
    # sound
    music.play(music.BADDY)
    # pause for narration
    sleep(4000)

def scene2():
    '''
    SCENE 2:
    'the castle vanished, and the rabbit was very confused'
    '''
    display.show(2)
    for i in range (0, 10):
        lights[i] = blue
    lights.show()
    # pause for narration
    sleep(5000)

while True:
    scene = 0
    if button_a.was_pressed():
        scene += 1
        sleep(200)
    if scene == 1:
        scene1()
    elif scene == 2:
        scene2()

