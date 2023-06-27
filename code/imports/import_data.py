import csv
from code.classes.station import Station

def import_(map):
    """Import stations and connecties from given map (Holland or Nationaal)."""

    # Import stations
    stations = []
    with open(f"data/Stations{map}.csv", 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        if header != None:
            for row in reader:
                station = Station(row[0], float(row[1]), float(row[2]))
                stations.append(station)

    # Add connections
    with open(f"data/Connecties{map}.csv", 'r') as g:
        reader = csv.reader(g)
        header = next(reader)
        if header != None:
            for row in reader:

                for station_1 in stations:
                    if station_1.name == row[0]:

                        for station_2 in stations:
                            if station_2.name == row[1]:
                                station_1.add_connection(station_2, float(row[2]))
                
                for station_1 in stations:
                    if station_1.name == row[1]:

                        for station_2 in stations:
                            if station_2.name == row[0]:
                                station_1.add_connection(station_2, float(row[2]))

    return stations
