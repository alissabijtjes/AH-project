import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot(all_stations):
    """give visual representation of the data"""

    # Plot all stations
    for station in all_stations:
        plt.plot(station.coordinates[1], station.coordinates[0], 'bo')

        # Plot all connections
        for connection in station.connections:
            plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'r-', linewidth=0.5)

    plt.title("Initiele data")
    plt.legend(["Station", "Verbinding"])
    plt.show()

def plot_routes(routes, map):
    """Plots all routes"""

    # List of colors for the different routes
    color = ["grey", "black", "pink", "yellow", "green", "red", "blue", "purple", "lightblue", "lightgreen", "brown", "olive", "cyan", "darkblue", "darkgreen", "gold"]
    j = 0

    # Plot all stations
    for station in map:
        plt.plot(station.coordinates[1], station.coordinates[0], 'bo')

    # Plot all routes
    for route in routes:

        for i in range(0, len(route.route) - 1):
            plt.plot([route.route[i].coordinates[1], route.route[i+1].coordinates[1]] , [route.route[i].coordinates[0], route.route[i+1].coordinates[0]], color=f"{color[j]}")
        
        j += 1

    plt.title("Lijnvoering")
    plt.show()

def live_plot(route, map):
    """Shows a live plot of a single route"""

    # Initiates plot
    fig = plt.figure()

    # Plots all stations
    for station in map:
        plt.plot(station.coordinates[1], station.coordinates[0], 'bo')

    # Sets start point
    x = [route.route[0].coordinates[1]]
    y = [route.route[0].coordinates[0]]

    # Sets line
    ln, = plt.plot(x,y, '-')
    
    # Sets axis
    plt.axis([3.5, 7, 50.5, 53.5])

    i = 0
    
    def update(i):
        """Function that will be called again and again to plot the route"""

        # Add the next station
        x.append(route.route[i].coordinates[1])
        y.append(route.route[i].coordinates[0])

        # Stop when all stations are visited
        if i == len(route.route) - 1:
            animation.event_source.stop()
            plt.close()

        ln.set_data(x,y)

        i += 1
        return ln,

    animation = FuncAnimation(fig, update, interval=500)
    
    plt.title("Live plot")
    plt.show()