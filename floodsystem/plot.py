import matplotlib
from .analyse import polyfit
import matplotlib.pyplot as plt
import numpy as np
import math
def plot_water_level_with_fit(station,dates,levels,p):
    plt.rc("lines",marker=".",linestyle="None")
    #plot_water_levels_no_show(station,dates,levels)
    matplotlib.pyplot.rcdefaults()
    poly,shift=polyfit(dates,levels,p)
    k=[]
    for i in range(len(dates)):
      k.append(matplotlib.dates.date2num(dates[i]-shift))
    
        
    plt.plot(k,poly(k),label=f"Best fit, degree {p}",color="red")
    plt.legend


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