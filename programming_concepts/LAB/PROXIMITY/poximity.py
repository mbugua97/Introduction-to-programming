import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG = 23
ECHO = 24

# Setup GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Trigger the sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure the time until the echo is received
    start_time = None
    end_time = None

    # Wait for the pulse to start
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Wait for the pulse to end
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Ensure that start_time and end_time were set
    if start_time is None or end_time is None:
        return None  # or return a value indicating the measurement failed

    # Calculate the distance based on time
    time_elapsed = end_time - start_time
    distance = (time_elapsed * 34300) / 2  # in cm
    return distance

try:
    while True:
        dist = measure_distance()
        if dist is not None:
            print(f"Distance: {dist} cm")
        else:
            print("Failed to measure distance.")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
