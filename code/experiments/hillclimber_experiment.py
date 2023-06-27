from code.algorithms import random_run
from code.algorithms import hillclimber
from code.helper import output
from code.visualisation import plot
import matplotlib.pyplot as plt

def experiment_hillclimber(map, iterations_experiment, begin, algoritme):
    # Amount of iterations
    max_iterations = iterations_experiment

    # Start algorithms and the new route heuristics
    start_algorithm = begin
    route_heuristic = algoritme

    K_list = []
    iterations = []
    all_lists_values = []
    best_routes = 0
    
    original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)
    
    for i in range(max_iterations):
        if i % 1000 == 0:
            print(i)
        routes, current_k, var_min, values_list = hillclimber.hillclimber(map, route_heuristic, original_all_routes, copy_all_stations, var_min, current_k)
        
        if i > 1:
            if current_k > max(K_list):
                output.output(routes, current_k)
                best_routes = routes
            
        K_list.append(current_k)
        iterations.append(i)
        all_lists_values.append(values_list)

        if i > 10000:
            if K_list[-10000] == current_k:
                original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)

        if i > 1000:
            if K_list[-1000] == current_k:
                original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)

    print(max(K_list))
    plt.plot(iterations, K_list)
    plt.title(f"Scores hillclimber algoritme (max: {int(max(K_list))})")
    plt.xlabel("Iteraties")
    plt.ylabel("Score")
    if start_algorithm == "random":
        plt.axhline(y=4727, color="r")
        plt.legend(["Hillclimber", "Max random algoritme(4727)"])
    if start_algorithm == "greedy" or "greedy11" or "greedy12":
        plt.axhline(y=7549, color="r")
        plt.legend(["Hillclimber", "Max theoretische score(7549)"])
        plt.ylim(6950, 7600)
    plt.show()
    plot.plot_routes(best_routes, copy_all_stations)