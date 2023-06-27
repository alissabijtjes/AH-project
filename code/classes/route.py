class Route():
    """A complete route with all stations and total time."""

    counter = 1
    def __init__(self, start):
        self.id = Route.counter
        self.route = [start]
        self.total_time = 0
        Route.counter += 1

    def add_station(self, destination, time):
        """Add one station to the route."""
        self.route.append(destination)
        self.total_time += time

    # def delete_station(self, destination, time):
    #     """Removes one station from the route."""
    #     self.route.remove(destination)
    #     self.total_time -= time
