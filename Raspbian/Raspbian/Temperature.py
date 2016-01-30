import RPi.GPIO as GPIO
import time

deviceId = "0115508d25ff"
devicePath = "/sys/bus/w1/devices/28-{}/w1_slave".format(deviceId)

def Measure():
    file = open(devicePath)
    text = file.read()
    file.close()
    data = text.split("\n")[1].split(" ")[9]
    temperature = float(data[2:]) 
    temperature = temperature / 1000
    print temperature

while(True):
    Measure()
    time.sleep(10)

