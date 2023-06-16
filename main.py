from code.algorithms import random_run
from code.imports import import_data
from code.visualisation import plot
from code.algorithms import greedy
from code.algorithms import hillclimber
import matplotlib.pyplot as plt

# Set which data to use ("Nationaal" or "Holland")
map = "Nationaal"

# Use random algorithm
# K_list = []
# for i in range(1000):
#     routes, K = random.random_algorithm(map)
#     K_list.append(K)
# random.output(routes, K)

# for station in routes[0].route:
#     print(station.name)

# print(routes[0].total_time)




# plt.hist(K_list, bins=50)
# plt.xlabel("K value")
# plt.ylabel("Amount")
# plt.show()

# print(max(K_list))
# print(min(K_list))

# Run greedy algoritm
# routes, K = greedy.complete_run(map)
# random_run.output(routes, K)


#K_list = []
#for i in range(1):
#    routes, K = greedy.complete_run(map)
#    K_list.append(K)
# random_run.output(routes, K)

# print(max(K_list))

K_list = []
new_all_routes, copy_all_stations, all_stations, var_min, current_k = hillclimber.initial_hillclimber(map)
for i in range(1000):
    routes, K = hillclimber.hillclimber(map, new_all_routes, copy_all_stations, all_stations, var_min, current_k)
#print("first k", current_k)
#print("best k", K)
random_run.output(new_all_routes, K)





# Plots all stations with connections
#all_stations = import_data.import_data(map)
# plot.plot_(routes, all_stations)

#for route in routes:
#    plot.live_plot(route, all_stations)