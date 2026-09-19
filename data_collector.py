import psutil
import platform
import time
from datetime import datetime


def get_uptime():

    uptime_seconds = int(time.time() - psutil.boot_time())

    days = uptime_seconds // 86400
    remaining_seconds = uptime_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds2 = remaining_seconds % 3600
    minutes = remaining_seconds2 // 60
    seconds = remaining_seconds2 % 60

    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"


def collect_system_info():
    computer = platform.node()
    operating_system = platform.system()

    system_info = {
        "Computer": computer,
        "Operating System": operating_system
    }

    return system_info


def collect_system_usage():
    cpu_use = psutil.cpu_percent(interval=1)
    ram_use = psutil.virtual_memory().percent
    disk_use = psutil.disk_usage("C:\\").percent

    system_usage = {
        "CPU": cpu_use,
        "Memory": ram_use,
        "Disk": disk_use
    }
    return system_usage


def get_timestamp():
    now = datetime.now()

    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_time
