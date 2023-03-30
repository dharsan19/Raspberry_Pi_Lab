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
# DHARSAN S
# RA2011003010732
from sense_hat import SenseHat
import time

sense = SenseHat()

# Set up colors
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Define images
give_way = [
    black, black, black, red, red, black, black, black,
    black, black, red, yellow, yellow, red, black, black,
    black, red, yellow, white, white, yellow, red, black,
    red, yellow, white, white, white, white, yellow, red,
    red, yellow, white, white, white, white, yellow, red,
    black, red, yellow, white, white, yellow, red, black,
    black, black, red, yellow, yellow, red, black, black,
    black, black, black, red, red, black, black, black
]

diode = [
    black, black, black, white, white, black, black, black,
    black, black, black, white, white, black, black, black,
    black, black, black, white, white, black, black, black,
    black, black, black, white, white, black, black, black,
    black, black, black, white, white, black, black, black,
    black, black, black, white, white, black, black, black,
    black, black, black, white, white, black, black, black,
    black, black, black, white, white, black, black, black
]

# Display give_way symbol
sense.set_pixels(give_way)
time.sleep(5)

# Display diode symbol
sense.set_pixels(diode)
time.sleep(5)

# Clear the display
sense.clear()

```