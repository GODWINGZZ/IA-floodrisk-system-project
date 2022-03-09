import matplotlib
from .analyse import polyfit
import matplotlib.pyplot as plt
import numpy as np
def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates, levels, '.')
    x=matplotlib.dates.date2num(dates)
    x1=np.linspace(x[0],x[-1],30)
    plt.plot(x1,polyfit(x1-x1[0],levels,p))
    plt.axhline(y=15)
    plt.axhline(y=1)
    plt.show
    
