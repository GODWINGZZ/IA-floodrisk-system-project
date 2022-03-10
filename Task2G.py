from xmlrpc.client import DateTime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import datetime, timedelta, date

stations = build_station_list

for station in stations:
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))

for date, level in zip(dates, levels):
    print(date, level)

