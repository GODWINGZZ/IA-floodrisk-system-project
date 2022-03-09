import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x, levels, p)
    poly=np.poly1d(p_coeff)
    return poly
   