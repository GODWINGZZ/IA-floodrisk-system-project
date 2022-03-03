from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
def run():
 stations=build_station_list()
 update_water_levels(stations)
 tuplelist=()
 for i in stations_level_over_threshold(stations,0.8):
     tuplelist=tuplelist+(i.name,i.latest_level)
 print(tuplelist)
     
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()


        