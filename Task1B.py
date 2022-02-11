"""function to return a list of (station, distance) tuples where distance is distance from p to station"""
from floodsystem.stationdata import build_station_list
import haversine
from floodsystem.geo import stations_by_distance


def run():
    stations = build_station_list                                       #imports station data
    distancefromcam = stations_by_distance(stations,(52.2053, 0.1218))  #input coords p as centre of cambridge
    closest10 = distancefromcam[:10]                                    #closest 10 entries to cambridge
    farthest10 = distancefromcam[-10:]                                  #furthest 10 entries from cambridge
    print(closest10,farthest10)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()