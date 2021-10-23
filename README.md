# Using the ARROW Radio Telescope to map the Galaxy

## Aim of ARROW Project
ARROW is a radio telescope, so it can, luckily, detect signals whatever the weather (but, of course, any vibrations from the surrounding environment could have an impact). ARROW specifically **detects 21 cm radiowaves** from the abundance of hydrogen gas in the outer arms of our galaxy and the wider Galactic plane. By utilising the Doppler shift of these emissions, one can determine the speeds of the clouds of hydrogen gas. In turn, a rotation curve can be constructed from this (note that the velocity of this gas may have components in three directions). From this, the mass can be estimated.

The rotational speed of the Galaxy will be plotted as a function of distance from the centre. Since the view is restricted in the UK, archival data from the inner Galactic place will also be used for a fuller graph of the rotational speed.

## About ARROW itself

ARROW is located at the Open University's campus in Milton Keynes, and is functions as a steerable 3-metre telescope dish. It has a detector that is capable of detecting/receiving 21 cm radio emissions.

The dish is operated via the ARROW OpenScience Observatory.

## Planning Observing Session

Targets will need to be picked that are not in the *exclusion zone*, which is the zone through which the dish cannot rotate due to hardware limitations. The exclusion zone is in `Alt/Az` coordinates:
  - 20 deg < Azimuth < 340 deg
  - 20 deg < Altitude < 80 deg

The dish takes roughly 5-6 seconds to rotate by 1 degree (so ~ 10 degrees / minute). Also, it takes around 15 seconds to run a quic scan (and 100s for a full scane), and this would be done, typically, only to confirm that the dish has been turned away from an unkown source of radio interference. Interference shows up as sharp peaks on the graph, and if these sharp peaks are close to the H1 line, then it will be necessary to shift the dish 1-2 degrees to the right or left and make a quick scan to investiage the interference.

## Operation of ARROW

The two 'status' panes (lower left) of the UI is shows the dish orientation ("Drive") and the weather. The first pane either has a status of "Slewing", menaing the dish is on the move, or "Stopped". When the dish has stopped, the RA/Dec coordinates should be changing only slowly, and the Alt/Az coordinates should remain constant. And when a target is being tracked, only the Alt/Az coordinates should change, and the RA/Dec should remain relatively constant.

Of course, the weather needs to be fairly calm, otherwise tracking may be slightly off (and the wind may contribute to the disturbance). Thus, the weather conditions the experimenter needs to monitor are wind speed and temperature. Winds over 30 km/h (~8.3 m/s) should be noted, since at these speeds, the dish starts to wobble, and there will be additional noise when scanning. Similarly, if the temperature is below -5 degrees Celsius, then the grease in the mount bearings may not lubricate properly, and so tracking may be lost.

### Data/Graph Pane

The graph is the signal intensity (y-axis) vs Doppler shifts (x-axis), which is labelled about the HI rest frequency (0.0).

The graph will show two tabs, "Current" and "Previous", for the current and previous scans. This will be useful for visual comparisons between two adjacent coordinates or for detecting any radio interference/noise. The 'download' button will save the data as a `.csv` file. The dowload is available after the next scan is started.  

When the operator locks onto a target (i.e. tracks a target, once the coordinates have been successuflly located), then the "Full Scan" will be pressed gived a trace from L-to-R. The *x-axis*, as already noted, representes increasing frequences, and the higher the frequencies (shorter wavelengths) correspond to negative radial velocities; that is, the motion of the source is towards the observer). The rest frequency of atomic hydrogen (0.0 on graph) has been subtracted from the graph, and so negative frequencies correspond to redshifted hydrogen gas clouds, and positive ones are blueshifted.

**Each broad peak on the graph represents a large mass of atomic hydrogen moving independently of each other (as we go along the x-axis, there may be multiple broad peaks - so these will be at different frequencies, and thus have differing radial velocities).**

There is also a slight upward trend of the spectra, which will be discussed later.

## Scanning and Radio Frequency Interference (RFI)
