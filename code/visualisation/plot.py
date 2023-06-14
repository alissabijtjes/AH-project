import matplotlib.pyplot as plt

def plot(map):
    """give visual representation of the data"""

    for station in map:
        plt.plot(station.coordinates[1], station.coordinates[0], 'ro')
        for connection in station.connections:
            plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-')

    # plt.axis([4.2, 5.2, 51.5, 53.5])
    plt.show()
