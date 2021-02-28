# import datetime library in python
from datetime import datetime
# Saves a .txt file with file name
# as 2020-01-11-10-20-23.txt  at current time indicated by now function of datetime library
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), "w") as myfile:
    # instead of now i could also initialse with datetime(1999, 12, 12, 12, 12, 12, 342380) to give the time values to datetime constructor
    # Content of the file (it can be any script in python which we want to run at a particular time )
    myfile.write("hii guys ,your Lunch time begins ! ")
