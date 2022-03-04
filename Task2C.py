from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
 stations=build_station_list()
 list=stations_highest_rel_level(stations,10)
 print(list)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()