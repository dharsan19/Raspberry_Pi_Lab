## [Switching a High-Power DC Device](https://create.withcode.uk/python/MyJ)
```py
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    user_input = input("Enter 'on' to turn on the relay or 'off' to turn it off: ")
    
    if user_input.lower() == "on":
        GPIO.output(18, GPIO.HIGH)
    elif user_input.lower() == "off":
        GPIO.output(18, GPIO.LOW)
    else:
        print("Invalid input. Please try again.")

GPIO.cleanup()
```