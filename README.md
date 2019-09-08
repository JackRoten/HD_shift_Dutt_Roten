# HD_shift_Dutt_Roten

## Experimental Overview
Created by Baskar Dutt and Jack Roten for UCSB Physics lab course.
UCSB 128AL lab on Hydrogen and Deuterium Isotope Shifts

The Balmer Series energy spectrum of an atom, or the wavelenght of most intensly emmited visible spectrum photons, is related to the mass of the nucleus. 

We observe the Balmer series (Electron transitions of n = 3 -> 2, 4 -> 2 , ... , 8 -> 2 ) of Dueterium and Hydrogen. This demonstrates the relationship between the mass of the nucleas and the energy spectrum. We capture light from the hydrogen and dueterium gas tube, which travels through a narrow, adjustable, slit. the light is then difracted into its spectrum due to a difraction grating, which is then sent through a secondary narrow slit, to be captured by a Photo Multiplier Tube (PMT) and aquired by a data logging program.



![expDiagram.png](https://github.com/JackRoten/HD_shift_Dutt_Roten/blob/JackBranch/expDiagram.png)

Through tunning the angle of the diffraction graiting we are able to capture different wavelengths of light and notice the subtle shift in wavelength that comes from Dueterium's single nucleon heavier nucleus

For each balmer series transition we notice two peaks, one tall, higher intensity peak and another shorter, lower intensity, peak. The former is Dueterium with it electron being bound closer to the heavier nucleus, shifting the wavelength emitted as well as increasing the likelyhood of being exited; in turn a higher number of photon emmisions.

![410_Peak_shift_4.png](https://github.com/JackRoten/HD_shift_Dutt_Roten/blob/JackBranch/410_Peak_shift_4.png)

The figure above depics the signal in volts as a function of time with a sweeping speed of 5 angstoms per second. The cyan line represents the raw data and the red line is the transformed filtered data, which allows us to easily find the peaks.

We measured several shifts in Angstrom(Ang) and randomly selected peaks with low percent error

Transition | Measured shift(Ang)  | Theoretical shift(Ang) | % Error |
|-------|---------|--------|------|
| 3 -> 2 | 1.766 +/- 0.019   | 1.787  | 1.2 |
|4 -> 2 | 1.301 +/- 0.007   | 1.324 | 1.7 |
|5 -> 2 | 1.186 +/- 0.012  | 1.182 | 0.3 |
|6 -> 2  | 1.103 +/- 0.009& | 1.059   | 2.9 |
|7 -> 2  | 1.098 +/- 0.004 | 1.080  | 1.7 |
|8 -> 2  | 1.062 +/- 0.011&  | 1.059  | 0.3 |

## Data Analysis
Our experimental aparatus allowed us to aquire decent data. Bu even this data wasn't safe from noise. as we sweeped over shorter wavelenghs (higher frequency and transition energy) they probabilty of an electron being driven into this state and emitting a phton was lower, causing the signal amplitude to be shorter. And along with given line noise and other potential background interference, peak signal in the 7 -> 2, and 8 -> 2 transitions were almost indistinguishable from the line noise. 

Our main issue of lessening noise in our data is solved with the digital data smoohing algorithm devised by Savitzky and Golay. Savitzky-Golay filters is a least-squares polynomial smoothing essentialy digital low pass filters and were originally developed for smoohing data from chemical specrum analyzers... somewhate related to this experiment...

Least-squares polynomial smoothing is not compuationally complex and is carried out by convolution of data points with properly choosen sets of integers. A great overview and mathematical explaination can be found in the paper: [What is a Savitzky-Golay Filter?](https://inst.cs.berkeley.edu/~ee123/fa12/docs/SGFilter.pdf)

For our purposes we used the [SciPy Cookbook Savitzky_Golay Filter](https://scipy-cookbook.readthedocs.io/items/SavitzkyGolay.html) for our smoothing filter and [PeakUtils](https://peakutils.readthedocs.io/en/latest/tutorial_a.html) to find our peaks.

