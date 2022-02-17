
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

stations=build_station_list()
def run1():
 Num=len(rivers_with_station(build_station_list()))
 OrederedList=sorted(rivers_with_station(build_station_list()))
 x=OrederedList[0:9]
 print(Num,'stations','First 10 -',x)

def run2():
     temp1=stations_by_river(stations)
     print("Station by river:\n")
     for river in["River Aire","River Cam","River Thames"]:
         names=sorted(map(lambda stn: stn.name,temp1[river]))
         print(f" {river}:")
         print(f"   {names}\n")

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run1() 
    print()
    run2()


