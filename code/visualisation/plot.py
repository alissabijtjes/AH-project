import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange

def plot(all_stations):
    """give visual representation of the data"""

    for station in all_stations:
        plt.plot(station.coordinates[1], station.coordinates[0], 'bo')
        for connection in station.connections:
            plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'r-', linewidth=0.5)

    # plt.axis([4.2, 5.2, 51.5, 53.5])
    plt.legend(["Station", "Verbinding"])
    # plt.show()

def plot_(routes, map):

    color=["grey", "black", "pink", "yellow", "green", "red", "blue", "purple", "lightblue", "lightgreen", "brown", "olive", "cyan"]
    l = 0
    for route in routes:
        
        # j = 1
        for station in map:
            plt.plot(station.coordinates[1], station.coordinates[0], 'bo')
        # for station in route.route:
        for i in range(len(route.route) - 1):

            # if j == 1:
            #     plt.plot(route.route[i].coordinates[1], route.route[i].coordinates[0], 'ro')

            plt.plot([route.route[i].coordinates[1], route.route[i+1].coordinates[1]] , [route.route[i].coordinates[0], route.route[i+1].coordinates[0]], color=f"{color[l]}")


            # j += 1
        l += 1
    plt.show()

def live_plot(route, map):

    
    fig = plt.figure()
    for station in map:
        plt.plot(station.coordinates[1], station.coordinates[0], 'bo')


    # for route in routes:
    x = [route.route[0].coordinates[1]]
    y = [route.route[0].coordinates[0]]

    ln, = plt.plot(x,y, '-')
    

    plt.axis([3.5, 7, 50.5, 53.5])

    
    i = 0
    
    def update(i):
        x.append(route.route[i].coordinates[1])
        y.append(route.route[i].coordinates[0])

        if i == len(route.route) - 1:
            animation.event_source.stop()
            # plt.close()

        ln.set_data(x,y)

        i += 1
        return ln,

    animation = FuncAnimation(fig, update, interval=500)

    plt.show()

