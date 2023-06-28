"""Experiment with random algorithm."""

import matplotlib.pyplot as plt

from code.algorithms import random_run
from code.helper import output

def experiment(map, iterations_experiment):
    """Preceeds experiment with random algorithm."""
    
    # Amount of iterations
    max_iterations = iterations_experiment

    K_list = []

    # Runs random algorithm in range of iterations
    for i in range(max_iterations):
        routes, K, all_stations = random_run.random_algorithm(map, max_routes=None)
        K_list.append(K)
        print(i)

    # Plot the routes
    output.output(routes, K)

    # Plot histogram with the scores
    plt.title(f"Scores random algoritme (max: {int(max(K_list))})")
    plt.hist(K_list, bins=100, color="blue", ec="lightblue")
    plt.xlabel("Score")
    plt.ylabel("Hoeveelheid")
    plt.legend(["Random"])
    plt.show()

    print(max(K_list))

