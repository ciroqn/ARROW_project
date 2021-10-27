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
