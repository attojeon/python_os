import psutil as ps
import time
import datetime
import numpy as np
import random
import matplotlib.pyplot as plt
import threading


def worker():
    datas_x = []
    datas_y = []

    fig = plt.gcf()
    fig.show()
    fig.canvas.draw()

    dt = datetime.datetime.now()
    for x in range(60):
        datas_x.append( dt )
        datas_y.append(0.0)
        dt += datetime.timedelta(seconds=0.1)

    while (True):
        now = datetime.datetime.now()
        hour = bytes([now.hour])
        minute = bytes([now.minute])
        cpu_p = (ps.cpu_percent())
        mem_p = (ps.virtual_memory().percent)
        disk_p = (ps.disk_usage('/').percent)
        #disk_s = ps.disk_usage('/')
        #print("date:{}, cpu:{}, mem:{}, disk:{}, disk_s:{}".format( str(now), cpu_p, mem_p, disk_p, disk_s))
        datas_y.append(cpu_p)
        if( len(datas_y) > 60 ):
            datas_y.remove(datas_y[0])

        #plt.hist(cpu_datas)
        plt.clf()
        plt.plot_date(datas_x, datas_y)
        fig.canvas
        fig.canvas.draw()

        time.sleep(0.5)


if __name__ == "__main__":
    thread = threading.Thread( target = worker)
    thread.start()
    