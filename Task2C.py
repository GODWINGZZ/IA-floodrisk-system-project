from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
stations=build_station_list()
print(stations_highest_rel_level(stations,10))

#if __name__ == "__main__":
    #print("*** Task 2C: CUED Part IA Flood Warning System ***")
    #run()