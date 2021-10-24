# Open the .csv file, which contains data of potential targets from Table 4.1 (mod. website). This prints out the table in basic format, showing the RA/Dec of 
# potential targets (as well as the Galactic longitudes)

# <------------------------------------------------------ SECTION 1: ACCESSING RA/DEC DATA FROM TABLE 4.1 ------------------------------------------------>

with open('gal_coords_targets.csv', mode='r') as galactic_coords:
    read_file = galactic_coords.read()
    print(read_file)
    
# Import pandas, since we will need this for the 'read_csv' method, and this printout is much clearer than above

import pandas as pd
import numpy as np

# Creating a Pandas DataFrame (a more powerful array), using comma-separated variable file, and reading file *from* header (or, row) 1:

df = pd.read_csv('gal_coords_targets.csv', sep=',', header=1)

# Now that we have the DataFrame, the data needs to be sorted into an array (in this case, an array for the RA values AND an array for the Dec values). 
# When we have these two arrays, the 'zip()' function can be used to join the respective coordinates into one array - and then we should have sets of Ra/Dec coords:

with open('gal_coords_targets.csv', mode='r') as gal_coords:
    df = pd.read_csv(gal_coords, sep=',', header=1)
    col_ra = df['RA']                                     # Accessing data in column called 'RA'
    ra_array = col_ra.array                               # Converting column RA data into array
    clean_ra_array = []
    for coord in  ra_array:
        clean_ra_array.append(coord.strip())              # append data to empty list, clean_ra_array, and stripping the '\n'
    print(clean_ra_array)

with open('gal_coords_targets.csv', mode='r') as gal_coords:
    df = pd.read_csv(gal_coords, sep=',', header=1)
    col_dec = df['DEC']                                   # Accessing data in column 'DEC'
    dec_array = col_dec.array                             # Turning column DEC data into array (for some reason, this didn't need 'stripping')
    print(dec_array)
    
# Join two array to give a set of coords in array

radec_targets = zip(clean_ra_array, dec_array)             # Joining two array together to give respective RA/Dec coords
print(radec_targets)                                       # The zip() function creates an object, so we need to convert it

# 'Unzip' zip object and convert it to list
radec_sets = list(radec_targets)
print(radec_sets)

# <------------------------------------------- SECTION 2: RA/DEC TO ALT/AZ - CHECKING IF COORDS IN RANGE ------------------------------------------->


# Now for the second part, which is using 'astropy' to select our location, observation time, and conver the RA/Dec values to Alt/Az. By doing this, we can see
# what will be visible in the sky at a particular observation at a particular time (in this case ARROW in Milton Keynes, starting at 19:20:00 on 4/11/21

# Import astropy packages

from astropy import constants as c
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
                 
# We need SkyCoord() constructors for *each* RA/Dec set in 'radec_sets' in order to convert this to Alt/Az. First, an empty list is established, to which
# we append each SkyCoord of RA/Dec coord sets.

skycoord_gal_list = []
for coord in radec_sets:
    skycoord_gal_list.append(SkyCoord(coord[0], coord[1])).  # Where coord[0] gives the RA, and coord[1] gives Dec values
print(skycoord_gal_list)

# Now we have the SkyCoord() constructors for each RA/Dec value in 'radec_sets', the Alt/Az constructor now needs to be put in place. It takes two arguments:
# the date and time strings (in a specific format - according to 'isot') and the location of observation (ARROW). They are defined below:

# <------------------------------------- INPUT TIME FOR 't_str' TO SEE EFFECT ON ALT/AZ COORDS ---------------------------------------->

# First set up the time and date strings for our location (ARROW in Milton Keynes).

t_str = '19:20:00'

dt_string = '2021-11-04T' + t_str

# Use Time() constructor using necessary formats (including 'isot')

obs_time = Time(dt_string, format='isot', scale='utc')

# Now for setting up ARROW's location using EarthLocation() constructor (we need three values: latitude, longitude and height)

arrow = EarthLocation(lat=52.024444*u.deg, lon=-0.706388*u.deg, height=114*u.m)

# Now that we have established the Time() (date and time we observe) and EarthLocation() (for ARROW) constructors, the Alt/Az can be established:

obs_altaz_frame = AltAz(obstime=obs_time, location=arrow)

# Now to convert this to the AltAz coords using our frame defined by the AltAz constructor:

altaz_coords = []
for radec_coords in skycoord_gal_list:
    altaz_coords.append(radec_coords.transform_to(obs_altaz_frame))
print(altaz_coords)

# The above printout shows a list of Alt/Az coordinates

print('\n')

# Determine visibility according to the angles that are restricted due to ARROW's hardware limitations:

count = 0
for altaz_set in altaz_coords:
    if int(altaz_set.az.degree) > 20 and int(altaz_set.az.degree) < 340 and int(altaz_set.alt.degree) > 20 and int(altaz_set.alt.degree) < 80:
        print(f'The Alt/Az coordinates, with Azimuth {altaz_set.az.deg:.3f} and Altitude {altaz_set.alt.deg:.3f}, are in range, and are VISIBLE at', t_str, '; RA/Dec: (', round(skycoord_gal_list[count].ra.deg, 4), ',', round(skycoord_gal_list[count].dec.deg, 4),')')
    else:
        print(f'The Alt/Az coordinates, with Azimuth {altaz_set.az.deg:.3f} and Altitude {altaz_set.alt.deg:.3f}, are in NOT in range at', t_str, '; RA/Dec: (', round(skycoord_gal_list[count].ra.deg, 4), ',', round(skycoord_gal_list[count].dec.deg, 4),')')
    count += 1
    
# Alternatively, for a different RA/DEC format in the print() statements in the conditional statement above, we can access the data directly from the .csv file that was 
# defined earlier in the file. So instead of the RA/DEC in degrees, they are in h:m:s and d:m:s, respecitvely:

count = 0
for altaz_set in altaz_coords:
    if int(altaz_set.az.degree) > 20 and int(altaz_set.az.degree) < 340 and int(altaz_set.alt.degree) > 20 and int(altaz_set.alt.degree) < 80:
        print(f'The Alt/Az coordinates, with Azimuth {altaz_set.az.deg:.3f} and Altitude {altaz_set.alt.deg:.3f}, are in range, and are VISIBLE at', t_str, '; RA/Dec: (', df['RA'][count], ',', df['DEC'][count],')')
    else:
        print(f'The Alt/Az coordinates, with Azimuth {altaz_set.az.deg:.3f} and Altitude {altaz_set.alt.deg:.3f}, are in NOT in range at', t_str, '; RA/Dec: (', df['RA'][count], ',', df['DEC'][count],')')
    count += 1
