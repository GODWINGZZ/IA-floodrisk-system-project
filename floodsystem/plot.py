import matplotlib
from .analyse import polyfit
import matplotlib.pyplot as plt
import numpy as np
import math
def plot_water_level_with_fit(station,dates,levels,p):
    poly,shift=polyfit(dates,levels,p)
    k=[]
    g=[]
    for i in range(len(dates)):
      k.append(matplotlib.dates.date2num(dates[i]-shift))
      g.append(matplotlib.dates.date2num(dates[i]))

    plt.plot(g,levels,label="Original data",color="green")
        
    plt.plot(k,poly(k),label="Best fit, degree {p}",color="red")
    plt.title(station[0].name)
    plt.xlabel('Time')
    plt.ylabel('Water level')
    plt.legend
    plt.show()


import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
from .stationdata import build_station_list
from .datafetcher import fetch_measure_levels

stations = build_station_list

def plot_water_levels(station, dates, levels):
    
    plt.plot(dates,levels)
    
    plt.xlabel('date')
    plt.ylabel('water level/m')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()

    return