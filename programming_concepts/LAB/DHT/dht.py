import Adafruit_DHT

# Set the sensor type and GPIO pin
sensor = Adafruit_DHT.DHT22
pin = 18 

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print(temperature)
    print(humidity)
else:
    print("Failed to retrieve data from humidity sensor")
