from import_data import stations
import matplotlib.pyplot as plt
import csv

def Plot():
    """give visual representation of the data"""

    for station in stations:
        plt.plot(station.coordinates[1], station.coordinates[0], 'ro')
        for connection in station.connections:
            plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-')

    # plt.axis([4.2, 5.2, 51.5, 53.5])
    plt.show()

# Plot()

def Output():
    with open("output.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["train", "stations"])
        writer.writerow(["traject","stations"])
        # writer.writerow([train_2,"[Amsterdam Sloterdijk, Amsterdam Centraal, Amsterdam Amstel, Amsterdam Zuid, Schiphol Airport]"])
        # writer.writerow([train_3,"[Rotterdam Alexander, Gouda, Alphen a/d Rijn, Leiden Centraal, Schiphol Airport, Amsterdam Zuid]"])
        writer.writerow(["score", "3819"])

Output()