import csv
import random

from code.imports import import_data
from code.helper import score_function
from code.classes.route import Route

def route_(all_stations, map):
    """Creates one train route."""

    # Set correct value for the maximum time
    if map == "Nationaal":
        max_allowed_time = 180
    
    if map == "Holland":
        max_allowed_time = 120

    # Creates route object with random start point
    start_point = random.choice(all_stations)

    # Create route object
    route = Route(start_point)

    # Loop until total time is less than two hours
    while route.total_time < max_allowed_time:
        
        # Set current station als last station in list
        current_station = route.route[-1]

        # Choose random next destination
        destination = random.choice(current_station.connections)

        station = destination[0]
        time = destination[1]

        # Stop if time would be exceeded 
        if route.total_time + time > max_allowed_time:
            break

        else:
            station.set_visited()
            route.add_station(station, time)

            # Set connections to ridden
            station.ridden_connection(current_station)
            current_station.ridden_connection(station)
    
    return route


def random_algorithm(map, max_routes=None):
    """Produces random solution with given map."""

    all_routes = []
    Min = 0
    all_stations = import_data.import_(map)
    
    # Set correct value for maximum train routes
    if max_routes == None:
        if map == "Nationaal":
            max_routes = random.randint(1,20)

        if map == "Holland":
            max_routes = random.randit(1,7)

    # Create the routes
    for i in range(0, max_routes):
        route = route_(all_stations, map)
        Min += route.total_time
        all_routes.append(route)

    # Calculate K-value (score)
    T = len(all_routes)
    P = score_function.fraction_p(all_stations)
    K = score_function.calculate_var_k(P, T, Min)

    return all_routes, K, all_stations
