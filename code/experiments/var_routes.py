from code.algorithms import random_run
from code.algorithms import hillclimber
from code.helper import output
from code.visualisation import plot
import matplotlib.pyplot as plt

def experiment(map, iterations_experiment):
    # Amount of iterations
    max_iterations = iterations_experiment

    # Start algorithms and the new route heuristics
    start_algorithm = "random"

    heuristics = ["random", "hillclimber"]

    # Calculate for both heuristics
    for heuristic in heuristics:

        route_heuristic = heuristic
        best_k_values = []
        number_of_routes_list = []

        # Find best solution for every amount of routes
        for number_of_routes in range(1, 21):

            K_list = []
            
            # Initiate start state
            original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm, number_of_routes)
            
            # Run the hillclimber algorithm
            for i in range(max_iterations):

                # Print to see the program running
                if i % 1000 == 0:
                    print(f"routes:{number_of_routes} iteration: {i}")
                
                routes, current_k, var_min, values_list = hillclimber.hillclimber(map, route_heuristic, original_all_routes, copy_all_stations, var_min, current_k)

                K_list.append(current_k)

                # Get new start state if no better solutions are found after x tries
                if i > 100:
                    if K_list[-100] == current_k:
                        original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm, number_of_routes)

            best_k_values.append(max(K_list))
            number_of_routes_list.append(number_of_routes)

        # Plot the data
        plt.plot(number_of_routes_list, best_k_values)
    
    # Show the plot
    plt.title("Maximale score na hillclimber met verschillend aantal trajecten")
    plt.xlabel("Aantal trajecten")
    plt.ylabel("Score")
    plt.legend(["Random", "Greedy"])
    plt.xticks(range(0,21))
    plt.show()