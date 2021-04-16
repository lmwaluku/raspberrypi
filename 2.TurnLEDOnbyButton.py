import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sleepTime = .1

#GPIO Pin of the component
lightPin = 18
buttonPin = 23

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#print ('On')

try:
    while True:
        GPIO.output(lightPin, not GPIO.input(buttonPin))
        #print ('Off')
        sleep(.1)
finally:
    GPIO.output(lightPin, False)
    GPIO.cleanup()