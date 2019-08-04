import seabreeze
import seabreeze.spectrometers as sb

import numpy as np
import matplotlib.pyplot as plt

devices = sb.list_devices()
print(devices)

spec = sb.Spectrometer(devices[0])
spec.integration_time_micros(12000)
spec.wavelengths()
spec.intensities()
time = np.arange(0,3840,1)
dataw = spec.wavelengths()
datai = spec.intensities()
plt.plot(time,dataw)
plt.show()
