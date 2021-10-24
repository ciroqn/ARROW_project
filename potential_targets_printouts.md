# These are the terminal printouts from the [potential_targets.py](https://github.com/ciroqn/ARROW_project/blob/main/potential_targets.py) to give a visual check (it can also be done in Jupyter Notebook)

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
