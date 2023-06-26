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
    route_heuristic = "hillclimber"

    for i in range(2):
        if i == 0:
            route_heuristic = "random"

        K_value = []
        routes_ = []

        for max_routes in range(1,21):
            K_list = []
            iterations = []
            all_lists_values = []
            
            original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm, max_routes)
            
            for i in range(10000):
                routes, current_k, var_min, values_list = hillclimber.hillclimber(map, route_heuristic, original_all_routes, copy_all_stations, var_min, current_k)
                K_list.append(current_k)
                iterations.append(i)
                all_lists_values.append(values_list)

                if i > 500:
                    if K_list[-500] == current_k:
                        original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm, max_routes)
        
            print(max(K_list), max_routes)
            K_value.append(max(K_list))
            routes_.append(max_routes)

            # print(K_list)
            # print(min(K_list))
            # print(max(K_list))
            #write_results(all_lists_values)
            # plt.plot(iterations, K_list)
            # plt.show()

        #all_stations = import_data.import_data(map)
        #plot.plot_routes(routes, all_stations)
        plt.plot(routes_, K_value)

    plt.title("Maximale score na hillclimber met verschillend aantal trajecten")
    plt.xticks(range(0,21))
    plt.xlabel("Aantal trajecten")
    plt.ylabel("Score")
    plt.legend(["random", "greedy"])
    plt.show()