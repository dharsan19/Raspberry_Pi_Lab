## [1. To write a python program to display(scrolling) “RASPBERRY PI ” in sensehat LED matrix display and execute  it in the Sense HAT  simulator](https://trinket.io/python/8742ab555d)
```py
from sense_hat import SenseHat
import time

sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)

message = "RASPBERRY PI"

speed = 1
text_color = green

while True:
    sense.show_message(message, speed, text_color)

```

## [2. To write a python program to display “give way” traffic symbol and diode  symbol and execute  it in the Sense HAT  simulator](https://trinket.io/python/86b428b2b0)

```py
from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
def space():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
def diode():
    P = pink
    O = nothing
    logo = [
    O, O, O, P, P, O, O, O,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, P, O, O, P, O, O,
    O, P, O, O, O, O, P, O,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    ]
    return logo
def giveway():
    P = pink
    O = nothing
    logo = [
    P, P, P, O, O, O, O, O,
    P, P, P, P, O, O, O, O,
    P, P, O, P, P, O, O, O,
    P, P, O, O, P, P, O, O,
    P, P, O, O, P, P, P, O,
    P, P, O, P, P, P, O, O,
    P, P, P, P, O, O, O, O,
    P, P, P, O, O, O, O, O,
    ]
    return logo
images = [diode, space, giveway, space]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
```

## POST LAB QUESTIONS
## 1. Write the statements to display in red clour and orange clour in Sense HAT  matrix display
## [RED](https://trinket.io/python/bbdbb005cb)
```py
from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
def r():
    R = red
    logo = [
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    ]
    return logo
images = [r]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
```
## [BLUE](https://trinket.io/python/e43f0adbca)
```py
from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
blue = (0, 0, 255)
def b():
    B = blue
    logo = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    ]
    return logo
images = [b]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
```
## [2. Give the python code to display Nike symbol in blue color](https://trinket.io/python/e3554e8f88)
```py
from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
blue = (0, 0, 255)
white = (255,255,255)
def b():
    B = blue
    O = white
    logo = [
    B, B, B, O, O, O, O, O,
    O, B, B, B, O, O, O, O,
    O, O, B, B, B, O, O, O,
    O, O, O, B, B, B, O, O,
    O, O, O, O, B, B, B, O,
    O, O, O, O, O, B, B, B,
    O, O, O, O, B, B, B, O,
    O, O, O, B, B, B, O, O,
    ]
    return logo
images = [b]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
```