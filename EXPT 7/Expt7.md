# Programming on Interrupts
## --> TASK 1
## Configure two I/O pin for LOW to HIGH  transition Interrupt source and HIGH to LOW transition Interrupt source

```python
# DHARSAN S 
# RA2011003010732

import RPi.GPIO as GPIO
import time

# Define the GPIO pins to be used
pin1 = 4   # GPIO 4 (pin 7)
pin2 = 17  # GPIO 17 (pin 11)

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin1 as input with a pull-down resistor
GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set pin2 as input with a pull-up resistor

# Define the interrupt handlers
def pin1_callback(channel):
    print("Pin 1 triggered!")
    # TODO: Add code here to switch on LED

def pin2_callback(channel):
    print("Pin 2 triggered!")
    # TODO: Add code here to switch on LED

# Add the interrupt handlers to the GPIO pins
GPIO.add_event_detect(pin1, GPIO.RISING, callback=pin1_callback, bouncetime=200)
GPIO.add_event_detect(pin2, GPIO.FALLING, callback=pin2_callback, bouncetime=200)

# Wait for interrupts
while True:
    time.sleep(1)
```
# --> TASK 2
## Write two  Interrupt Service Routine(IRS) for LOW to HIGH  transition Interrupt(ISRL2H) and HIGH to LOW transition Interrupt(ISRH2L), which will display( print)the occurrence of positive edge or negative edge  Interrupt when it is called.  

```python
# DHARSAN S 
# RA2011003010732

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Set up the input pin for ISR 1
input_pin_1 = 18
GPIO.setup(input_pin_1, GPIO.IN)

# Set up the input pin for ISR 2
input_pin_2 = 23
GPIO.setup(input_pin_2, GPIO.IN)

# Initialize the counters for the positive and negative edge interrupts
pos_edge_count = 0
neg_edge_count = 0

# Define the ISR for low-to-high transition on input pin 1
def ISR_L2H(channel):
    global pos_edge_count
    pos_edge_count += 1
    print("ISR 1: Positive edge interrupt detected! Count = ", pos_edge_count)

# Define the ISR for high-to-low transition on input pin 2
def ISR_H2L(channel):
    global neg_edge_count
    neg_edge_count += 1
    print("ISR 2: Negative edge interrupt detected! Count = ", neg_edge_count)

# Set up the interrupts for both input pins
GPIO.add_event_detect(input_pin_1, GPIO.RISING, callback=ISR_L2H, bouncetime=200)
GPIO.add_event_detect(input_pin_2, GPIO.FALLING, callback=ISR_H2L, bouncetime=200)

# Keep the program running
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted by user")

# Clean up the GPIO
GPIO.cleanup()
```

## --> TASK 3
## Make ON of  LED1 for a while, if a positive edge interrupt signal occurs and call ISRL2H. Make ON of  LED2  for a while, if the negative edge Interrupt signal occurs and call ISRH2L. Don’t use inbuilt function GPIO.add_event_detect() to detect interrupt.

```python
# DHARSAN S 
# RA2011003010732

import RPi.GPIO as GPIO
import time

# Set up GPIO pins
led1 = 27
led2 = 31
input1 = 18
input2 = 24
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(input1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(input2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Variables to track edge interrupts
pos_edge = 0
neg_edge = 0

# Define interrupt service routines
def ISRL2H(channel):
    print("Positive edge interrupt detected!")
    global pos_edge
    GPIO.output(led1, GPIO.HIGH)
    pos_edge += 1
    time.sleep(1)
    GPIO.output(led1, GPIO.LOW)
    print("Number of positive edges:", pos_edge)

def ISRH2L(channel):
    print("Negative edge interrupt detected!")
    global neg_edge
    GPIO.output(led2, GPIO.HIGH)
    neg_edge += 1
    time.sleep(1)
    GPIO.output(led2, GPIO.LOW)
    print("Number of negative edges:", neg_edge)

# Set up interrupts
GPIO.add_event_detect(input1, GPIO.RISING, callback=ISRL2H, bouncetime=200)
GPIO.add_event_detect(input2, GPIO.FALLING, callback=ISRH2L, bouncetime=200)

# Turn on LED1 for a short time to check positive edge interrupt
GPIO.output(led1, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(led1, GPIO.LOW)

# Turn on LED2 for a short time to check negative edge interrupt
GPIO.output(led2, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(led2, GPIO.LOW)

# Wait for interrupts to occur
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
```