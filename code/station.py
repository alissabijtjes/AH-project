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


