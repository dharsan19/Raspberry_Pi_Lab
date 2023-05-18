## LED Blinking
```py
import time
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
GPIO.setup(18, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
while True:
	GPIO.output(18,True)  ## Turn on Led
	time.sleep(2)         ## Wait for one second
	GPIO.output(18,False) ## Turn off Led
	time.sleep(2)         ## Wait for one second
```
## Brightness Control
```py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 100)
pwm.start(0)

try:
    while True:
        duty_cycle = float(input("Enter the Duty cycle : " ))
        pwm.ChangeDutyCycle(duty_cycle)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
```
# POST LAB QUESTION
## 2. Write python code in which LED  only make blinking with medium and highest brightness
```py
import RPi.GPIO as GPIO
led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

while True:
    duty_s = input("Enter Brightness (Low, Medium, High): ")
    if duty_s == "Low":
      duty = 10
    elif duty_s == "Medium":
      duty = 1000
    elif duty_s == "High":
      duty = 10000
      pwm_led.ChangeDutyCycle(duty)
```