from code.algorithms import random_run
from code.algorithms import hillclimber
from code.helper import output
from code.imports import import_data
from code.visualisation import plot
import matplotlib.pyplot as plt

def experiment_hillclimber(map):
    # ----------- Run hillclimber algorithm -------
    # Choose start solution for hillclimber ("greedy" or "random")
    start_algorithm = "random"
    # Choose heuristic for generating new route ("random", "greedy", "hillclimber") (when choosing greedy+greedy, see greedy algorithm)
    route_heuristic = "random"

    K_list = []
    iterations = []
    all_lists_values = []
    
    original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)
    
    for i in range(100000):
        if i % 1000 == 0:
            print(i)
        routes, current_k, var_min, values_list = hillclimber.hillclimber(map, route_heuristic, original_all_routes, copy_all_stations, var_min, current_k)
        K_list.append(current_k)
        iterations.append(i)
        all_lists_values.append(values_list)

        if i > 500:
            if K_list[-500] == current_k:
                original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)


    print(max(K_list))
    plt.plot(iterations, K_list)
    # plt.axhline(y=6963)
    plt.axhline(y=4727, color="r")
    plt.title(f"Scores hillclimber algoritme (max: {int(max(K_list))})")
    plt.xlabel("Iteraties")
    plt.ylabel("Score")
    plt.legend(["Hillclimber", "Max score random algoritme(4727)"])
    plt.show()