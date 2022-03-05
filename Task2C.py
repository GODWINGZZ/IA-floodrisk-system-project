from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels

def run():
 stations=build_station_list()
 update_water_levels(stations)
 list=[]
 for i in stations_highest_rel_level(stations,10):
     temp1=(i[0].name,i[1])
     list.append(temp1)
 print(list)
 

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()