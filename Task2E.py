from xmlrpc.client import DateTime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import datetime, timedelta, date

def run():
    stations = build_station_list()
    update_water_levels(stations)
    topfive = stations_highest_rel_level(stations, 5)
    names = []
    for tuple in topfive:
        names.append(tuple[0])
    namelist = []
    for station in names:
        namelist.append(station.name)
    
    print(namelist)

    for i in stations:
        if i.name in namelist:
            
            dt = 10
            dates, levels = fetch_measure_levels(i.measure_id, dt=timedelta(days=dt))

            for date, level in zip(dates, levels):
                print(date, level)

            print(plot_water_levels(i, dates, levels))
    

    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()