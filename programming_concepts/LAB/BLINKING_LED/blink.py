import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin=18

GPIO.setup(led_pin,GPIO.OUT)

GPIO.output(led_pin,True)
time.sleep(1)
GPIO.output(led_pin,False)
time.sleep(1)