
import csv  #csv - Comma Separated Values
from gmplot import gmplot


gmap = gmplot.GoogleMapPlotter(20.613456, 72.9431185,17) #Plotting data on map
#gmap.coloricon="https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png"

with open('Home/MyPC/Python/LatLong.csv','r') as f:  #give the address of csv file with respect to your folder containing .py file
    reader=csv.reader(f)
    k=0
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        
        if k==0:
            gmap.marker(lat, long, 'green')  #PLotting Markers
            k=1
        else:
            gmap.marker(lat,long,'blue')    #plotting Markers
        
gmap.marker(lat,long,'red')
gmap.draw("Output.html") #Taking output in the form of html file 
