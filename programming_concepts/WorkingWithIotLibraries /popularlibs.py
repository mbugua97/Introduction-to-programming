#gpio libraries

#TURN ON AND OFF AN LED

# RPi.GPIO LIB

import RPi.GPIO  as GPIO
import time

my_pin=24
# HIGH(ON) OR LOW(OFF)
GPIO.setmode(GPIO.BCM)
GPIO.setup(my_pin,GPIO.OUT)
GPIO.output(my_pin,GPIO.HIGH)# IT WILL TURN the gpio to an high state
time.sleep(3)
GPIO.output(my_pin,GPIO.LOW)# IT WILL TURN the gpio to an low state
time.sleep(3)
