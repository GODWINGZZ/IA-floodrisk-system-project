from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
def test_stations_within_radius():
     stations=build_station_list()
     temp=stations_within_radius(stations,(114.514,0.2233),10)
     assert len(temp)>0
     assert len(temp)< len(stations)