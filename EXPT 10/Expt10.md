## To write a python program to display(scrolling) “RASPBERRY PI ” in sensehat LED matrix display and execute  it in the Sense HAT  simulator 

```python
# Dharsan S
# RA2011003010732
from sense_hat import SenseHat
import time

sense = SenseHat()

# Set up colors
red = (255, 0, 0)
green = (0, 255, 0)

# Set up message to scroll
message = "RASPBERRY PI"

# Set up scrolling speed and text color
speed = 1
text_color = green

# Scroll the message continuously
while True:
    sense.show_message(message, speed, text_color)

```

## To write a python program to display “give way” traffic symbol and diode  symbol and execute  it in the Sense HAT  simulator 

```python
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