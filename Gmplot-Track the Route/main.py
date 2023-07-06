import csv
from gmplot import gmplot  # importing

Path = input("Enter the path of your csv file , with filename and extension : ")
Zoom = int(
    input("Enter your zoom level (less value zoom out , large value zoom in ) : "))

x = 0  # for central coordinates x and y
y = 0

with open(Path, 'r') as f:
    reader = csv.reader(f)
    k = 0
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        x += lat
        y += long

# Zoom level and here total number of coordinates we're taking average
gmap = gmplot.GoogleMapPlotter(x/(100), y/(100), Zoom)


with open(Path, 'r') as f:
    reader = csv.reader(f)
    k = 0
    for row in reader:
        lat = float(row[0])
        long = float(row[1])

        if k == 0:
            gmap.marker(lat, long, 'green')
            k = 1
        else:
            gmap.marker(lat, long, 'blue')
            k = 0

gmap.marker(lat, long, 'red')
print("Done! Check file Output.html")
gmap.draw("Output.html")
