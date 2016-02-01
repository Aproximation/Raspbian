import RPi.GPIO as GPIO
import time
import datetime

pinMS = 23
pinLed = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinMS, GPIO.IN)
GPIO.setup(pinLed, GPIO.OUT)

try:
    print "(CTRL+C to exit)"
    print "Ready"
    while True:
        if GPIO.input(pinMS):
            timeNow = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
            print "Motion detected! {}".format(timeNow)
            GPIO.output(pinLed, True)  
        else:
            GPIO.output(pinLed, False)  
        time.sleep(1)
except KeyboardInterrupt:
    print "Stopped"
    GPIO.cleanup()


