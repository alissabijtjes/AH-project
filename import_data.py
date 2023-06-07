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

stations = Stations()


def Connecties():
    # connecties = []
    with open("ConnectiesHolland.csv", 'r') as g:
        reader = csv.reader(g)
        header = next(reader)
        if header != None:
            for row in reader:
                print(row)

    return None

# connecties = Connecties()


# for station in stations:
#     print(station.station_name, station.station_id)