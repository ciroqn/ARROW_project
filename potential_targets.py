# Open the .csv file, which contains data of potential targets from Table 4.1 (mod. website). This prints out the table in basic format, showing the RA/Dec of 
# potential targets (as well as the Galactic longitudes)

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


# Now for the second part, which is using 'astropy' to select our location, observation time, and conver the RA/Dec values to Alt/Az. By doing this, we can see
# what will be visible in the sky at a particular observation at a particular time (in this case ARROW in Milton Keynes, starting at 19:20:00 on 4/11/21

# Import astropy packages

from astropy import constants as c
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
                 

