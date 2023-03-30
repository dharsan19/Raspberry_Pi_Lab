## To turn an LED on and off with a push switch so that it toggles between on and off each time switch is pressed.

```python
import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the LED and switch
LED_PIN = 18
SWITCH_PIN = 17

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define a function to toggle the LED
def toggle_led(channel):
    if GPIO.input(LED_PIN):
        GPIO.output(LED_PIN, GPIO.LOW)
    else:
        GPIO.output(LED_PIN, GPIO.HIGH)

# Set up the switch to trigger the toggle_led function on a falling edge (i.e. when the switch is pressed)
GPIO.add_event_detect(SWITCH_PIN, GPIO.FALLING, callback=toggle_led, bouncetime=200)

# Loop forever, waiting for events
while True:
    time.sleep(1)

# Clean up the GPIO pins
GPIO.cleanup()

```