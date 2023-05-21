import psutil

# Function to retrieve CPU temperature
def get_cpu_temperature():
    try:
        # Retrieve temperature information using psutil
        # and access the first temperature value from the 'coretemp' key
        temperature = psutil.sensors_temperatures()['coretemp'][0].current
        return temperature
    except (KeyError, IndexError):
        # Handle cases where temperature information is not available
        return "CPU temperature information not available."

# Call the get_cpu_temperature() function to get the CPU temperature
cpu_temperature = get_cpu_temperature()

# Print the CPU temperature
print("Current CPU Temperature (Celsius):", cpu_temperature)

