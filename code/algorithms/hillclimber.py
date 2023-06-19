"""Hillclimber file."""

from code.algorithms import random_run
from code.algorithms import greedy
from code.imports import import_data
import random
from code.classes.route import Route
from code.classes.station import Station
import copy
from resultaten.write_results import write_results

# optie heuristiek: laatste station weghalen (bv. Alkmaar-Den Helder-Alkmaar)

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
    
    return original_all_routes, copy_all_stations, all_stations, var_min, first_k


def hillclimber(map, original_all_routes, copy_all_stations, all_stations, var_min, current_k):
    
    # original solution total minutes routes
    var_min_first = var_min

    #random route current 
    random_current_route = random.choice(original_all_routes)
    min_current_route = random_current_route.total_time
    
    index = original_all_routes.index(random_current_route)

    # voor de overige tracks de connecties van route.route naar copy_all_stations
    new_all_routes = []

    for route in original_all_routes:
        #i = original_all_routes.index(route)
        #if i is not index:
            #print("----------------treinbegin", route.route[0].name)
            #print(copy_all_stations)
            for station in copy_all_stations:
                if station.name == route.route[0].name:
                    start_station = station
                    new_route = Route(start_station)
                    station.set_visited()
    

            for i in range(0, len(route.route) - 1):
                route_station = route.route[i]

                for station in copy_all_stations:
                    if station.name == route_station.name:
                        for connection in station.connections:
                            if connection[0].name == route.route[i+1].name:
                                destination = connection
                                station = destination[0]
                                time = destination[1]
                                station.set_visited()
                                new_route.add_route(station, time)
                                # Set connections to ridden
                                station.ridden_connection(route_station)
                                route_station.ridden_connection(station)


                        # station.connections = route_station.connections

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

    # new random route
    new_route = random_run.route_(copy_all_stations, map)
    #new_route = greedy.greedy(copy_all_stations, map)
    min_new_route = new_route.total_time

    # op plek van current route de nieuwe route
    # print(original_all_routes)
    # print(index)
    # print(new_route)
    # original_all_routes[index] = new_route
    new_all_routes = copy.deepcopy(original_all_routes)
    new_all_routes[index] = new_route

    var_min_new = 0
    for route in new_all_routes:
        var_min_new += route.total_time


    # Variabels calculation
    var_t = len(new_all_routes)
    #print("t-waarde", var_t)
    var_p = random_run.fraction_p(copy_all_stations)
    #print("p-waarde", var_p) 
    var_min_totaal = var_min_new
    #var_min_totaal = var_min_first - min_current_route + min_new_route
    #print("min-waarde", var_min_totaal)
    var_k = var_p * 10000 - (var_t * 100 + var_min_totaal)
    print("k-waarde", var_k)
    print("current k", current_k)

    # wel alle stations ook bereikt
    if var_k > current_k:
        original_all_routes = new_all_routes
        current_k = var_k
        var_min = var_min_totaal

    values_list = [var_p, var_t, var_min, current_k]

    return original_all_routes, current_k, var_min, values_list
