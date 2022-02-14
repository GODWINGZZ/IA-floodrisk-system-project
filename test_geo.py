from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_within_radius(): 
     stations=build_station_list()
     temp=stations_within_radius(stations,(52.2053, 0.1218),10) # use exmaple given in the docummnet
     assert len(temp)>0 #the length of the returned list should be bigger than zero
     assert len(temp)==11 # there should be exactly 11 stations in this range 

def test_rivers_with_station(): 
     ins=build_station_list()
     assert len(rivers_with_station(ins))>0 #the length of the returned list should be bigger than zero
     assert type(rivers_with_station(ins)) is set #the typr of the return should be a set 

def test_rivers_by_station_number(): #sam
     temp1=build_station_list()
     temp3=rivers_by_station_number(temp1,10)
     assert len(rivers_by_station_number(temp1,10))==10 #the length of the returned list should be 10
     assert type(rivers_by_station_number(temp1,10)) is list # type of returned list should be list
     assert temp3[0]>temp3[1] #the list in correct order, the number of statins of the previous instance should be bigger than the current one

def test_stations_by_river(): #sam
     temp2=build_station_list()
     assert len(stations_by_river(temp2))>0  #the length of the returned list should be bigger than zero
     assert type(stations_by_river(temp2)) is dict # the returned type shpuld dictionary


