# DHARSAN S RA2011003010732
from time import sleep
import paho.mqtt.client as mqtt 
import json

host = 'demo.thingsboard.io' 
access_token = 'd8iPsPtMZMkqD5eyW7W4'
sensor_data = {'temperature':0,'humidity':0,'windspeed':0,'rain sensor':'not rainy'} 
client = mqtt.Client()
client.username_pw_set(access_token)

while True:
    sensor_data['temperature'] = 70
    sensor_data['humidity'] = 40
    sensor_data['windspeed'] = 50 
    sensor_data['rain sensor'] = 'not rainy' 
    client.connect(host, 1883, 20)
    client.publish('v/devices/me/telemetry',json.dumps(sensor_data),1) 
    client.disconnect()
    sleep(10)  