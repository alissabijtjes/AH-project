class Station():
    """Station object with name, coordinates and connections."""

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
        """Add connection to station."""
        self.connections.append([destination, time, False])

    def ridden_connection(self, destination):
        """Sets a connection to ridden."""
        for connection in self.connections:
            if connection[0].name == destination.name:
                connection[2] = True

    def unridden_connection(self, destination):
        """Sets a connection to unridden."""
        for connection in self.connections:
            if connection[0].name == destination.name:
                connection[2] = False

    def set_visited(self):
        """Sets station to visited"""
        self.visited = True

