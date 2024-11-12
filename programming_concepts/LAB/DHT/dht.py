import Adafruit_DHT 

def readings(self):
    DHT_SENSOR = Adafruit_DHT.DHT11 # initialises the variable  DHT_SENSOR to specifically hold values from the DHT11 sensor from the Adafruit_DHT module
    DHT1_PIN1 = 18 # initiates DHT_PIN1 to pin 18 of the raspberry pi
    DHT2_PIN2 = 3 #initaites  DHT_PIN2 to pin 3 of the raspberry pi
    try:
        try:
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT1_PIN1) 
            return (humidity,temperature)
        except:
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT2_PIN2)
            return (humidity,temperature)
    except:
        return None

while True:
    data=readings()
    if data is None:
        message="check the dht's"
        print(message)
    else:
        message=readings
        print(message)