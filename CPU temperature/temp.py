# importing the psutil library
import psutil

# Note: It is not for windows user

data = psutil.sensors_temperatures()
print("Current Temperature of CPU (celcius): ", data['coretemp'][0][1])
