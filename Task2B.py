from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
stations=build_station_list()
def run():
 print(stations_level_over_threshold(stations,0.8))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()