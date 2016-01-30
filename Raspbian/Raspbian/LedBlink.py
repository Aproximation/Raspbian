import RPi.GPIO as GPIO
import time
import pdb

pinNum = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum, GPIO.OUT)

def ChangeState():
    if (GPIO.input(pinNum)):
        GPIO.output(pinNum, False)   
    else:
        GPIO.output(pinNum, True)   

while(True):
    ChangeState()
    time.sleep(1)


