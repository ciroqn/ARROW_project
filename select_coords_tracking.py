import pandas as pd

from astropy import constants as c
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

# Date and time of observation. The time can be changed so the changing Alt/Az can be monitored.

dt_string = '2021-11-04T19:20:00'   # <---- Time can be changed 

# Use Time() constructor using necessary formats (including 'isot')

obs_time = Time(dt_string, format='isot', scale='utc')

#  EarthLocation() for ARROW

arrow = EarthLocation(lat=52.024444*u.deg, lon=-0.706388*u.deg, height=114*u.m)

# 
