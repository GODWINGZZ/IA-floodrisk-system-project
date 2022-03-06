from floodsystem.analyse import polyfit
import matplotlib.pyplot as plt
import numpy as np
def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates, levels, '.')
    x1=np.linspace(dates[0],dates[-1],30)
    plt.plot(x1,polyfit(x1-x1[0]))
    plt.show
    
