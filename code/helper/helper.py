"""Helper functions for hillclimber"""


class Compare_routes():
    """Class for comparing the amount of connections of routes."""
    
    def compare_routes(self, original_all_routes):
        """Select the route with the in comman connections."""
        selected_route = None

        for route1 in original_all_routes:
            for route2 in original_all_routes:
                if route1 != route2 and self.compare_two_routes(route1, route2):
                    selected_route = route1
                    break

        return selected_route

    def compare_two_routes(self, route1, route2, min_common_connections=3):
        """Compare two routes to check if they have at least min_common_connections in common."""

        connections1 = set(self.get_ridden_connections(route1))
        connections2 = set(self.get_ridden_connections(route2))

        common_connections = connections1.intersection(connections2)

        return len(common_connections) >= min_common_connections

    def get_ridden_connections(self, route):
        """Get a list of ridden connections between stations in the route."""
        ridden_connections = []

        for i in range(len(route.route) - 1):
            current_station = route.route[i]
            next_station = route.route[i + 1]

            for connection in current_station.connections:
                if connection[0] == next_station:
                    ridden_connections.append(tuple(connection))

        return tuple(ridden_connections)
    

class Longest_route():
    """Class for selecting the route with the highest time."""
    
    def get_longest_route(self, routes):
        longest_route = None
        max_time = -1

        for route in routes:
            if route.total_time > max_time:
                longest_route = route
                max_time = route.total_time

        return longest_route, max_time