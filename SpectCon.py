import seabreeze
import seabreeze.spectrometers as sb

devices = sb.list_devices()
print(devices)

spec = sb.Spectrometer(devices[0])
spec.integration_time_micros(12000)
spec.wavelengths()

#spec.intensities()
