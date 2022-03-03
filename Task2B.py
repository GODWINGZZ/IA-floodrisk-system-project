from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
def run():
 stations=build_station_list()
 update_water_levels(stations)
 tuplelist=()
 stations_level_over_threshold(stations,0.8)
 for i in stations:
     Retuple=(i.name,i.latest_level)
     tuplelist=tuplelist+Retuple
 print(tuplelist)
     
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()


        