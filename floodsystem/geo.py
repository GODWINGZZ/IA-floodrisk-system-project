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
        distance=((centre[0]-x)^2+(centre[1]-y)^2)^0.5
        if distance<=r:
          Inrange[i]= stations[i]

    return Inrange 



def rivers_by_station_number(stations, N):
    Newlist=[]
    RequiredList=[]
    for i in range (len(stations)):
        temp=stations.river
        for j in range((len(Newlist))):
            if temp:=Newlist[j][0]:
                Newlist[j][1]+=1
            if temp!=Newlist[j] and (j:=len(Newlist)):
                Newlist[j][0]=temp
                Newlist[j][1]=1
    p = len(Newlist)
    while p > 0:
        for i in range(p - 1):
            if Newlist[i][1] > Newlist[i + 1][1]:
                Newlist[i + 1], Newlist[i] = Newlist[i], Newlist[i + 1]
            
        p = p - 1
    for  k in range(N):
        RequiredList[k]=Newlist[k]
    return RequiredList
        


