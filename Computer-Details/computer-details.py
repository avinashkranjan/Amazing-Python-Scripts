import psutil
import platform
import subprocess
import socket

# Function to get CPU information


def get_cpu_info():
    cpu_info = {}
    cpu_info['CPU'] = platform.processor()
    cpu_info['Cores'] = psutil.cpu_count(logical=False)
    cpu_info['Threads'] = psutil.cpu_count(logical=True)
    cpu_info['Clock Speed'] = f"{psutil.cpu_freq().current:.2f} MHz"
    return cpu_info

# Function to get GPU information (for any brand)


def get_gpu_info():
    gpu_info = {}
    try:
        gpus = psutil.virtual_memory().available
        if gpus:
            # If integrated graphics is available
            gpu_info['GPU Name'] = 'Integrated GPU'
            gpu_info['GPU Memory'] = f"{gpus / (1024 ** 3):.2f} GB"
            # For integrated GPUs, driver version may not be available
            gpu_info['Driver Version'] = 'N/A'
        else:
            result = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"], encoding="utf-8")
            gpu_name, memory, driver_version = result.strip().split(',')
            gpu_info['GPU Name'] = gpu_name
            gpu_info['GPU Memory'] = f"{int(memory.strip().split()[0]) / 1024:.2f} GB"
            gpu_info['Driver Version'] = driver_version.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        gpu_info['GPU Name'] = 'N/A'
        gpu_info['GPU Memory'] = 'N/A'
        gpu_info['Driver Version'] = 'N/A'
    return gpu_info

# Function to get battery status (for laptops)


def get_battery_status():
    battery_status = {}
    try:
        battery = psutil.sensors_battery()
        battery_status['Charge Percentage'] = f"{battery.percent}%"
        battery_status['Power Plugged'] = "Yes" if battery.power_plugged else "No"
        battery_status['Remaining Time'] = "Unknown" if battery.power_plugged else str(
            battery.secsleft // 60) + " minutes"
    except AttributeError:
        battery_status['Charge Percentage'] = 'N/A'
        battery_status['Power Plugged'] = 'N/A'
        battery_status['Remaining Time'] = 'N/A'
    return battery_status

# Function to get network interface information


def get_network_info():
    network_info = {}
    try:
        interfaces = psutil.net_if_addrs()
        for interface_name, addresses in interfaces.items():
            network_info[interface_name] = []
            for address in addresses:
                if address.family == socket.AddressFamily.AF_INET:
                    network_info[interface_name].append(address.address)
    except Exception as e:
        print(f"Error fetching network information: {e}")
        network_info = {}
    return network_info

# Function to get system temperature (Linux and Windows only)


def get_system_temperature():
    temp_info = {}
    try:
        # sensors = psutil.sensors_temperatures()
        temp_info = psutil.sensors_temperatures()['coretemp'][0].current
        # for sensor, entries in sensors.items():
        # temp_info[sensor] = [f"{entry.current}°C" for entry in entries]
    except Exception as e:
        print(f"Error fetching system temperature: {e}")
        temp_info = {'Temperature': 'N/A'}
    return temp_info

# Function to list installed software (Windows only)


def get_installed_software():
    software_list = {}
    try:
        process = subprocess.Popen(["wmic", "product", "get", "Name"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = process.communicate()
        software_list['Installed Software'] = [line.strip()
                                               for line in stdout.split('\n') if line.strip()]
    except FileNotFoundError:
        software_list['Installed Software'] = 'N/A'
    except Exception as e:
        print(f"Error fetching installed software: {e}")
        software_list = {'Installed Software': 'N/A'}
    return software_list

# Function to list connected USB devices


def get_usb_devices():
    usb_devices = []
    try:
        devices = psutil.disk_partitions(all=True)
        for device in devices:
            if "removable" in device.opts:
                usb_devices.append(device.device)
    except Exception as e:
        print(f"Error fetching USB devices: {e}")
    return usb_devices

# Function to get display information (Windows only)


def get_display_info():
    display_info = {}
    try:
        process = subprocess.Popen(["wmic", "desktopmonitor", "get", "ScreenHeight,ScreenWidth",
                                   "/format:list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = process.communicate()
        lines = [line.strip() for line in stdout.split('\n') if line.strip()]

        if len(lines) >= 2:
            display_info['Screen Resolution'] = f"{lines[0].split('=')[1]}x{lines[1].split('=')[1]} pixels"
        else:
            display_info['Screen Resolution'] = 'N/A'

        if len(lines) >= 3:
            display_info['Color Depth'] = f"{lines[2].split('=')[1]} bits"
        else:
            display_info['Color Depth'] = 'N/A'

        if len(lines) >= 4:
            display_info['Refresh Rate'] = f"{lines[3].split('=')[1]} Hz"
        else:
            display_info['Refresh Rate'] = 'N/A'

    except FileNotFoundError:
        display_info['Screen Resolution'] = 'N/A'
        display_info['Color Depth'] = 'N/A'
        display_info['Refresh Rate'] = 'N/A'
    except Exception as e:
        print(f"Error fetching display information: {e}")
    return display_info

# Function to get audio devices information (Windows only)


def get_audio_devices_info():
    audio_devices_info = {}
    try:
        process = subprocess.Popen(["powershell", "(Get-WmiObject -Class Win32_SoundDevice).Name"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = process.communicate()
        audio_devices_info['Audio Devices'] = [line.strip()
                                               for line in stdout.split('\n') if line.strip()]
    except FileNotFoundError:
        audio_devices_info['Audio Devices'] = 'N/A'
    except Exception as e:
        print(f"Error fetching audio devices information: {e}")
        audio_devices_info = {'Audio Devices': 'N/A'}
    return audio_devices_info

# Function to check internet connectivity


def check_internet_connectivity():
    try:
        subprocess.check_call(["ping", "-c", "1", "www.google.com"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False
    except Exception as e:
        print(f"Error checking internet connectivity: {e}")
        return False

# Function to get current date and time


def get_current_date_time():
    import datetime
    try:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(f"Error getting current date and time: {e}")
        return 'N/A'

# Function to get total and available RAM and disk space


def get_memory_disk_space_info():
    try:
        svmem = psutil.virtual_memory()
        total_memory_gb = svmem.total / (1024 ** 3)
        available_memory_gb = svmem.available / (1024 ** 3)

        total_disk = psutil.disk_usage('/')
        total_disk_gb = total_disk.total / (1024 ** 3)
        available_disk_gb = total_disk.free / (1024 ** 3)

        return {
            'Total Memory (RAM)': total_memory_gb,
            'Available Memory (RAM)': available_memory_gb,
            'Total Disk Space': total_disk_gb,
            'Available Disk Space': available_disk_gb
        }
    except Exception as e:
        print(f"Error fetching memory and disk space information: {e}")
        return {
            'Total Memory (RAM)': 'N/A',
            'Available Memory (RAM)': 'N/A',
            'Total Disk Space': 'N/A',
            'Available Disk Space': 'N/A'
        }


if __name__ == "__main__":
    if platform.system() != 'Windows':
        print("Sorry, the script is currently available only for Windows Operating System")
    else:
        print("\n---- CPU Information ----")
        print(get_cpu_info())

        print("\n---- GPU Information ----")
        print(get_gpu_info())

        print("\n---- Battery Status ----")
        print(get_battery_status())

        print("\n---- Network Interface Information ----")
        print(get_network_info())

        print("\n---- System Temperature ----")
        print(get_system_temperature())

        print("\n---- Installed Software ----")
        print(get_installed_software())

        print("\n---- Connected USB Devices ----")
        print(get_usb_devices())

        print("\n---- Display Information ----")
        print(get_display_info())

        print("\n---- Audio Devices Information ----")
        print(get_audio_devices_info())

        print("\n---- Internet Connectivity ----")
        print("Connected" if check_internet_connectivity() else "Disconnected")

        print("\n---- Current Date and Time ----")
        print(get_current_date_time())

        print("\n---- RAM and Disk Space Information ----")
        memory_disk_info = get_memory_disk_space_info()
        print(
            f"Total Memory (RAM): {memory_disk_info['Total Memory (RAM)']:.2f} GB")
        print(
            f"Available Memory (RAM): {memory_disk_info['Available Memory (RAM)']:.2f} GB")
        print(
            f"Total Disk Space: {memory_disk_info['Total Disk Space']:.2f} GB")
        print(
            f"Available Disk Space: {memory_disk_info['Available Disk Space']:.2f} GB")
