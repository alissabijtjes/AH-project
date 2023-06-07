import csv
from station import Station

def Stations():
    # Creates list of all stations with coordinates
    stations = []
    with open("StationsHolland.csv", 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        if header != None:
            for row in reader:
                station = Station(row[0], float(row[1]), float(row[2]))
                stations.append(station)
    return stations




def Connecties():
    stations = Stations()
    with open("ConnectiesHolland.csv", 'r') as g:
        reader = csv.reader(g)
        header = next(reader)
        if header != None:
            for row in reader:

                for station in stations:
                    if station.station_name == row[0]:

                        for station in stations:
                            if station.station_name == row[1]:

                                station.add_connection(station, row[2])
                
                for station in stations:
                    if station.station_name == row[1]:

                        for station in stations:
                            if station.station_name == row[0]:
                                station.add_connection(station, row[2])

    return stations

stations = Connecties()

# connecties = Connecties()


for station in stations:
    # print(station.station_name)
    print(station.connections[0])