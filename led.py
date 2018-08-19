from time import sleep
from RPi import GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        GPIO.output(18, True)
        sleep(1)

        GPIO.output(23, True)
        sleep(1)

        GPIO.output(24, True)
        sleep(1)

        GPIO.output(18, False)
        sleep(1)

        GPIO.output(23, False)
        sleep(1)

        GPIO.output(24, False)
        sleep(1)

except:
    GPIO.cleanup()
