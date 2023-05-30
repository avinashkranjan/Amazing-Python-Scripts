
from speedtest import Speedtest

def measure_internet_speed():
    speed = Speedtest()
    print("Running speed test...")

    download_speed = speed.download() 
    # To Convert to Mbps
    download_speed = download_speed / 1024 / 1024  
    print(f"Download speed: {download_speed:.2f} Mbps")

    upload_speed = speed.upload() 
    # To Convert to Mbps
    upload_speed = upload_speed / 1024 / 1024  
    print(f"Upload speed: {upload_speed:.2f} Mbps")

    ping_latency = speed.results.ping
    print(f"Ping latency: {ping_latency:.2f} ms")
    
    server = speed.get_best_server()
    print(f"Server: {server['sponsor']} ({server['name']})")

measure_internet_speed()