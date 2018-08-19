import traceback
from RPi import GPIO
from time import time, sleep

GPIO_TRIG = 19
GPIO_ECHO = 26

def get_distance():
    GPIO.output(GPIO_TRIG, True)

    sleep(0.00001)
    GPIO.output(GPIO_TRIG, False)

    while GPIO.input(GPIO_ECHO) == False:
        pulse_start = time()
    
    while GPIO.input(GPIO_ECHO) == True:
        pulse_stop = time()

    time_elapsed = pulse_stop - pulse_start

    distance = (time_elapsed * 34300) / 2

    return distance

try:
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(GPIO_TRIG, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.OUT)

    GPIO.output(GPIO_TRIG, False)
    print('Waiting for sensor to settle')
    sleep(2)

    while True:
        dist = get_distance()

        print('Distance: {}cm'.format(round(dist, 2))
        sleep(1)

except:
    traceback.print_exc()
    GPIO.cleanup()