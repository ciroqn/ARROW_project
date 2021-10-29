# These are the terminal printouts from the [potential_targets.py](https://github.com/ciroqn/ARROW_project/blob/main/potential_targets.py) to give a visual check (it can also be done in Jupyter Notebook)

## To see if a coordinate is visible at a particular time string, see code in [this file](https://github.com/ciroqn/ARROW_project/blob/main/select_coords_tracking.py) where one can input a time and a potential target (i.e. input RA and Dec values)

```py
import pandas as pd
import numpy as np

from astropy import constants as c
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

# Open the .csv file, which contains data of potential targets from Table 4.1 (mod. website)

with open('gal_coords_targets.csv', mode='r') as galactic_coords:
    read_file = galactic_coords.read()
    print(read_file)
```

```
Table of Galactic Longitudes (Along Galactic plane at b = 0 deg) and Corresponding RA/Dec,,
l,RA,DEC
20,18h27m00s,-11d29m00s
30,18h46m00s,-02d36m00s
40,19h04m00s,+06d17m00s
50,19h23m00s,+15d08m00s
60,19h43m00s,+23d53m00s
70,20h07m00s,+32d26m00s
80,20h35m00s,+40d39m00s
90,21h12m00s,+48d19m00s
100,22h00m00s,+55d02m00s
110,23h04m00s,+60d09m00s
120,00h25m00s,+62d43m00s
130,01h52m00s,+62d02m00s
140,03h07m00s,+58d17m00s
150,04h04m00s,+52d25m00s
160,04h46m00s,+45d14m00s
170,05h19m00s,+37d18m00s
180,05h45m00s,+28d56m00s
190,06h07m00s,+20d17m00s
200,06h27m00s,+11d29m00s
210,06h46m00s,+02d36m00s
220,07h04m00s,-06d17m00s
230,07h23m00s,-15d08m00s
240,07h43m00s,-23d53m00s
```

```py
with open('gal_coords_targets.csv', mode='r') as gal_coords:
    df = pd.read_csv(gal_coords, sep=',', header=1)
    col_ra = df['RA']
    ra_array = col_ra.array
    clean_ra_array = []
    for coord in  ra_array:
        clean_ra_array.append(coord.strip())
    print(clean_ra_array)

with open('gal_coords_targets.csv', mode='r') as gal_coords:
    df = pd.read_csv(gal_coords, sep=',', header=1)
    col_dec = df['DEC']
    dec_array = col_dec.array
    print(dec_array)
    
# Join two array to give a set of coords in array

radec_targets = zip(clean_ra_array, dec_array)
print(radec_targets)

# 'Unzip' zip object and convert it to list
radec_sets = list(radec_targets)
print(radec_sets)

```

```
----> The first array shows the 'stripped' RA values (accessed through df['RA'])

['18h27m00s', '18h46m00s', '19h04m00s', '19h23m00s', '19h43m00s', '20h07m00s', '20h35m00s', '21h12m00s', '22h00m00s', '23h04m00s', '00h25m00s', '01h52m00s', '03h07m00s', '04h04m00s', '04h46m00s', '05h19m00s', '05h45m00s', '06h07m00s', '06h27m00s', '06h46m00s', '07h04m00s', '07h23m00s', '07h43m00s']
<PandasArray>

----> The second array shows the Dec values (accessed through df['DEC'])

['-11d29m00s', '-02d36m00s', '+06d17m00s', '+15d08m00s', '+23d53m00s',
 '+32d26m00s', '+40d39m00s', '+48d19m00s', '+55d02m00s', '+60d09m00s',
 '+62d43m00s', '+62d02m00s', '+58d17m00s', '+52d25m00s', '+45d14m00s',
 '+37d18m00s', '+28d56m00s', '+20d17m00s', '+11d29m00s', '+02d36m00s',
 '-06d17m00s', '-15d08m00s', '-23d53m00s']
Length: 23, dtype: object

----> This is the zip object, whose action combined the RA and Dec values, respectively. It needs to be converted to a list.

<zip object at 0x7f93fa955f50>

----> Converting to a list gives:

[('18h27m00s', '-11d29m00s'), ('18h46m00s', '-02d36m00s'), ('19h04m00s', '+06d17m00s'), ('19h23m00s', '+15d08m00s'), ('19h43m00s', '+23d53m00s'), ('20h07m00s', '+32d26m00s'), ('20h35m00s', '+40d39m00s'), ('21h12m00s', '+48d19m00s'), ('22h00m00s', '+55d02m00s'), ('23h04m00s', '+60d09m00s'), ('00h25m00s', '+62d43m00s'), ('01h52m00s', '+62d02m00s'), ('03h07m00s', '+58d17m00s'), ('04h04m00s', '+52d25m00s'), ('04h46m00s', '+45d14m00s'), ('05h19m00s', '+37d18m00s'), ('05h45m00s', '+28d56m00s'), ('06h07m00s', '+20d17m00s'), ('06h27m00s', '+11d29m00s'), ('06h46m00s', '+02d36m00s'), ('07h04m00s', '-06d17m00s'), ('07h23m00s', '-15d08m00s'), ('07h43m00s', '-23d53m00s')]
```

```py
# Create a list of SkyCoord() constructors for each RA/Dec set in 'radec_sets':

skycoord_gal_list = []
for coord in radec_sets:
    skycoord_gal_list.append(SkyCoord(coord[0], coord[1]))
print(skycoord_gal_list)
```

```
----> The 'skycoord_gal_list' list, containing the SkyCoord constructors for each RA/Dec set. This is now ripe for conversion to Alt/Az, once we have
----> established the date/time string using Time() and the location of our observation, ARROW, using EarthLocation(), and then combining this information
----> in AltAz() constuctor

[<SkyCoord (ICRS): (ra, dec) in deg
    (276.75, -11.48333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (281.5, -2.6)>, <SkyCoord (ICRS): (ra, dec) in deg
    (286., 6.28333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (290.75, 15.13333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (295.75, 23.88333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (301.75, 32.43333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (308.75, 40.65)>, <SkyCoord (ICRS): (ra, dec) in deg
    (318., 48.31666667)>, <SkyCoord (ICRS): (ra, dec) in deg
    (330., 55.03333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (346., 60.15)>, <SkyCoord (ICRS): (ra, dec) in deg
    (6.25, 62.71666667)>, <SkyCoord (ICRS): (ra, dec) in deg
    (28., 62.03333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (46.75, 58.28333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (61., 52.41666667)>, <SkyCoord (ICRS): (ra, dec) in deg
    (71.5, 45.23333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (79.75, 37.3)>, <SkyCoord (ICRS): (ra, dec) in deg
    (86.25, 28.93333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (91.75, 20.28333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (96.75, 11.48333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (101.5, 2.6)>, <SkyCoord (ICRS): (ra, dec) in deg
    (106., -6.28333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (110.75, -15.13333333)>, <SkyCoord (ICRS): (ra, dec) in deg
    (115.75, -23.88333333)>]
```

```py
# First set up the time and date strings for our location (PIRATE in Tenerife, in this case).

dt_string = '2021-11-04T19:20:00'

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
```

```
----> Looping through the 'skycoord_gal_list' list and converted each to Alt/Az. The print() gives the following rather dense list. We only need to worry about the
----> (az, alt) at the end of each SkyCoord AltAz object:

[<SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (236.11963956, 10.14257307)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (236.72464187, 20.18083286)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (237.58257433, 30.10642749)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (238.54068378, 40.07952559)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (240.02841708, 49.96048071)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (241.9163068, 59.9526151)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (245.82136396, 69.76810783)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (255.84491781, 79.55198047)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (328.7659132, 86.30166479)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (35.44207671, 79.17783973)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (45.34363721, 69.53544517)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (49.01636313, 59.5954018)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (51.00791096, 49.65026941)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (52.31452592, 39.72287307)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (53.36704884, 29.81070944)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (54.09243708, 19.77499071)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (54.80809584, 9.82411735)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (55.49918881, -0.13875604)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (56.11290284, -10.14483019)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (56.7174801, -20.18148703)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (57.57465713, -30.10551547)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (58.53154962, -40.07710665)>, <SkyCoord (AltAz: obstime=2021-11-04T19:20:00.000, location=(3932588.11129261, -48486.53479912, 5004567.24279243) m, pressure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0.0, obswl=1.0 micron): (az, alt) in deg
    (60.01722164, -49.95672415)>]
```

```py
# Finally, we loop through each AltAz coord set and determine if it's visible at our observation time and date (and location) using 
# 'f-strings' for neat formatting. Note the int() to convert the string to an integer in the 'if' statement:

count = 0
for altaz_set in altaz_coords:
    if int(altaz_set.az.degree) > 20 and int(altaz_set.az.degree) < 340 and int(altaz_set.alt.degree) > 20 and int(altaz_set.alt.degree) < 80:
        print(f'The Alt/Az coordinates, with Azimuth {altaz_set.az.deg:.3f} and Altitude {altaz_set.alt.deg:.3f}, are in range, and are VISIBLE at', t_str, '; RA/Dec: (', round(skycoord_gal_list[count].ra.deg, 4), ',', round(skycoord_gal_list[count].dec.deg, 4),')')
    else:
        print(f'The Alt/Az coordinates, with Azimuth {altaz_set.az.deg:.3f} and Altitude {altaz_set.alt.deg:.3f}, are in NOT in range at', t_str, '; RA/Dec: (', round(skycoord_gal_list[count].ra.deg, 4), ',', round(skycoord_gal_list[count].dec.deg, 4),')')
    count += 1 
```

```
----> From the loop above, we should get the following statements:

The Alt/Az coordinates, with Azimuth 229.746 and Altitude 13.751, are NOT in range at 19:30:00 ; RA/Dec: ( 276.75 , -11.4833 ); (l = 20 )
The Alt/Az coordinates, with Azimuth 229.836 and Altitude 23.806, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 281.5 , -2.6 ); (l = 30 )
The Alt/Az coordinates, with Azimuth 230.123 and Altitude 33.758, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 286.0 , 6.2833 ); (l = 40 )
The Alt/Az coordinates, with Azimuth 230.383 and Altitude 43.760, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 290.75 , 15.1333 ); (l = 50 )
The Alt/Az coordinates, with Azimuth 230.972 and Altitude 53.689, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 295.75 , 23.8833 ); (l = 60 )
The Alt/Az coordinates, with Azimuth 231.478 and Altitude 63.735, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 301.75 , 32.4333 ); (l = 70 )
The Alt/Az coordinates, with Azimuth 233.058 and Altitude 73.669, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 308.75 , 40.65 ); (l = 80 )
The Alt/Az coordinates, with Azimuth 237.939 and Altitude 83.734, are NOT in range at 19:30:00 ; RA/Dec: ( 318.0 , 48.3167 ); (l = 90 )
The Alt/Az coordinates, with Azimuth 35.679 and Altitude 86.084, are NOT in range at 19:30:00 ; RA/Dec: ( 330.0 , 55.0333 ); (l = 100 )
The Alt/Az coordinates, with Azimuth 45.478 and Altitude 76.215, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 346.0 , 60.15 ); (l = 110 )
The Alt/Az coordinates, with Azimuth 47.250 and Altitude 66.259, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 6.25 , 62.7167 ); (l = 120 )
The Alt/Az coordinates, with Azimuth 48.000 and Altitude 56.206, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 28.0 , 62.0333 ); (l = 130 )
The Alt/Az coordinates, with Azimuth 48.451 and Altitude 46.199, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 46.75 , 58.2833 ); (l = 140 )
The Alt/Az coordinates, with Azimuth 48.763 and Altitude 36.232, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 61.0 , 52.4167 ); (l = 150 )
The Alt/Az coordinates, with Azimuth 49.081 and Altitude 26.286, are in range, and are VISIBLE at 19:30:00 ; RA/Dec: ( 71.5 , 45.2333 ); (l = 160 )
The Alt/Az coordinates, with Azimuth 49.209 and Altitude 16.229, are NOT in range at 19:30:00 ; RA/Dec: ( 79.75 , 37.3 ); (l = 170 )
The Alt/Az coordinates, with Azimuth 49.405 and Altitude 6.257, are NOT in range at 19:30:00 ; RA/Dec: ( 86.25 , 28.9333 ); (l = 180 )
The Alt/Az coordinates, with Azimuth 49.611 and Altitude -3.728, are NOT in range at 19:30:00 ; RA/Dec: ( 91.75 , 20.2833 ); (l = 190 )
The Alt/Az coordinates, with Azimuth 49.740 and Altitude -13.752, are NOT in range at 19:30:00 ; RA/Dec: ( 96.75 , 11.4833 ); (l = 200 )
The Alt/Az coordinates, with Azimuth 49.830 and Altitude -23.805, are NOT in range at 19:30:00 ; RA/Dec: ( 101.5 , 2.6 ); (l = 210 )
The Alt/Az coordinates, with Azimuth 50.116 and Altitude -33.756, are NOT in range at 19:30:00 ; RA/Dec: ( 106.0 , -6.2833 ); (l = 220 )
The Alt/Az coordinates, with Azimuth 50.375 and Altitude -43.756, are NOT in range at 19:30:00 ; RA/Dec: ( 110.75 , -15.1333 ); (l = 230 )
The Alt/Az coordinates, with Azimuth 50.963 and Altitude -53.683, are NOT in range at 19:30:00 ; RA/Dec: ( 115.75 , -23.8833 ); (l = 240 )
```

----> Note that each Alt/Az coord above is listed in the same order as the RA/Dec values at the top of this file (which, in turn, was 'read' from [this file](https://github.com/ciroqn/ARROW_project/blob/main/gal_coords_targets.csv)).

----> Alternatively, instead of expressing the RA/DEC in degrees, they could be expressed at `h:m:s` and `d:m:s` for the RA and Dec, respectively. In this case, the conidtional statement will look like this:

```py
count = 0
for altaz_set in altaz_coords:
    if int(altaz_set.az.degree) > 20 and int(altaz_set.az.degree) < 340 and int(altaz_set.alt.degree) > 20 and int(altaz_set.alt.degree) < 80:
        print(f'The Alt/Az coordinates, with Azimuth {altaz_set.az.deg:.3f} and Altitude {altaz_set.alt.deg:.3f}, are in range, and are VISIBLE at', t_str, '; RA/Dec: (', df['RA'][count], ',', df['DEC'][count],')')
    else:
        print(f'The Alt/Az coordinates, with Azimuth {altaz_set.az.deg:.3f} and Altitude {altaz_set.alt.deg:.3f}, are in NOT in range at', t_str, '; RA/Dec: (', df['RA'][count], ',', df['DEC'][count],')')
    count += 1
```
```
----> Where the DataFrame, df, was defined earlier when 'reading' the .csv file. Thus, the RA/DEC format as expressed in the file will be shown:

The Alt/Az coordinates, with Azimuth 254.517 and Altitude -2.526, are NOT in range at 21:30:00 ; RA/Dec: ( 18h27m00s , -11d29m00s ); (l = 20 )
The Alt/Az coordinates, with Azimuth 256.108 and Altitude 7.403, are NOT in range at 21:30:00 ; RA/Dec: ( 18h46m00s , -02d36m00s ); (l = 30 )
The Alt/Az coordinates, with Azimuth 257.913 and Altitude 17.202, are NOT in range at 21:30:00 ; RA/Dec: ( 19h04m00s , +06d17m00s ); (l = 40 )
The Alt/Az coordinates, with Azimuth 259.848 and Altitude 27.044, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 19h23m00s , +15d08m00s ); (l = 50 )
The Alt/Az coordinates, with Azimuth 262.305 and Altitude 36.760, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 19h43m00s , +23d53m00s ); (l = 60 )
The Alt/Az coordinates, with Azimuth 265.230 and Altitude 46.572, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 20h07m00s , +32d26m00s ); (l = 70 )
The Alt/Az coordinates, with Azimuth 269.655 and Altitude 56.135, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 20h35m00s , +40d39m00s ); (l = 80 )
The Alt/Az coordinates, with Azimuth 276.741 and Altitude 65.647, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 21h12m00s , +48d19m00s ); (l = 90 )
The Alt/Az coordinates, with Azimuth 291.751 and Altitude 74.301, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 22h00m00s , +55d02m00s ); (l = 100 )
The Alt/Az coordinates, with Azimuth 329.926 and Altitude 80.057, are NOT in range at 21:30:00 ; RA/Dec: ( 23h04m00s , +60d09m00s ); (l = 110 )
The Alt/Az coordinates, with Azimuth 22.843 and Altitude 77.886, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 00h25m00s , +62d43m00s ); (l = 120 )
The Alt/Az coordinates, with Azimuth 46.956 and Altitude 70.129, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 01h52m00s , +62d02m00s ); (l = 130 )
The Alt/Az coordinates, with Azimuth 57.117 and Altitude 61.009, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 03h07m00s , +58d17m00s ); (l = 140 )
The Alt/Az coordinates, with Azimuth 62.627 and Altitude 51.511, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 04h04m00s , +52d25m00s ); (l = 150 )
The Alt/Az coordinates, with Azimuth 66.292 and Altitude 41.881, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 04h46m00s , +45d14m00s ); (l = 160 )
The Alt/Az coordinates, with Azimuth 68.855 and Altitude 32.033, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 05h19m00s , +37d18m00s ); (l = 170 )
The Alt/Az coordinates, with Azimuth 70.985 and Altitude 22.240, are in range, and are VISIBLE at 21:30:00 ; RA/Dec: ( 05h45m00s , +28d56m00s ); (l = 180 )
The Alt/Az coordinates, with Azimuth 72.853 and Altitude 12.413, are NOT in range at 21:30:00 ; RA/Dec: ( 06h07m00s , +20d17m00s ); (l = 190 )
The Alt/Az coordinates, with Azimuth 74.512 and Altitude 2.524, are NOT in range at 21:30:00 ; RA/Dec: ( 06h27m00s , +11d29m00s ); (l = 200 )
The Alt/Az coordinates, with Azimuth 76.102 and Altitude -7.403, are NOT in range at 21:30:00 ; RA/Dec: ( 06h46m00s , +02d36m00s ); (l = 210 )
The Alt/Az coordinates, with Azimuth 77.907 and Altitude -17.200, are NOT in range at 21:30:00 ; RA/Dec: ( 07h04m00s , -06d17m00s ); (l = 220 )
The Alt/Az coordinates, with Azimuth 79.841 and Altitude -27.041, are NOT in range at 21:30:00 ; RA/Dec: ( 07h23m00s , -15d08m00s ); (l = 230 )
The Alt/Az coordinates, with Azimuth 82.297 and Altitude -36.756, are NOT in range at 21:30:00 ; RA/Dec: ( 07h43m00s , -23d53m00s ); (l = 240 )
```
