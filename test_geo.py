from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_within_radius(): #morgan
     stations=build_station_list()
     temp=stations_within_radius(stations,(52.2053, 0.1218),10)       #stations 10km from centre of cambridge
     assert len(temp) == 11                                           #make sure there are the correct number in this range 

def test_rivers_with_station(): #sam
     ins=build_station_list()
     assert len(rivers_with_station(ins))>0                           #the length of the returned list should be bigger than zero
     assert type(rivers_with_station(ins)) is set                     #the type of the return should be a set 

def test_rivers_by_station_number(): #sam
     temp1=build_station_list()
     temp3=rivers_by_station_number(temp1,10)
     assert len(rivers_by_station_number(temp1,10))==10               #the length of the returned list should be 10
     assert type(rivers_by_station_number(temp1,10)) is list          #type of returned list should be list
     assert temp3[0]>temp3[1]                                         #the list in correct order, the number of stations of the previous instance should be bigger than the current one

def test_stations_by_river(): #sam
     temp2=build_station_list()
     assert len(stations_by_river(temp2))>0                           #the length of the returned list should be bigger than zero
     assert type(stations_by_river(temp2)) is dict                    #the returned type should dictionary

def test_stations_by_distance(): #morgan
     stations = build_station_list()
     temp4 = stations_by_distance(stations,(52.2053, 0.1218)) 
     temp5 = type(temp4[1])
     assert temp5 == tuple                                             #test to check that stations_by_distance is returning tuples
     assert temp4[0][1] < temp4[1][1]                                  #test to check list is sorted
