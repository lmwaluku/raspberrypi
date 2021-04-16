#import RPi.GPIO as GPIO
import Adafruit_DHT
import time
#import sys

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#GPIO Pin of the component
DHT_PIN = 4
DHT_SENSOR = Adafruit_DHT.DHT11

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
    #if temperature is not None:
        print ("Temp {0:0.1f} C Humidy {1:0.1f} %".format(temperature, humidity))
    else:
        print("Sensor Failure");
    time.sleep(5);