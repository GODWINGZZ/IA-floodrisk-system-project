
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    temp=inconsistent_typical_range_stations(build_station_list())
    x=[]
    for i in range(len(temp)):
        x.append(temp[i].name)
    x.sort()
    print(x)

    
 

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run() 
