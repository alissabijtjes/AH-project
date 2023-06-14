import csv
import random

from code.imports.import_data import import_data
from code.classes.station import Station
from code.classes.route import Route

def route_(all_stations, map):
    
    """Creates one train route"""

    # set correct value for the maximum time
    if map == "Nationaal":
        max_allowed_time = 180
    
    if map == "Holland":
        max_allowed_time = 120


    # creates route object with random start point
    route = Route(random.choice(all_stations))

    # loop until total time is less than two hours
    while route.total_time < 120:
        
        # set current station als last station in list
        current_station = route.route[-1]

        # choose random next destination
        destination = random.choice(current_station.connections)
        station = destination[0]
        time = destination[1]

        # stop if time would be exceeded 
        if route.total_time + time > max_allowed_time:
            break

        else:
            route.add_route(station, time)

            # set connections to ridden
            station.ridden_connection(current_station)
            current_station.ridden_connection(station)
    
    return route

def fraction_p(all_stations):
    """calculates the fraction of ridden connections"""
    ridden = 0
    total = 0

    # loops over all stations
    for station in all_stations:

        # loops over all connection for every station and check if station in ridden
        for connection in station.connections:
            total += 1
            if connection[2]:
                ridden += 1
    
    return ridden / total


def output(routes, score):
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



def random_algorithm(map):
    
    all_routes = []
    Min = 0
    all_stations = import_data(map)
    
    # set correct value for maximum train routes
    if map == "Nationaal":
        max_routes = 20

    if map == "Holland":
        max_routes = 7

    # create the routes
    for i in range(0, max_routes):
        route = route_(all_stations, map)
        Min += route.total_time
        all_routes.append(route)

    # calculate score
    T = len(all_routes)
    P = fraction_p(all_stations)
    K = P*10000 - (T*100 + Min)

    return all_routes, K
