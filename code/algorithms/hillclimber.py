"""Hillclimber file."""

from code.algorithms import random_run
from code.algorithms import greedy
from code.imports import import_data
import random
from code.classes.route import Route
from code.classes.station import Station
import copy

# optie heuristiek: laatste station weghalen (bv. Alkmaar-Den Helder-Alkmaar)

def initial_hillclimber(map):

    # alle connections (all_stations en copy_all_stations) zijn hier False
    all_stations = import_data.import_data(map)
    copy_all_stations = copy.deepcopy(all_stations)

    # Initial state hill climbing
    #all_routes, first_k = random_run.random_algorithm(map)
    all_routes, first_k = greedy.complete_run(map)

    new_all_routes = []
    # new_all_routes is in begin the random solution
    var_min = 0
    for route in all_routes:
        var_min += route.total_time
        new_all_routes.append(route)
    
    return new_all_routes, copy_all_stations, all_stations, var_min, first_k


def hillclimber(map, new_all_routes, copy_all_stations, all_stations, var_min, current_k):
    
    # original solution total minutes routes
    var_min_first = var_min

    #random route current 
    random_current_route = random.choice(new_all_routes)
    min_current_route = random_current_route.total_time
    
    index = new_all_routes.index(random_current_route)

    # voor de overige tracks de connecties van route.route naar copy_all_stations
    for route in new_all_routes:
        i = new_all_routes.index(route)
        if i is not index:
            #print("----------------treinbegin", route.route[0].name)
            #print(copy_all_stations)
            for station in copy_all_stations:
                if station.name == route.route[0].name:
                    start_station = station
            for list_item in route.route:
                for station in copy_all_stations:
                    if station.name == list_item.name:
                        station.connections = list_item.connections

    # # Set every connection to false
    # for station in copy_all_stations:
    #     for connection in station.connections:
    #         connection[2] = False

    # # Set if connections are made to true, not the place where the new random route is getting placed
    # for route in new_all_routes:
    #     i = new_all_routes.index(route)
    #     if i != index:
    #         #print("----------------treinbegin", route.route[0].name)
    #         j = 0
    #         for j in range(len(route.route) - 1):
    #             current_station = route.route[j]
    #             next_station = route.route[j + 1]
    #             for station in copy_all_stations:
    #                 if station.name == current_station.name:
    #                     for connection in station.connections:
    #                         if connection[0].name == next_station.name:
    #                             connection[2] = True

    # for station in copy_all_stations:
    #     for connection in station.connections: 
    #         print(connection[2])                      

    # new random route
    new_route = random_run.route_(all_stations, map)
    #new_route = greedy.greedy(all_stations, map)
    min_new_route = new_route.total_time

    # op plek van current route de nieuwe route
    new_all_routes[index] = new_route


    # Variabels calculation
    var_t = len(new_all_routes)
    #print("t-waarde", var_t)
    var_p = random_run.fraction_p(copy_all_stations)
    print("p-waarde", var_p) 
    var_min_totaal = (var_min_first - min_current_route) + min_new_route
    #print("min-waarde", var_min_totaal)
    var_k = var_p * 10000 - (var_t * 100 + var_min_totaal)
    #print("k-waarde", var_k)
    #print("current k", current_k)

    # wel alle stations ook bereikt
    if var_k > current_k:
        new_all_routes[index] = new_route
        current_k = var_k
        var_min = var_min_totaal
        #print("nieuwe hoger dan oude")
    else:
        new_all_routes[index] = random_current_route
        #print("blijft hetzelfde")

    return new_all_routes, current_k, var_min