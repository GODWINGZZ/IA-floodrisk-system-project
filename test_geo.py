from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_within_radius(): #sam
     stations=build_station_list()
     temp=stations_within_radius(stations,(52.2053, 0.1218),10)
     assert len(temp)>0
     assert len(temp)==11

def test_rivers_with_station(): #sam
     ins=build_station_list()
     assert len(rivers_with_station(ins))>0
     assert type(rivers_with_station(ins)) is set 

def test_rivers_by_station_number(): #sam
     temp1=build_station_list()
     temp3=rivers_by_station_number(temp1,10)
     assert len(rivers_by_station_number(temp1,10))==10 
     assert type(rivers_by_station_number(temp1,10)) is list
     assert temp3[0]>temp3[1]

def test_stations_by_river(): #sam
     temp2=build_station_list()
     assert len(stations_by_river(temp2))>0
     assert type(stations_by_river(temp2)) is dict


