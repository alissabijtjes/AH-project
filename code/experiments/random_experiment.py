from code.algorithms import random_run
from code.helper import output
from code.imports import import_data
from code.visualisation import plot
import matplotlib.pyplot as plt
import copy
import csv

def experiment_random(map):
    # ------------- Run random algorithm -----------
    K_list = []
    for i in range(1000):
        routes, K = random_run.random_algorithm(map)
        K_list.append(K)
    output.output(routes, K)

    plt.hist(K_list, bins=50)
    plt.xlabel("K value")
    plt.ylabel("Amount")
    plt.show()

    print(max(K_list))
    print(min(K_list))

    all_stations = import_data.import_data(map)
    plot.plot_routes(routes, all_stations)
    plot.plot(all_stations)

    for route in routes:
      plot.live_plot(route, all_stations)
