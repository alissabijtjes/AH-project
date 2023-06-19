import csv

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