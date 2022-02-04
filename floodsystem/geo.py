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