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
    k=matplotlib.dates.date2num(dates-shift)
    #num=43
    ##interval=math.ceil((len(dates)-1)/num)
    #dates_reduced=systematic_sample(dates[:-1],interval)
    #dates_reduced.append(dates[-1])
    #x1=np.array(
        ###list(map(lambda d:matplotlib.dates.date2num(d-shift),dates_reduced)))
        
    plt.plot(k,poly(k),label=f"Best fit, degree {p}",color="red")
    plt.legend


import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
from .stationdata import build_station_list
from datafetcher import fetch_measure_levels

stations = build_station_list

def plot_water_levels(station, dates, levels):
    
    plt.plot(t,level)
    
    plt.xlabel('date')
    plt.ylabel('water level/m')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()

    return