"""Class station."""

class Station():
    """Class station."""
    counter = 1
    def __init__(self, name, y, x):
        """Initalize class."""
        self.id = Station.counter
        self.name = name
        self.visited = False
        self.coordinates = (y, x)
        self.connections = []
        Station.counter += 1

    def add_connection(self, destination, time):
        """"""
        self.connections.append((destination, time))
        
class Route():
    """Class route."""
    counter = 1
    def __init__(self, start):
        self.id = Route.counter
        self.route = [start]
        self.total_time = 0
        Route.counter += 1

    def add_route(self, destination, time):
        self.route.append(destination)
        self.total_time += time

    def delete_route(self, destination, time):
        self.route.remove(destination)
        self.total_time -= time

