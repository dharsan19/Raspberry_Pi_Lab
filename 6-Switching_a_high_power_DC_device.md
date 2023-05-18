## Switching a High-Power DC Device
```py
import RPi.GPIO as GPIO

# Set up GPIO pin for relay control
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Prompt user for input
while True:
    user_input = input("Enter 'on' to turn on the relay or 'off' to turn it off: ")
    
    if user_input.lower() == "on":
        # Turn on relay
        GPIO.output(18, GPIO.HIGH)
    elif user_input.lower() == "off":
        # Turn off relay
        GPIO.output(18, GPIO.LOW)
    else:
        # Invalid input
        print("Invalid input. Please try again.")

# Clean up GPIO pins
GPIO.cleanup()
```