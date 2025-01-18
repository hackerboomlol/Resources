import os
import platform
import psutil
import speedtest

def get_system_info():
    # OS Information
    os_info = platform.system() + " " + platform.version()

    # CPU Information
    cpu_cores = psutil.cpu_count(logical=True)

    # RAM Information
    ram_info = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # in GB

    # Storage Information
    storage_info = round(psutil.disk_usage('/').total / (1024 ** 3), 2)  # in GB

    # Internet Speed
    st = speedtest.Speedtest()
    download_speed = round(st.download() / (1024 ** 2), 2)  # in Mbps
    upload_speed = round(st.upload() / (1024 ** 2), 2)  # in Mbps

    return {
        "OS": os_info,
        "CPU Cores": cpu_cores,
        "RAM (GB)": ram_info,
        "Storage (GB)": storage_info,
        "Download Speed (Mbps)": download_speed,
        "Upload Speed (Mbps)": upload_speed
    }

if __name__ == "__main__":
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")