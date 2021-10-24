import pandas as pd

from astropy import constants as c
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

# Date and time of observation. The time can be changed so the changing Alt/Az can be monitored.

time_string = '19:20:00'

dt_string = '2021-11-04T' + time_string   # <---- Time can be changed 

# Use Time() constructor using necessary formats (including 'isot')

obs_time = Time(dt_string, format='isot', scale='utc')

#  EarthLocation() for ARROW

arrow = EarthLocation(lat=52.024444*u.deg, lon=-0.706388*u.deg, height=114*u.m)

# Random RA/Dec (potential target) in SkyCoord() constructor

potential_target = SkyCoord('19h04m00s', '06d17m00s')

# Create AltAz observation frame

altaz_obsframe = AltAz(obstime=obs_time, location=arrow)

# Convert potential target to AltAz frame

altaz_coords = potential_target.transform_to(altaz_obsframe)

# Determine if Alt/Az coords are out of range of ARROW's dish with the time of potential observation attached:

if int(altaz_coords.az.degree) > 20 and int(altaz_coords.az.degree) < 340 and int(altaz_coords.alt.degree) > 20 and int(altaz_coords.alt.degree) < 80:
   print(f'The Alt/Az coordinates, with Azimuth {altaz_coords.az.deg:.3f} and Altitude {altaz_coords.alt.deg:.3f}, are in range, and are VISIBLE at', time_string)
else:
   print(f'The Alt/Az coordinates, with Azimuth {altaz_coords.az.deg:.3f} and Altitude {altaz_coords.alt.deg:.3f}, are in NOT in range at', time_string)
