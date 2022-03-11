from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
def run():
 stations=build_station_list()
 update_water_levels(stations)
 list=[]
 for i in stations_level_over_threshold(stations,0.8):
     temp1=(i[0].name,i[1])
     list.append(temp1)
 for k in range(len(list)):
     print(list[k][0]+list[k][1])
    
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()


        