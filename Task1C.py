from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

#Newlist=[]
#temp1=build_station_list()
#Newlist=stations_within_radius(temp1,(52.2053, 0.1218),10)
#print(Newlist)
#print(len(Newlist))

#N.B. commented out sam's broken code, morgan's attempt below:

def run():
    stations = build_station_list                                                   #import list of stations
    stationsinrange = stations_within_radius(stations,(52.2053, 0.1218),10)         #list of stations within 10km of cambridge
    print(stationsinrange)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()