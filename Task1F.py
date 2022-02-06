
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
 y=inconsistent_typical_range_stations(build_station_list())
 x=sorted(y)
 print(x)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run() 
