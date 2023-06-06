"""Class station."""

class Station():
    """Class station."""
    counter = 0
    def __init__(self, station_name, y, x):
        """Initalize class."""
        self.station_id = Station.counter
        self.station_name = station_name
        self.visited = False
        self.coordinates = (y, x)
        Station.counter += 1
