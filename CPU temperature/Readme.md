# CPU Temperature

This Python script is used to retrieve the CPU temperature using the psutil library.


## Prerequisites
- Python installed on your machine
- `psutil` library installed. You can install it by running the following command:
  
 ```bash
  pip install psutil
 ```

## Explanation of the Script

The script utilizes the `psutil` library's `sensors_temperatures()`, `virtual_memory()` and `cpu_percent()` functions to output data that tells us about the system's resource consumption.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the "CPU Temperature" folder.
3. Install the `psutil` library if you haven't already by running the following command:

    ```bash
    pip install psutil
    ```
## Output

The script will display the current CPU temperature in Celsius alongwith CPU Percentage Used.
In addition, it'll display the percentage used and total RAM of the system.

Sample Output:

```
Current CPU Temperature (Celsius): 60, with percentage utilized being at 3.1%,
Current RAM utilization is 75.3% of 512 MB
```


## Compatibility

Please note that the script is primarily designed for Linux-based systems. While it may work on other platforms, the availability and format of temperature information can vary. Ensure that your system supports the `psutil` library and has the necessary sensors for CPU temperature measurement.
However, the CPU and RAM utilization functionalities would work regaurdless of the Operating System.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.


