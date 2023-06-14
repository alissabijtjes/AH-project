from code.algorithms import random
from code.imports import import_data
from code.visualisation import plot

# Set which data to use ("Nationaal" or "Holland")
map = "Nationaal"

# Use random algorithm
routes, K = random.random_algorithm(map)
random.output(routes, K)

# Plots all stations with connections
all_stations = import_data.import_data(map)
plot.plot(all_stations)