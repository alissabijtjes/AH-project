import csv
import matplotlib.pyplot as plt

def write_results(all_lists_values):
    filename = "resultaten/results_values.csv"

    fieldnames = ['p', 't', 'min', 'k']

    # Open the file
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

         # Write the values to the file
        for values_list in all_lists_values:
            writer.writerow({'p': values_list[0], 't': values_list[1], 'min': values_list[2], 'k': values_list[3]})

def plot_results(all_lists_values):
    iterations = range(len(all_lists_values))

    # Plot p
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, [values[0] for values in all_lists_values], label='p')
    plt.xlabel('Iteration')
    plt.ylabel('p Value')
    plt.title('p')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot t
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, [values[1] for values in all_lists_values], label='t')
    plt.xlabel('Iteration')
    plt.ylabel('t Value')
    plt.title('t')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot min
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, [values[2] for values in all_lists_values], label='min')
    plt.xlabel('Iteration')
    plt.ylabel('min Value')
    plt.title('min')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot k
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, [values[3] for values in all_lists_values], label='k')
    plt.xlabel('Iteration')
    plt.ylabel('k Value')
    plt.title('k')
    plt.legend()
    plt.grid(True)
    plt.show()