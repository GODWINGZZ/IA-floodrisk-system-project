from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels,build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from datetime import timedelta

def run():
    stations=build_station_list()
    update_water_levels(stations)
    temp1=stations_highest_rel_level(stations,5)
    for station in temp1:
       dt=2
       dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
       plot_water_level_with_fit(station,dates,levels,4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run() 

