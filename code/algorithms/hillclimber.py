"""Hillclimber file."""

from code.algorithms import random_run
from code.algorithms import greedy
from code.imports import import_data
import random
from code.classes.route import Route
import copy


def initial_hillclimber(map):

    # alle connections (all_stations en copy_all_stations) zijn hier False
    all_stations = import_data.import_data(map)
    copy_all_stations = copy.deepcopy(all_stations)

    # Initial state hill climbing
    all_routes, first_k = random_run.random_algorithm(map)
    #all_routes, first_k = greedy.complete_run(map)

    original_all_routes = []
    # new_all_routes is in begin the random solution
    var_min = 0
    for route in all_routes:
        var_min += route.total_time
        original_all_routes.append(route)
    
    return original_all_routes, copy_all_stations, var_min, first_k


def hillclimber(map, original_all_routes, copy_all_stations, var_min, current_k):

    # Compare route based on double connections
    selected_route = compare_routes(original_all_routes)
    longest_route, max_time = get_longest_route(original_all_routes)
    print(max_time)
    if selected_route is not None:
        delete_route_index = original_all_routes.index(selected_route)
        del original_all_routes[delete_route_index]
        print("select", delete_route_index)

    # Get index from longest route from all routes
    if max_time == 180.0:
        index = original_all_routes.index(longest_route)
        print("max_time")
    else:
        # Get index from random route from all routes
        random_current_route = random.choice(original_all_routes)
        index = original_all_routes.index(random_current_route)
        print("random", index)

    new_all_routes = []

    # Set all connections to false
    for station in copy_all_stations:
        for connection in station.connections:
            connection[2] = False

    for route in original_all_routes:
        for station in copy_all_stations:
            if station.name == route.route[0].name:
                start_station = station
                new_route = Route(start_station)
                station.set_visited()

        for i in range(len(route.route) - 1):
            route_station = route.route[i]
            next_station = route.route[i+1]

            for station in copy_all_stations:
                if station.name == route_station.name:
                    for connection in station.connections:
                        if connection[0].name == next_station.name:
                            destination = connection
                            des_station = destination[0]
                            time_station = destination[1]
                            route_station.set_visited()
                            new_route.add_route(des_station, time_station)
                            if connection[0].name == destination[0].name:
                                # Set connections to ridden
                                station.ridden_connection(destination[0])
                                destination[0].ridden_connection(station)
                                break                         
    
    # Variabel p before adding new route
    original_var_p = random_run.fraction_p(copy_all_stations)

    # New route
    #new_route = random_run.route_(copy_all_stations, map)
    #new_route = greedy.greedy(copy_all_stations, map)
    new_route = hillclimber_new_route(copy_all_stations, map)

    new_all_routes = copy.deepcopy(original_all_routes)
    new_all_routes[index] = new_route

    var_min_new = 0
    for route in new_all_routes:
        var_min_new += route.total_time

    # Variabels calculation
    var_t = len(new_all_routes)
    var_p = random_run.fraction_p(copy_all_stations)
    print("var_p", var_p)
    var_min_totaal = var_min_new
    #print("min-waarde", var_min_totaal)
    var_k = var_p * 10000 - (var_t * 100 + var_min_totaal)
    print("k-waarde", var_k)
    print("current k", current_k)

    # Compare current k-value with new k-value
    if var_k > current_k:
        original_all_routes = copy.deepcopy(new_all_routes)
        current_k = var_k
        var_min = var_min_totaal
    else:
        var_p = original_var_p

    values_list = [var_p, var_t, var_min, current_k]

    return original_all_routes, current_k, var_min, values_list


def hillclimber_new_route(copy_all_stations, map):
    """Creates one train route."""

    # Set correct value for the maximum time
    if map == "Nationaal":
        max_allowed_time = 180
    
    if map == "Holland":
        max_allowed_time = 120

    start_point = None
    for station in copy_all_stations:
        if station.visited == False:
            start_point = station
            station.set_visited()
            break

    # Creates route object with random start point
    start_point = random.choice(copy_all_stations)

    route = Route(start_point)

    # Loop until total time is less than two hours
    while route.total_time < max_allowed_time:
        
        # Set current station als last station in list
        current_station = route.route[-1]

        destination = None

        # Set destination to station that has not been visited
        for connection in current_station.connections:
            if connection[0].visited == False:
                destination = connection
                break
        
        # If all stations are visited, set destination to station with not ridden connection
        if destination == None:
            for connection in current_station.connections:
                if connection[2] == False:
                    destination = connection
                    break

        # Choose random next destination
        if destination is None:
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


def compare_routes(original_all_routes):
    selected_route = None

    for route1 in original_all_routes:
        for route2 in original_all_routes:
            if route1 != route2 and compare_two_routes(route1, route2):
                selected_route = route1
                break

    return selected_route


def compare_two_routes(route1, route2, min_common_connections=5):
    """
    Compare two routes to check if they have at least min_common_stations in common.
    """

    connections1 = set(get_ridden_connections(route1))
    connections2 = set(get_ridden_connections(route2))

    common_connections = connections1.intersection(connections2)
    #print(common_connections)

    return len(common_connections) >= min_common_connections


def get_ridden_connections(route):
    """
    Get a list of ridden connections between stations in the route.
    """
    ridden_connections = []

    for i in range(len(route.route) - 1):
        current_station = route.route[i]
        next_station = route.route[i + 1]

        for connection in current_station.connections:
            if connection[0] == next_station:
                ridden_connections.append(tuple(connection))

    return tuple(ridden_connections)


def get_longest_route(routes):
    longest_route = None
    max_time = -1

    for route in routes:
        if route.total_time > max_time:
            longest_route = route
            max_time = route.total_time

    return longest_route, max_time