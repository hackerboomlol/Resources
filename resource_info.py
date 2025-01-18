import os
import platform
import subprocess
import sys
from datetime import datetime

# Function to install required packages
def install_packages():
    required_packages = ['psutil==5.9.5', 'speedtest-cli==2.1.3']
    for package in required_packages:
        try:
            __import__(package.split('==')[0])
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required packages if not already installed
install_packages()

# Now import the required libraries
import psutil
import speedtest

def get_system_info():
    # OS Information
    os_info = platform.system() + " " + platform.version()

    # CPU Information
    cpu_cores = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent(interval=1)

    # RAM Information
    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024 ** 3), 2)  # in GB
    ram_used = round(ram.used / (1024 ** 3), 2)  # in GB
    ram_percent = ram.percent

    # Storage Information
    disk = psutil.disk_usage('/')
    disk_total = round(disk.total / (1024 ** 3), 2)  # in GB
    disk_used = round(disk.used / (1024 ** 3), 2)  # in GB
    disk_percent = disk.percent

    # Internet Speed
    st = speedtest.Speedtest()
    download_speed = round(st.download() / (1024 ** 2), 2)  # in Mbps
    upload_speed = round(st.upload() / (1024 ** 2), 2)  # in Mbps

    # Current Time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "OS": os_info,
        "CPU Cores": cpu_cores,
        "CPU Usage (%)": cpu_usage,
        "RAM Total (GB)": ram_total,
        "RAM Used (GB)": ram_used,
        "RAM Usage (%)": ram_percent,
        "Storage Total (GB)": disk_total,
        "Storage Used (GB)": disk_used,
        "Storage Usage (%)": disk_percent,
        "Download Speed (Mbps)": download_speed,
        "Upload Speed (Mbps)": upload_speed,
        "Current Time": current_time
    }

def display_info(info):
    print("===== System Resource Information =====")
    for key, value in info.items():
        print(f"{key}: {value}")
    print("======================================")

if __name__ == "__main__":
    info = get_system_info()
    display_info(info)
