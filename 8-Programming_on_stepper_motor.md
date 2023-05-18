## Programming on Stepper Motor
## Write a Python program to run a stepper motor in Python with following conditions. Assume unipolar stepper motor. The step sequence should be '1010', '0110', '0101', '1001'. The term ‘1’ represents excitation of stepper motor winding. The motor has to move ‘forward’ and ‘reverse’ based on user request. Assume number of steps as 2. Print the winding sequence as well as direction i.e. forward of reverse.
```python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
coil_A1_pin = 22
coil_A2_pin = 24
coil_B1_pin = 26
coil_B2_pin = 28
GPIO.setup(coil_A1_pin, GPIO.OUT)
GPIO.setup(coil_A2_pin, GPIO.OUT)
GPIO.setup(coil_B1_pin, GPIO.OUT)
GPIO.setup(coil_B2_pin, GPIO.OUT)
forward = ['1010', '0110', '0101', '1001']
backward = ['1001', '0101', '0110', '1010']
def forw(delay, steps):
    for i in range(steps):
        for step in forward:
            print(step)
            set_step(step)
            time.sleep(delay)
def back(delay, steps):
    for i in range(steps):
        for step in backward:
            print(step)
            set_step(step)
            time.sleep(delay)
def set_step(step):
    GPIO.output(coil_A1_pin, step[0] == '1')
    GPIO.output(coil_A2_pin, step[1] == '1')
    GPIO.output(coil_B1_pin, step[2] == '1')
    GPIO.output(coil_B2_pin, step[3] == '1')
while(True):
    choice = input("Enter your choice - Forward [F/f] -Backward [B/b] - Stop [S/s]: ")
    if(choice == 'F' or choice == 'f'):
        print("Forward Motion")
        set_step('0000')
        forw(1,2)
        set_step('0000')
        time.sleep(2)
    if(choice == 'B' or choice == 'b'):
        print("Backward Motion")
        set_step('0000')
        back(1,2)
        set_step('0000')
        time.sleep(2)
    if(choice == 'S' or choice == 's'):
        print("STOP!!!")
        break
```