# CPU Temperature

This python script is used to get cpu temperature

- psutil (process and system utilities) is a cross-platform library.
- It is used for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python.

## Explanation of the script

- Using psutil library's inbuilt function "sensors_temperatures()" to measure temperature of CPU

## Setup instructions

- Clone the repo to your machine
- Head over to the required folder (Cpu Temperature folder)
- Install psutil using
```bash
pip install psutil
```
- Run the script
```bash
python temp.py
```

## Output

<img src="https://raw.githubusercontent.com/gavinlyonsrepo/raspberrypi_tempmon/master/screenshots/main_screen.jpg">

## Disclaimer

This does not work on a windows machine
