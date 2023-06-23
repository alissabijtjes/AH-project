import csv
import random

from code.imports.import_data import import_data
from code.classes.route import Route
from code.helper import score_function

def my_Func(all_stations):
    """funtion to sort stations by their number of connections"""
    return(len(all_stations.connections))


def greedy(all_stations, map):
    """Creates one train route."""

    # Set correct value for the maximum time
    if map == "Nationaal":
        max_allowed_time = 180
    
    if map == "Holland":
        max_allowed_time = 120

    # Creates route object with start point at not visited station
    start_point = None

    # Sort stations on amount of connections
    all_stations.sort(key=my_Func)

    # Set start station to station that has not been visited yet
    for station in all_stations:
        if station.visited == False:
            start_point = station
            station.set_visited()
            break

    # If all stations are visited, set start station to station with not ridden connection
    if start_point == None:
        stop = False

        for station in all_stations:
            for connection in station.connections:
                if connection[2] == False:
                    start_point = station
                    station.set_visited()
                    stop = True
                    break

            if stop:
                break
        
    route = Route(start_point)


    # Loop until total time is less than two hours
    while route.total_time < max_allowed_time:
        
        # Set current station als last station in list
        current_station = route.route[-1]

        destination = None 
        
        # If all stations are visited, set destination to station with not ridden connection
        if destination == None:
            for connection in current_station.connections:
                if connection[2] == False:
                    destination = connection
                    break
        
        # if all connections are ridden, look one station further and choose station which has a non ridden connection
        if destination == None:
            stop = False
            for connection in current_station.connections:
                for next_connection in connection[0].connections:
                    if next_connection[2] == False:
                        destination = connection
                        stop = True
                        break

                if stop:
                    break

        # else, set destination random(could later be improved)
        if destination == None:
            break
            destination = random.choice(current_station.connections)

        station = destination[0]
        time = destination[1]

        # Stop if time would be exceeded 
        if route.total_time + time > max_allowed_time:
            break

        else:
            station.set_visited()
            route.add_route(station, time)

            # Set connections to ridden
            station.ridden_connection(current_station)
            current_station.ridden_connection(station)
    
    return route


def complete_run(map):
    """Produces random solution with given map."""

    all_routes = []
    Min = 0
    all_stations = import_data(map)
    
    # Set correct value for maximum train routes
    if map == "Nationaal":
        max_routes = 20

    if map == "Holland":
        max_routes = 10

    # Create the routes
    for i in range(0, max_routes):
        P = score_function.fraction_p(all_stations)

        # Stop running if all connections are ridden
        if P == 1:
            break

        # Create route
        route = greedy(all_stations, map)
        Min += route.total_time
        all_routes.append(route)
     

    # Calculate K-value (score)
    T = len(all_routes)
    K = score_function.calculate_var_k(P, T, Min)

    return all_routes, K