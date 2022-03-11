from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():
    ins=build_station_list()
    assert type(stations_level_over_threshold(ins,0.8)) is tuple
