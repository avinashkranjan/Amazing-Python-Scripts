import psutil

# Function to retrieve CPU temperature


def get_cpu_temperature() -> float | str:
    """A function which returns the temperature of the CPU

    Returns:
        float | str: The temperature value in Celsius or 'NA' if temperature info. is unavailable
    """
    try:
        # Retrieve temperature information using psutil
        # and access the first temperature value from the 'coretemp' key
        temperature = psutil.sensors_temperatures()['coretemp'][0].current
        return temperature
    except (KeyError, IndexError):
        # Handle cases where temperature information is not available
        return "NA"


def get_ram_and_cpu_util() -> list:
    """Get the utilization of system RAM and CPU

    Returns:
        list: Contains total memory of system, percentage utilized and percantage of CPU utilized
    """
    memory_stats = psutil.virtual_memory()
    return [
        # Total memory available in the system (MB)
        memory_stats[0]//(1024*1024),
        memory_stats[2],  # Percentage of memory utilized
        # Percentage of CPU utilized
        psutil.cpu_percent(interval=4, percpu=True)
    ]


# Call the get_cpu_temperature() function to get the CPU temperature
cpu_temperature = get_cpu_temperature()

# Call the get_ram_and_cpu_util() function to get data on system resource utilization
system_utils = get_ram_and_cpu_util()

# Print the system info
if (type(system_utils[2]) == list):
    cpu_percentage = ""
    for i in system_utils[2]:
        cpu_percentage += "{}%, ".format(i)
else:
    cpu_percentage = '{}%'.format(system_utils[2])

print(
    f"Current CPU Temperature in Celsius is {cpu_temperature}°C, with percentage utilized being at {cpu_percentage}")
print(f"Current RAM utilization is {system_utils[1]}% of {system_utils[0]} MB")
