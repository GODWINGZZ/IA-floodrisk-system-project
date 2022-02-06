# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa


def stations_within_radius(stations, centre, r):
    """This function is used for returning a list of station within a certain radius"""
    Inrange=[]
    for i in range ( len(stations)):
        x=stations[i].coord[0]
        y=stations[i].coord[1]
        distance=((centre[0]-x)**2+(centre[1]-y)**2)**0.5
        if distance<=r:
          Inrange.append(stations[i])

    return Inrange 

def rivers_with_station(stations):
    """
    Function that returns a set of names of rivers that have an associated monitoring station.
    """
    List_of_rivers = set()
    for s in stations:
        List_of_rivers.add(s.river)
    return List_of_rivers

def stations_by_river(stations):
    """
    Function that returns a dictionary mapping river names to a list of MonitoringStation objects
    """
    Set_of_stations = {}
    for s in stations:
        river = s.river
        if river in Set_of_stations:
            Set_of_stations[river].append(s)
        else:
            Set_of_stations[river] = [s]
    return Set_of_stations


def rivers_by_station_number(stations, N):
    """
    This function is used to determines the N rivers with the greatest number of monitoring stations
    """

    list = sorted_by_key([(key, len(value))for key, value in stations_by_river(stations).items()],1,reverse=True)
    Newlist = list[:N]
    for i in range(N, len(list)):
        if list[i][1] < list[N - 1][1]:
            break
        else:
            Newlist.append(list[i])

    return Newlist

        


