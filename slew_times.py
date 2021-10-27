from astropy import constants as const
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

#<------------------------------- SLEW FROM PARK TO NEP -------------------------------->

# First create SkyCoords for Parking Position of ARROW and NEP. Az/Alt of Park is (180, 80) deg.
park_radec = SkyCoord('22h21m00s',  '+42d04m00s')  # Approx. RA/Dec coords of Park position on 4/11/21 at ~1930 
nep_radec = SkyCoord('18h00m00s', '+66d33m00s')

# Use .separation() method to measure angular distance between them
ang_distance = park_radec.separation(nep_radec)

# Save in variable whose units are in degrees, instead of d:m:s
ang_dist_deg = ang_distance.deg*u.deg

# Check
print(ang_dist_deg)

print('The angular distance of Park and NEP against the sky is', ang_distance)

# ARROW travels approx. 1 degree every 6 seconds
travel_speed = 1/6*(u.deg/u.second)

# Check
print(travel_speed)

slew_time = ang_dist_deg / travel_speed

# Convert to minutes (equal to 4.2 mins)
print(slew_time.to('min')). 
