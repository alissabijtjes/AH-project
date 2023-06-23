import csv
import random

from code.imports.import_data import import_data
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
    # i = 0
    # while start_point.visited:
    #     i += 1
    #     start_point = random.choice(all_stations)
    #     if i > 50:
    #         break
        

    route = Route(start_point)


    # Loop until total time is less than two hours
    while route.total_time < max_allowed_time:
        
        # Set current station als last station in list
        current_station = route.route[-1]

        # Choose random next destination
        destination = random.choice(current_station.connections)

        # destination = None

        # for connection in current_station.connections:
        #     # print(connection[0].name)
        #     if connection[0].visited == False:
        #         # print(connection[0].name)
        #         destination = connection
                
        # if destination == None:
        #     destination = random.choice(current_station.connections)

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


# def fraction_p(all_stations):
#     """Calculates the fraction of ridden connections."""

#     ridden = 0
#     total = 0

#     # Loops over all stations
#     for station in all_stations:

#         # Loops over all connection for every station and check if station in ridden
#         for connection in station.connections:
#             total += 1
#             if connection[2]:
#                 ridden += 1
    
#     return ridden / total


def random_algorithm(map):
    """Produces random solution with given map."""

    all_routes = []
    Min = 0
    all_stations = import_data(map)
    
    # Set correct value for maximum train routes
    if map == "Nationaal":
        max_routes = 20

    if map == "Holland":
        max_routes = 7

    # Create the routes
    for i in range(0, max_routes):
        route = route_(all_stations, map)
        Min += route.total_time
        all_routes.append(route)

    # Calculate K-value (score)
    T = len(all_routes)
    P = score_function.fraction_p(all_stations)
    K = score_function.calculate_var_k(P, T, Min)

    return all_routes, K
