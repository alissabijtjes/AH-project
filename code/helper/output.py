import csv

def output(routes, score):
    """Generates output in uniform format."""

    # Create list with all station names
    station_names = []
    for route in routes:
        name_list = []
        for station in route.route:
            name_list.append(station.name)
        station_names.append((name_list, route.id))

    # Creates output in output file in folder resultaten
    with open("results/output.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["train", "stations"])

        for names in station_names:
            writer.writerow(["train_{}".format(names[1]),f'[{", ".join(names[0])}]'])

        writer.writerow(["score", "{}".format(score)])