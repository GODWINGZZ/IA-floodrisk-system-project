from xmlrpc.client import DateTime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import datetime, timedelta, date
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analyse import polyfit
import matplotlib.pyplot as plt
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)

    for station in stations:
        towns = []
        towns.append(station.town)
        if station.town is None:
            towns.append("no_name")
    
        for town in towns:
            dt=1
            dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))

            if (len(levels) == 0):      #you're welcome
                poly = [0]
            else:
                poly,shift=polyfit(dates,levels,4)    
                polyderivative = np.polyder(poly)

            if poly == 0 or station.latest_level is None or station.typical_range is None: #test for missing data
                print("no_data")
    
            elif polyderivative(1) > 0:

                if station.latest_level > station.typical_range[1]:
                    print(station.name,"severe risk")
    
                elif station.latest_level < station.typical_range[1]:
                    print(station.name,"moderate risk")

            elif polyderivative(1) < 0:

                if station.latest_level > station.typical_range[1]:
                    print(station.name,"moderate risk")
    
                elif station.latest_level < station.typical_range[1]:
                    print(station.name,"low risk")

            elif polyderivative(1) == 0:

                if station.latest_level > station.typical_range[1]:
                    print(station.name,"high risk")
    
                elif station.latest_level < station.typical_range[1]:
                    print(station.name,"moderate risk")     


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
