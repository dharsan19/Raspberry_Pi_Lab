## To write a python program to display temperature, humidity, wind speed data and rain sensor data (rainy or not)  in a webpage(localhost)  using JSON format using bottle library (get sensor data from user and  which is coming from a sensor )

```py
from bottle import route,run,request 
tempr=input("enter the temperature value:") 
hum=input("enter the humidity:") 
ws=input("enter the windspeed:") 
rain=input("enter rainy or not:")
@route('/')
def getsens(): 
    sensor_log=[{'sensor':'Temperature','value':tempr},
    {'sensor':'humidity','value':hum},
    {'sensor':'wind speed','value':ws},
    {'sensor':'rain','value':rain}]
    return dict(data=sensor_log)
run(host='localhost',port=7000,debug=True)
```