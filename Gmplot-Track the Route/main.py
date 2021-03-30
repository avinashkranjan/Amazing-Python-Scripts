
import csv
from gmplot import gmplot #importing

gmap = gmplot.GoogleMapPlotter(37.771260, -122.511011,17) #17 is here zoom level

Path=input("Enter the path of your csv file , with filename and extension : ")
with open(Path,'r') as f:
    reader=csv.reader(f)
    k=0
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        
        if k==0:
            gmap.marker(lat, long, 'green')
            k=1
        else:
            gmap.marker(lat,long,'blue')
        
gmap.marker(lat,long,'red')
print("Done! Check file Output.html")
gmap.draw("Output.html")
