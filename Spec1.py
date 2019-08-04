import numpy as np
import matplotlib.pyplot as plt
data = np.arange(-3,3,1)

print(data)

A = 2
w = 2

phi = np.pi

plt.plot(data,A*np.cos(w*data+phi))
plt.show()
