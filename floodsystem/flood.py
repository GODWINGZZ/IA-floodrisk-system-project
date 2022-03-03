from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
stations=build_station_list()

def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    Tuplelist=()
    for station in stations:
       temp1=station.relative_water_level()
       if temp1 > tol :
        Retuple=(station.name,station.latest_level)
        Tuplelist=Tuplelist+Retuple
    return Tuplelist

