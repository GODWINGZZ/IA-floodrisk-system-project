from .stationdata import build_station_list
from .geo import rivers_by_station_number
def run():
 temp3=build_station_list()
 temp2=rivers_by_station_number(temp3, 9)
 print(temp2)
if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run() 