import Adafruit_DHT
import time
import datetime

DHT_PIN = 4
DHT_SENSOR = Adafruit_DHT.DHT11

while True:
    e = datetime.datetime.now()
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    loc = "JHB"
    timed = "%s:%s:%s" % (e.hour, e.minute, e.second)
    dated = datetime.date.today()

    if humidity is not None and temperature is not None:
        print ("Location", loc, "Time ", timed, "Date", dated, "Temp", temperature,"C Humidy", humidity,"%")
    else:
        print("Sensor Failure");
    time.sleep(5);
