from astropy import constants as const
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

#<------------------------------- SLEW FROM PARK TO NEP -------------------------------->

# ----> NOT NECESSARY FOR SESSION (SINCE RFI PICKED UP EARLY IN OTHER SESSIONS NEAR NEP)

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
print(slew_time.to('min'))

#<------------------------------ SLEW TIME FROM NEP TO SPECIFIED LONGITUDE-------------------------------->

# ----> NOT NECESSARY NOW THAT NEP SCANS HAVE MOVED TIME-SLOT

# Slew time from NEP to first longitude location (in this case l = 50)

lon_50_radec = SkyCoord('19h23m00s',  '+15d08m00s')
nep_radec = SkyCoord('18h00m00s', '+66d33m00s')

ang_distance1 = nep_radec.separation(lon_50_radec)

ang_dist_deg1 = ang_distance1.deg*u.deg

print(ang_dist_deg1)

print('The angular distance of longitude, 50, and NEP against the sky is', ang_distance)

slew_time1 = ang_dist_deg1 / travel_speed

# Equal to 5.3 mins
print(slew_time1.to('min'))

#<---------------------------------- SLEW TIME FROM PARK TO L = 50 --------------------------------------->

park_radec_1920 = SkyCoord('22h14m00s', '+40d29m00s') # approx RA/Dec for park at ~1920

ang_dist2 = park_radec_1920.separation(lon_50_radec)

print(ang_dist2)

slew_time2 = ang_dist2 / travel_speed

# Prints ~ 4.5 mins
print('The approx. time from Park to l = 50 is', slew_time2.to('min'))

#<---------------------------------- SLEW TIME L = 70 TO NEP --------------------------------------->

lon_70_radec = SkyCoord('20h07m00s', '+32d26m00s')

ang_dist3 = lon_70_radec.separation(nep_radec)

slew_time3 = ang_dist3 / travel_speed

# Prints ~ 3.9 mins
print('The approx. time from longitude 70 to NEP is ', slew_time3.to('min'))
