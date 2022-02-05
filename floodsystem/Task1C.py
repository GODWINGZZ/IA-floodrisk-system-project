from .geo import stations_within_radius
from .stationdata import build_station_list

Newlist=[]
temp1=build_station_list()
Newlist=stations_within_radius(temp1,(52.2053, 0.1218),10)
print(Newlist)
