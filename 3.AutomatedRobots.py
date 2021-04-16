import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO Pin of the component
greenPin = 18
orangePin = 23
redPin = 24

GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(orangePin, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT)

for x in range(0, 7):
    GPIO.output(greenPin, True)
    time.sleep(.5)
    GPIO.output(greenPin, False)
    
    GPIO.output(orangePin, True)
    time.sleep(.5)
    GPIO.output(orangePin, False)
    
    GPIO.output(redPin, True)
    time.sleep(.5)
    GPIO.output(redPin, False)
    
GPIO.cleanup()
