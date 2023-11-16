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

def scene2():
    '''
    SCENE 2:
    'the castle vanished, and the rabbit was very confused'
    '''
    display.show(2)
    # lights
    for i in range (0, 10):
        lights[i] = blue
    lights.show()

while True:
    scene = 0
    # click button A when you are ready for the next scene
    if button_a.was_pressed():
        scene += 1
        sleep(200)
    if scene == 1:
        scene1()
    elif scene == 2:
        scene2()

