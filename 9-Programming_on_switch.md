## To turn an LED on and off with a push switch so that it toggles between on and off each time switch is pressed.

```python
from gpiozero import LED,Button
led1=LED(17)
led2=LED(18)
button=Button(2)
led2.on()
while(True):
    button.wait_for_press()
    print("BUTTON PRESSED!!")
    led1.on()
    led2.off()
    button.wait_for_release()
    print("BUTTON RELEASED!!")
    led1.off()
    led2.on()
```