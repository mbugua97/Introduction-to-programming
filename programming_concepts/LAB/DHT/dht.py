import Adafruit_DHT

# Set the sensor type and GPIO pin
sensor = Adafruit_DHT.DHT22
pin = 4  


humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Humidity: {humidity:.2f}%")
else:
    print("Failed to retrieve data from humidity sensor")
