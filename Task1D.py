
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run():
 Num=len(rivers_with_station(build_station_list()))
 OrederedList=sorted(rivers_with_station(build_station_list()))
 x=OrederedList[0:9]
 print(Num,'stations','First 10 -',x)
if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run() 


