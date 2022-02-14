# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa
from haversine import haversine
from .stationdata import build_station_list

def stations_within_radius(stations, centre, r):
    """This function is used for returning a list of station within a certain radius"""
    Inrange=[]
    for i in range ( len(stations)):
        x=stations[i].coord[0]  #get the  x coordinate of the object
        y=stations[i].coord[1]  #get the y cooedinate of the object
        distance=((centre[0]-x)**2+(centre[1]-y)**2)**0.5 #calculate the distance between the given point and the centre 
        if distance<r:
          Inrange.append(stations[i].name) #add it into the list 
        else:
          break

    return Inrange 

def rivers_with_station(stations):
    """
    Function that returns a set of names of rivers that have an associated monitoring station.
    """
    List_of_rivers =set() #initialate a new empty set
    for s in stations:   #loop in side the station list 
        List_of_rivers.add(s.river) #add suitable elements into the set 
    return List_of_rivers 

def stations_by_river(stations):
    """
    Function that returns a dictionary mapping river names to a list of MonitoringStation objects
    """
    Set_of_stations = {} #create an empty set 
    for s in stations:
        river = s.river # assign to a temp for futher comparision 
        if river in Set_of_stations:
            Set_of_stations[river].append(s) #if found the river with the same name then append it to the list
        else:
            Set_of_stations[river] = [s] # if it is a new river, creat a new field for it 
    return Set_of_stations


def rivers_by_station_number(stations, N):
    """
    This function is used to determines the N rivers with the greatest number of monitoring stations
    """

    list = sorted_by_key([(key, len(value))for key, value in stations_by_river(stations).items()],1,reverse=True) #sorted the returned dictionay by key from the above function
    Newlist = list[:N] #take the first N elments for the list 
    for i in range(N, len(list)):
        if list[i][1] < list[N - 1][1]:#compare the the number of stations each river has
            break
        else:
            Newlist.append(list[i])

    return Newlist

def stations_by_distance(stations, p):          #function to return sorted list of stations by distance from input coords p
    tuplelist = []                              #creates empty list
    stations = build_station_list()             #imports list of stations
    for i in stations:                          #loop that calculates distance of each station from p
        stationdistance = haversine(i.coord,p)
        temp = (i.name,stationdistance)
        tuplelist.append(temp)                  #adds (station,distance) tuple to the end of list
    sortedlist = sorted_by_key(tuplelist,1)     #sorts list entries by distance
    return sortedlist       


