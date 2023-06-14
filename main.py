from code.algorithms import random
from code.imports import import_data
from code.visualisation import plot
import matplotlib.pyplot as plt

# Set which data to use ("Nationaal" or "Holland")
map = "Holland"

# Use random algorithm
K_list = []
for i in range(1000):
    routes, K = random.random_algorithm(map)
    K_list.append(K)
random.output(routes, K)

# for station in routes[0].route:
#     print(station.name)

# print(routes[0].total_time)




# plt.hist(K_list, bins=50)
# plt.xlabel("K value")
# plt.ylabel("Amount")
# plt.show()

# print(max(K_list))
# print(min(K_list))

# Plots all stations with connections
all_stations = import_data.import_data(map)
plot.plot_(routes, all_stations)