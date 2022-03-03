from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
def stations_level_over_threshold(stations, tol):
  return  sorted_by_key([(station,station.relative_water_level())
    for station in stations if station.relative_water_level()!=None and station.relative_water_level()>tol],
    1,
    reverse=True)

