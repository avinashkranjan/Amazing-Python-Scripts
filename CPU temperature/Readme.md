# CPU Temperature

This Python script is used to retrieve the CPU temperature using the psutil library.


## Prerequisites
- Python installed on your machine
- `psutil` library installed. You can install it by running the following command:
  ```bash
  pip install psutil


## Explanation of the Script

The script utilizes the `psutil` library's `sensors_temperatures()` function to measure the temperature of the CPU.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the "Cpu Temperature" folder.
3. Install the `psutil` library if you haven't already by running the following command:
```bash
pip install psutil
```
## Output

The script will display the current CPU temperature in Celsius.



## Compatibility

Please note that the script is primarily designed for Linux-based systems. While it may work on other platforms, the availability and format of temperature information can vary. Ensure that your system supports the `psutil` library and has the necessary sensors for CPU temperature measurement.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.


