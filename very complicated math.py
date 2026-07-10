import math
# variables: lum, beamrate, bunches, atomsperbunch, Cfthickness, RFfreq, Cfareadensity, molnumber, Cfmolmass, target
Cfmolmass = 249.07
molnumber = 6.02214076e23
RFfreq = 18 * math.sqrt(2)
bunches = 1.8e7 * math.sqrt(2)
intensity = 500
charge = 7
e = 6.242e12
beamrate = (e * intensity) / charge
Cfarealdensity = 0.0005
target = (Cfarealdensity * molnumber) / Cfmolmass
lum = beamrate * target
atomsperbunch = beamrate / bunches

print(f"The beam rate is {beamrate}.")
print(f"The luminosity is {lum}.")
print(f"Each bunch contains {atomsperbunch} atoms.")