import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels,build_station_list
from floodsystem.plot import plot_water_level_with_fit
def run():
    stations=build_station_list()
    update_water_levels(stations)
    temp1=stations_highest_rel_level(stations,5)
    for i in temp1:
        

