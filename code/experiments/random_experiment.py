from code.algorithms import random_run
from code.helper import output
from code.imports import import_data
from code.visualisation import plot
import matplotlib.pyplot as plt
import copy
import csv

def experiment_random(map, iterations_experiment):
    # Amount of iterations
    max_iterations = iterations_experiment

    K_list = []
    for i in range(max_iterations):
        routes, K = random_run.random_algorithm(map)
        K_list.append(K)
        print(i)
    output.output(routes, K)

    # Plot histogram
    plt.title(f"Scores random algoritme (max: {int(max(K_list))})")
    plt.hist(K_list, bins=100, color="blue", ec="lightblue")
    plt.xlabel("Score")
    plt.ylabel("Hoeveelheid")
    plt.legend(["Random"])
    plt.show()

    print(max(K_list))

