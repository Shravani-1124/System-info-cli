import platform
import socket
import os
import psutil
import time
import argparse

def get_sys_info():
    opsys = platform.system()
    architecture = platform.machine()
    processor = platform.processor()
    hostname = socket.gethostname()

    sys_info = {
        "os": opsys,
        "architecture": architecture,
        "processor": processor,
        "hostname": hostname
    }

    return sys_info


def get_cpu_info():
    cpu_count = os.cpu_count()
    cpu_usage = psutil.cpu_percent(interval=1)

    cpu_info = {
        "CPU count": cpu_count,
        "CPU usage": cpu_usage
    }

    return cpu_info

def get_memory_info():
    memory = psutil.virtual_memory()

    total = memory.total
    used = memory.used
    available = memory.available
    percentage = memory.percent

    memory_info = {
        "total": total,
        "used": used,
        "available": available,
        "percentage": percentage
    }

    return memory_info
def bytes_to_gb(bytes_value):
    return bytes_value / (1024 ** 3)

def get_disk_info():
    disk = psutil.disk_usage("/")

    total = disk.total
    used = disk.used
    free = disk.free
    percentage = disk.percent

    disk_info = {
        "total": total,
        "used": used,
        "free": free,
        "percentage": percentage
    }

    return disk_info

def get_network_info():
    hostname = socket.gethostname()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()

    network_info = {
        "hostname": hostname,
        "local_ip": local_ip
    }

    return network_info

def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()

    uptime = current_time - boot_time

    return uptime

def format_uptime(seconds):
    days = int(seconds // (24 * 60 * 60))
    hours = int((seconds % (24 * 60 * 60)) // (60 * 60))
    minutes = int((seconds % (60 * 60)) // 60)
    seconds = int(seconds % 60)

    return f"{days}d {hours}h {minutes}m {seconds}s"

def display_cpu_info(cpu_info):
    print("CPU INFORMATION")
    print("----------------")
    print(f"CPU Count : {cpu_info['CPU count']}")
    print(f"CPU Usage : {cpu_info['CPU usage']}%")


def display_full_report():
    sys_info = get_sys_info()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()
    network_info = get_network_info()
    uptime = get_uptime()

    print("SYSTEM INFORMATION")
    print("------------------")
    print(f"OS           : {sys_info['os']}")
    print(f"Architecture : {sys_info['architecture']}")
    print(f"Processor    : {sys_info['processor']}")
    print(f"Hostname     : {sys_info['hostname']}")

    print()
    display_cpu_info(cpu_info)

    print()
    print("MEMORY INFORMATION")
    print("------------------")
    print(f"Total     : {bytes_to_gb(memory_info['total']):.2f} GB")
    print(f"Used      : {bytes_to_gb(memory_info['used']):.2f} GB")
    print(f"Available : {bytes_to_gb(memory_info['available']):.2f} GB")
    print(f"Usage     : {memory_info['percentage']}%")

    print()
    print("DISK INFORMATION")
    print("----------------")
    print(f"Total : {bytes_to_gb(disk_info['total']):.2f} GB")
    print(f"Used  : {bytes_to_gb(disk_info['used']):.2f} GB")
    print(f"Free  : {bytes_to_gb(disk_info['free']):.2f} GB")
    print(f"Usage : {disk_info['percentage']}%")

    print()
    print("NETWORK INFORMATION")
    print("-------------------")
    print(f"Hostname  : {network_info['hostname']}")
    print(f"Local IPv4: {network_info['local_ip']}")

    print()
    print("UPTIME")
    print("------")
    print(f"Uptime : {format_uptime(uptime)}")

def main():
    parser = argparse.ArgumentParser(
        description="System information CLI"
    )

    parser.add_argument(
        "--cpu",
        action="store_true",
        help="Display CPU information only"
    )

    args = parser.parse_args()

    if args.cpu:
        cpu_info = get_cpu_info()
        display_cpu_info(cpu_info)
    else:
        display_full_report()


if __name__ == "__main__":
    main()