import matplotlib
import numpy as np
from datetime import  timedelta


def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    d0=x[0]
    p_coeff = np.polyfit(x-d0, levels, p)
    poly=np.poly1d(p_coeff)
    return poly,timedelta(days=d0)
   