import sqlite3
import matplotlib.pyplot as plt
import time
import psutil

conn = sqlite3.connect("temp.db")
c = conn.cursor()

q = "select * from temph"
x = c.execute(q)
t = x.fetchall();

plt.rcParams['animation.html'] = 'jshtml'

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i=0
x, y = [], []

while True:
    x.append(i)
    y.append(t[i])
    ax.plot(x, y, color = 'b')
    plt.xlabel('Count')
    plt.ylabel('Temperature')
    plt.title('Weather Report')
    fig.canvas.draw()
    ax.set_xlim(left=max(0, i-50), right=i+50)
    time.sleep(3)
    i+=1
    
plt.close()

c.close()
conn.close()