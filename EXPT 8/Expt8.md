## Write a Python program to run a stepper motor in Python with following conditions. Assume unipolar stepper motor. The step sequence should be '1010', '0110', '0101', '1001'. The term ‘1’ represents excitation of stepper motor winding. The motor has to move ‘forward’ and ‘reverse’ based on user request. Assume number of steps as 2. Print the winding sequence as well as direction i.e. forward of reverse.
```python
import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the stepper motor
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

# Define the step sequence
SEQ = ['1010', '0110', '0101', '1001']

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Define a function to set the motor winding sequence
def set_sequence(seq):
    GPIO.output(IN1, int(seq[0]))
    GPIO.output(IN2, int(seq[1]))
    GPIO.output(IN3, int(seq[2]))
    GPIO.output(IN4, int(seq[3]))

# Define a function to move the motor forward
def move_forward(steps):
    print("Moving forward...")
    for i in range(steps):
        for seq in SEQ:
            set_sequence(seq)
            time.sleep(0.01)

# Define a function to move the motor in reverse
def move_reverse(steps):
    print("Moving in reverse...")
    for i in range(steps):
        for seq in reversed(SEQ):
            set_sequence(seq)
            time.sleep(0.01)

# Prompt the user for the direction and number of steps
direction = input("Enter the direction (forward/reverse): ")
steps = int(input("Enter the number of steps: "))

# Move the motor in the specified direction
if direction == "forward":
    move_forward(steps)
elif direction == "reverse":
    move_reverse(steps)
else:
    print("Invalid direction")

# Clean up the GPIO pins
GPIO.cleanup()

```