import Adafruit_DHT
import time
import matplotlib.pyplot as plt
import psutil
import datetime

DHT_PIN = 4
DHT_SENSOR = Adafruit_DHT.DHT11

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    e = datetime.datetime.now()
    loc = "JHB"
    timed = "%s:%s:%s" % (e.hour, e.minute, e.second)
    dated = datetime.date.today()

    if humidity is not None and temperature is not None:

        print ("Location", loc, "Time ", timed, "Date", dated, "Temp", temperature,"C Humidy", humidity,"%")

        import sqlite3
        conn = sqlite3.connect("temp.db")
        c = conn.cursor()

        q = """INSERT INTO iotTable (loc, timed, dated, temperature, humidity) VALUES (?,?,?,?,?)"""
        c.execute(q, (loc, timed, dated, temperature, humidity))
        conn.commit()
    else:
        print("Sensor Failure");
    time.sleep(3);

    conn.close()
