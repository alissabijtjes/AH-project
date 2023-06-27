"""Experiment for hillclimber."""

import matplotlib.pyplot as plt

from code.algorithms import hillclimber
from code.helper import output
from code.visualisation import plot

def hillclimber_exp(map, iterations_experiment, begin, algoritme):
    """Preceeds experiment with hillclimber algorithm."""

    # Amount of iterations
    max_iterations = iterations_experiment

    # Start algorithms and the new route heuristics
    start_algorithm = begin
    route_heuristic = algoritme

    K_list = []
    iterations = []
    all_lists_values = []
    best_routes = 0
    
    # Generates start solution
    original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)
    
    # Runs hillclimber in range of iterations
    for i in range(max_iterations):
        if i % 1000 == 0:
            print(i)
        routes, current_k, var_min, values_list = hillclimber.hillclimber(map, route_heuristic, original_all_routes, copy_all_stations, var_min, current_k)
        
        # Update the output with routes of the current best k-score
        if i > 1:
            if current_k > max(K_list):
                output.output(routes, current_k)
                best_routes = routes
        
        K_list.append(current_k)
        iterations.append(i)
        all_lists_values.append(values_list)

        # Generates new start solution when k-values are the same for 10000 times
        if i > 10000:
            if K_list[-10000] == current_k:
                original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)
        
        # Generates new start solution when k-values are the same for 1000 times
        if i > 1000:
            if K_list[-1000] == current_k:
                original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)

    print(max(K_list))

    # Plot graph with iterations and k-scores
    plt.plot(iterations, K_list)
    plt.title(f"Scores hillclimber algoritme (max: {int(max(K_list))})")
    plt.xlabel("Iteraties")
    plt.ylabel("Score")

    # Plot extra line when using the random start algorithm
    if start_algorithm == "random":
        plt.axhline(y=4727, color="r")
        plt.legend(["Hillclimber", "Max random algoritme(4727)"])
    
    # Plot extra line when using a greedy start algorithm
    if start_algorithm == "greedy" or "greedy11" or "greedy12":
        plt.axhline(y=7549, color="r")
        plt.legend(["Hillclimber", "Max theoretische score(7549)"])
        plt.ylim(6950, 7600)

    plt.show()

    # Plot the routes
    plot.plot_routes(best_routes, copy_all_stations)