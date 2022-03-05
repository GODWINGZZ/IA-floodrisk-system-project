import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    poly,d0 = np.polyfit(x, levels, p)
    return poly,d0