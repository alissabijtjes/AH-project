import matplotlib.pyplot as plt

from code.algorithms import random_run
from code.imports import import_data
from code.visualisation import plot
from code.algorithms import greedy
from code.algorithms import hillclimber
from code.helper import output
from code.helper.write_results import write_results
from code.experiments.random_experiment import experiment_random
from code.experiments.hillclimber_experiment import experiment_hillclimber

# Set which data to use ("Nationaal" or "Holland")
map = "Nationaal"


# ----------- Run random algorithm ----------- #

# # Set how many runs you want
# iterations = 1000

# # list for the score
# K_values = []

# # Run algormitme x times
# for i in range(iterations):
#     routes, K, all_stations = random_run.random_algorithm(map)

#     # Save best run
#     if i != 0:
#         if K > max(K_values):
#             output.output(routes, K)
#             best_all_stations = all_stations
#             best_routes = routes

#     K_values.append(K)

# # Print best score
# print(f"Best score: {max(K_values):.2f}")

# # Plot the data
# plt.hist(K_values, bins=50, ec="lightblue")
# plt.title("Random algoritme")
# plt.xlabel("Score")
# plt.ylabel("Aantal")
# plt.show()

# # Visualisation
# plot.plot_routes(best_routes, best_all_stations)

# ----------- End random algoritme ---------- #



# ----------- Run greedy algoritm ----------- #

# Run algoritm (Only needs to runs once because gives the same solution every time)
# routes, K, all_stations = greedy.complete_run(map)

# # Saves the routes
# output.output(routes, K)

# # Prints score
# print(f"Score: {K:.2f}")

# # Visualisation
# plot.plot_routes(routes, all_stations)

# ------------ End greedy algoritm ---------- #


# ----------- Run hillclimber algorithm ----- #

# Choose amount of iterations
iterations = 100

# Choose start solution for hillclimber ("greedy" or "random")
start_algorithm = "random"

# Choose heuristic for generating new route ("random", "hillclimber")
route_heuristic = "random"

# Initiate lists
K_values = []
runs = []
data = []

# Run an algoritm once to get a start state
original_all_routes, copy_all_stations, var_min, current_k = hillclimber.initial_hillclimber(map, start_algorithm)

# Run hillclimber x times
for i in range(iterations):
    routes, current_k, var_min, values_list = hillclimber.hillclimber(map, route_heuristic, original_all_routes, copy_all_stations, var_min, current_k)

    # Save best run
    if i != 0:
        if current_k > max(K_values):
            output.output(routes, current_k)

    K_values.append(current_k)
    runs.append(i)
    data.append(values_list)

# Print best score
print(f"Best score: {max(K_values):.2f}")

# Save all data in "results-values.csv" file
write_results(data)

# Plot the data
plt.plot(runs, K_values)
plt.title("Hillclimber algoritme")
plt.xlabel("Iteratie")
plt.ylabel("Score")
plt.show()

# ------- End Hillclimber algorithm ----- #


#-------------Experiments-------------

# Run random experiment
# experiment_random(map)

# Run hillclimber experiment
# experiment_hillclimber(map)

