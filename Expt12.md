```py
from bottle import route, run, template, request, static_file
import json
import random

sensor_data = {
    'temperature': 0,
    'humidity': 0,
    'wind_speed': 0,
    'rainy': 0,
}
arr = []

@route('/')
def index():
    for i in range(2):
        sensor_data['temperature'] = random.randint(0, 100)
        sensor_data['humidity'] = random.randint(0, 100)
        sensor_data['wind_speed'] = random.randint(0, 100)
        sensor_data['rainy'] = random.randint(0, 1)
        arr.append(sensor_data)
    return json.dumps(arr)

run(host='localhost', port=8080, debug=True)
```
