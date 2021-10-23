# Open the .csv file, which contains data of potential targets from Table 4.1 (mod. website). This prints out the table in basic format, showing the RA/Dec of 
# potential targets (as well as the Galactic longitudes)

with open('gal_coords_targets.csv', mode='r') as galactic_coords:
    read_file = galactic_coords.read()
    print(read_file)
