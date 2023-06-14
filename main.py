from code.algorithms import random
from code.imports import import_data
from code.visualisation import plot

map = "Nationaal"

routes, K = random.random_algorithm(map)
random.output(routes, K)

all_stations = import_data.import_data(map)
plot.plot(all_stations)