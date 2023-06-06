import csv

with open("StationsHolland.csv", 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    if header != None:
        for row in reader:
            print(row)

with open("ConnectiesHolland.csv", 'r') as g:
    reader = csv.reader(g)
    header = next(reader)
    if header != None:
        for row in reader:
            print(row)