from code.import_data import stations
import matplotlib.pyplot as plt
import csv
import random

from code.station import Station
from code.route import Route



def route_():
    """Creates one train route"""

    # creates route object with random start point
    route = Route(random.choice(stations))

    # loop until total time is less than two hours
    while route.total_time < 120:
        
        # set current station als last station in list
        current_station = route.route[-1]

        # choose random next destination
        destination = random.choice(current_station.connections)
        station = destination[0]
        time = destination[1]

        # stop if time would be exceeded 
        if route.total_time + time > 120:
            break
        else:
            route.add_route(station, time)

            # set connections to ridden
            station.ridden_connection(current_station)
            current_station.ridden_connection(station)
    
    return route

def main():

    all_routes = []
    Min = 0

    for i in range(0,7):
        route = route_()
        Min += route.total_time
        all_routes.append(route)

    T = len(all_routes)
    P = fraction_p()
    
    K = P*10000 - (T*100 + Min)

    return all_routes, K

def fraction_p():

    ridden = 0
    total = 0
    for station in stations:
        for connection in station.connections:
            total += 1
            if connection[2]:
                ridden += 1
    
    return ridden / total




def Plot():
    """give visual representation of the data"""

    for station in stations:
        plt.plot(station.coordinates[1], station.coordinates[0], 'ro')
        for connection in station.connections:
            plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-')

    # plt.axis([4.2, 5.2, 51.5, 53.5])
    plt.show()


def Output(routes, score):
    station_names = []
    for route in routes:
        name_list = []
        for station in route.route:
            name_list.append(station.name)
        station_names.append((name_list, route.id))

    with open("resultaten/output.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["train", "stations"])

        for names in station_names:
            writer.writerow(["train_{}".format(names[1]),f'[{", ".join(names[0])}]'])

        writer.writerow(["score", "{}".format(score)])


total_routes, K = main()

Output(total_routes, K)