import Adafruit_DHT
import time
import matplotlib.pyplot as plt
import psutil

DHT_PIN = 4
DHT_SENSOR = Adafruit_DHT.DHT11

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        
        print ("Temp {0:0.1f} C Humidy {1:0.1f} %".format(temperature, humidity))
        
        import sqlite3
        conn = sqlite3.connect("temp.db")
        c = conn.cursor()

        q = """INSERT INTO temph (temp, humid) VALUES (?,?)"""
        c.execute(q, (temperature, humidity))
        conn.commit()             
    else: 
        print("Sensor Failure");
    time.sleep(3);
    
    #c.close()
    conn.close()