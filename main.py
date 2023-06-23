from code.algorithms import random_run
from code.imports import import_data
from code.visualisation import plot
from code.algorithms import greedy
from code.algorithms import hillclimber
from code.helper import output
import matplotlib.pyplot as plt
from resultaten.write_results import write_results, plot_results

import subprocess
import time
from experiments.random_experiment import experiment_random
# import statisti

# Set which data to use ("Nationaal" or "Holland")
map = "Holland"

# ------------- Run random algorithm -----------
# K_list = []
# for i in range(10000):
#     routes, K = random_run.random_algorithm(map)
#     K_list.append(K)
# output.output(routes, K)

# for station in routes[0].route:
#     print(station.name)

# print(routes[0].total_time)



# plt.hist(K_list, bins=50)
# plt.xlabel("K value")
# plt.ylabel("Amount")
# plt.show()

# print(max(K_list))
# print(min(K_list))

# ----------- Run greedy algoritm -----------
# routes, K = greedy.complete_run(map)
# output.output(routes, K)


# K_list = []
# for i in range(1):
#    routes, K = greedy.complete_run(map)
#    K_list.append(K)
# output.output(routes, K)

# print(max(K_list))
# print(K_list)


# ----------- Run hillclimber algorithm -------
# Choose start solution for hillclimber ("greedy" or "random")
start_algorithm = "greedy"
# Choose heuristic for generating new route ("random", "greedy", "hillclimber") (when choosing greedy+greedy, see greedy algorithm)
route_heuristic = "hillclimber"

K_list = []
all_lists_values = []
original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)
for i in range(10000):
    routes, current_k, var_min, values_list = hillclimber.hillclimber(map, route_heuristic, original_all_routes, copy_all_stations, var_min, current_k)
    K_list.append(current_k)
    all_lists_values.append(values_list)

# print(K_list)
print(min(K_list))
print(max(K_list))
write_results(all_lists_values)
# plot_results(all_lists_values)
output.output(routes, current_k)





# Plots all stations with connections
all_stations = import_data.import_data(map)
# plot.plot_routes(routes, all_stations)
# plot.plot(all_stations)

# for route in routes:
#   plot.live_plot(route, all_stations)


#-------------Experiments------------

experiment_random(map)

