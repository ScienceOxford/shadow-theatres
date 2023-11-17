# Imports go at the top
from microbit import *
import neopixel
import music

lights = neopixel.NeoPixel(pin16, 10)

# define your colours
red = (100, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 100)
white = (100, 100, 100)

# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.HEART)
    sleep(1000)
    display.scroll('Hello')