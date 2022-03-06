import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels,build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
import datetime
def run():
    stations=build_station_list()
    update_water_levels(stations)
    temp1=stations_highest_rel_level(stations,5)
    for station in temp1:
       dt=5
       dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=dt))
       plot_water_level_with_fit(station,dates,levels,4)

