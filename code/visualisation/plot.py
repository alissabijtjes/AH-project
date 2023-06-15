import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plot(map):
    """give visual representation of the data"""

    for station in map:
        plt.plot(station.coordinates[1], station.coordinates[0], 'ro')
        for connection in station.connections:
            plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-')

    # plt.axis([4.2, 5.2, 51.5, 53.5])
    plt.show()

def plot_(routes, map):
    
    fig = plt.figure()

    color=["grey", "black", "pink", "yellow", "green", "red", "blue"]
    l = 0
    for route in routes:
        
        # j = 1
        for station in map:
            plt.plot(station.coordinates[1], station.coordinates[0], 'bo')
        # for station in route.route:
        for i in range(len(route.route) - 1):

            # if j == 1:
            #     plt.plot(route.route[i].coordinates[1], route.route[i].coordinates[0], 'ro')

            plt.plot([route.route[i].coordinates[1], route.route[i+1].coordinates[1]],[route.route[i].coordinates[0], route.route[i+1].coordinates[0]])#, color=f"{color[l]}")


            # j += 1
        l += 1
    plt.show()


    # plt.show()