from import_data import stations, Connecties
import matplotlib.pyplot as plt

for station in stations:
    plt.plot(station.coordinates[0], station.coordinates[1], 'ro')

plt.show()