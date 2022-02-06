
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    station=build_station_list()
    print(inconsistent_typical_range_stations(station))
 

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run() 
