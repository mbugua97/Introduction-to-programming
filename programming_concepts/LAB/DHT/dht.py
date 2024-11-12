import Adafruit_DHT

# Set the sensor type and GPIO pin
sensor = Adafruit_DHT.DHT11
pin = 18  # GPIO pin number

humidity, temperature = Adafruit_DHT.read_retry(sensor, str(pin))

if humidity is not None and temperature is not None:
    print(temperature)
    print(humidity)
else:
    print("Failed to retrieve data from humidity sensor")
