"""function to return a list of (station, distance) tuples where distance is distance from p to station"""
from floodsystem.stationdata import build_station_list
import haversine
from floodsystem.geo import stations_by_distance


def run():
    stations = build_station_list
    distancefromcam = stations_by_distance(stations,(52.2053, 0.1218))
    closest10 = distancefromcam[:10]
    farthest10 = distancefromcam[-10:]
    print(closest10,farthest10)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()