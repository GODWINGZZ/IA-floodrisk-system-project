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
