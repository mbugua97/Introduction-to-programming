import Adafruit_DHT
import time

def readings():
    DHT_SENSOR = Adafruit_DHT.DHT11  # Initializes the DHT11 sensor from Adafruit_DHT module
    DHT1_GPIO = 24  # Sets DHT1 to GPIO 24 (physical pin 18)
    DHT2_GPIO = 2   # Sets DHT2 to GPIO 2 (physical pin 3)
    

        # Try reading from the first DHT sensor
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT1_GPIO)
    if humidity is not None and temperature is not None:
            return humidity, temperature
    else:
            # If the first sensor fails, try reading from the second DHT sensor
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT2_GPIO)
            return humidity, temperature if humidity is not None and temperature is not None else None

while True:
    data = readings()
    if data is None:
        message = "Check the DHT sensors"
    else:
        humidity, temperature = data
        message = f"Humidity: {humidity}%, Temperature: {temperature}°C"
    
    print(message)
    time.sleep(2)  # Add a delay between readings to avoid spamming the sensor
