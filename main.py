from code.algorithms import random_run
from code.imports import import_data
from code.visualisation import plot
from code.algorithms import greedy
from code.algorithms import hillclimber
import matplotlib.pyplot as plt
from resultaten.write_results import write_results, plot_results
# import statisti

# Set which data to use ("Nationaal" or "Holland")
map = "Nationaal"

# ------------- Run random algorithm -----------
# K_list = []
# for i in range(10000):
#     routes, K = random_run.random_algorithm(map)
#     K_list.append(K)
# random_run.output(routes, K)

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
# random_run.output(routes, K)


K_list = []
for i in range(1):
   routes, K = greedy.complete_run(map)
   K_list.append(K)
random_run.output(routes, K)

# print(max(K_list))
# print(K_list)


# ----------- Run hillclimber algorithm -------
# K_list = []
# new_all_routes, copy_all_stations, all_stations, var_min, current_k = hillclimber.initial_hillclimber(map)
# for i in range(1000):
#     routes, current_k, var_min = hillclimber.hillclimber(map, new_all_routes, copy_all_stations, all_stations, var_min, current_k)
#     K_list.append(current_k)
# print(K_list)
# print(min(K_list))
# print(max(K_list))
# random_run.output(routes, current_k)
K_list = []
all_lists_values = []
original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map)
for i in range(5):
    routes, current_k, var_min, values_list = hillclimber.hillclimber(map, original_all_routes, copy_all_stations, var_min, current_k)
    K_list.append(current_k)
    all_lists_values.append(values_list)

# print(K_list)
# print(min(K_list))
# print(max(K_list))
# write_results(all_lists_values)
#plot_results(all_lists_values)
# random_run.output(routes, current_k)





# Plots all stations with connections
all_stations = import_data.import_data(map)
plot.plot_routes(routes, all_stations)
# plot.plot(all_stations)

# for route in routes:
#   plot.live_plot(route, all_stations)
