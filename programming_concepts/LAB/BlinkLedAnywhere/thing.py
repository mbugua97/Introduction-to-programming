import RPi.GPIO as GPIO

LED_PIN = 23


class PiThing(object):
  """Raspberry Pi Internet 'Thing'. """
  
  def __init__(self):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)    #LED as an output
       

  def set_led(self, value):
    """Change the LED to the passed in valaue, either True for on or False for off. """
    GPIO.output(LED_PIN, value)
