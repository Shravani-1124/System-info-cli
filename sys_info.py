
import platform
import socket
import os
import psutil
import time
import argparse
import json


# ---------------- SYSTEM INFORMATION ----------------

def get_sys_info():
    sys_info = {
        "os": platform.system(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "hostname": socket.gethostname()
    }

    return sys_info


# ---------------- CPU INFORMATION ----------------

def get_cpu_info():
    cpu_info = {
        "CPU count": os.cpu_count(),
        "CPU usage": psutil.cpu_percent(interval=1)
    }

    return cpu_info


# ---------------- MEMORY INFORMATION ----------------

def get_memory_info():
    memory = psutil.virtual_memory()

    memory_info = {
        "total": memory.total,
        "used": memory.used,
        "available": memory.available,
        "percentage": memory.percent
    }

    return memory_info


def bytes_to_gb(bytes_value):
    return bytes_value / (1024 ** 3)


# ---------------- DISK INFORMATION ----------------

def get_disk_info():
    disk = psutil.disk_usage("/")

    disk_info = {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percentage": disk.percent
    }

    return disk_info


# ---------------- NETWORK INFORMATION ----------------

def get_network_info():
    hostname = socket.gethostname()
    local_ip = "Unavailable"

    try:
        with socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        ) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]

    except OSError:
        pass

    network_info = {
        "hostname": hostname,
        "local_ip": local_ip
    }

    return network_info


# ---------------- UPTIME ----------------

def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()

    return current_time - boot_time


def format_uptime(seconds):
    days = int(seconds // (24 * 60 * 60))
    hours = int((seconds % (24 * 60 * 60)) // (60 * 60))
    minutes = int((seconds % (60 * 60)) // 60)
    seconds = int(seconds % 60)

    return f"{days}d {hours}h {minutes}m {seconds}s"


# ---------------- DISPLAY FUNCTIONS ----------------

def display_sys_info(sys_info):
    print("SYSTEM INFORMATION")
    print("------------------")
    print(f"OS           : {sys_info['os']}")
    print(f"Architecture : {sys_info['architecture']}")
    print(f"Processor    : {sys_info['processor']}")
    print(f"Hostname     : {sys_info['hostname']}")


def display_cpu_info(cpu_info):
    print("CPU INFORMATION")
    print("----------------")
    print(f"CPU Count : {cpu_info['CPU count']}")
    print(f"CPU Usage : {cpu_info['CPU usage']}%")


def display_memory_info(memory_info):
    print("MEMORY INFORMATION")
    print("------------------")
    print(f"Total     : {bytes_to_gb(memory_info['total']):.2f} GB")
    print(f"Used      : {bytes_to_gb(memory_info['used']):.2f} GB")
    print(f"Available : {bytes_to_gb(memory_info['available']):.2f} GB")
    print(f"Usage     : {memory_info['percentage']}%")


def display_disk_info(disk_info):
    print("DISK INFORMATION")
    print("----------------")
    print(f"Total : {bytes_to_gb(disk_info['total']):.2f} GB")
    print(f"Used  : {bytes_to_gb(disk_info['used']):.2f} GB")
    print(f"Free  : {bytes_to_gb(disk_info['free']):.2f} GB")
    print(f"Usage : {disk_info['percentage']}%")


def display_network_info(network_info):
    print("NETWORK INFORMATION")
    print("-------------------")
    print(f"Hostname   : {network_info['hostname']}")
    print(f"Local IPv4 : {network_info['local_ip']}")


def display_uptime():
    uptime = get_uptime()

    print("UPTIME")
    print("------")
    print(f"Uptime : {format_uptime(uptime)}")


# ---------------- FULL REPORT ----------------

def display_full_report():
    display_sys_info(get_sys_info())

    print()
    display_cpu_info(get_cpu_info())

    print()
    display_memory_info(get_memory_info())

    print()
    display_disk_info(get_disk_info())

    print()
    display_network_info(get_network_info())

    print()
    display_uptime()


def collect_all_info():
    return {
        "system": get_sys_info(),
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "network": get_network_info(),
        "uptime": format_uptime(get_uptime())
    }



def main():
    parser = argparse.ArgumentParser(
        description="System information CLI"
    )

    parser.add_argument(
        "--cpu",
        action="store_true",
        help="Display CPU information"
    )

    parser.add_argument(
        "--memory",
        action="store_true",
        help="Display memory information"
    )

    parser.add_argument(
        "--disk",
        action="store_true",
        help="Display disk information"
    )

    parser.add_argument(
        "--network",
        action="store_true",
        help="Display network information"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Display information in JSON format"
    )
    parser.add_argument(
        "--system",
        action="store_true",
        help="Display system information"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="sysinfo 1.0.0"
    )
    args = parser.parse_args()

    # Collect only the requested sections.
    sections = {}

    if args.cpu:
        sections["cpu"] = get_cpu_info()

    if args.memory:
        sections["memory"] = get_memory_info()

    if args.disk:
        sections["disk"] = get_disk_info()

    if args.network:
        sections["network"] = get_network_info()

    # If no section is selected, collect the full report.
    if not sections:
        sections = collect_all_info()

    # JSON output
    if args.json:
        print(json.dumps(sections, indent=4))
        return

    # Normal, human-readable output
    if args.cpu:
        display_cpu_info(sections["cpu"])

    if args.memory:
        display_memory_info(sections["memory"])

    if args.disk:
        display_disk_info(sections["disk"])

    if args.network:
        display_network_info(sections["network"])

    if not (args.cpu or args.memory or args.disk or args.network):
        display_full_report()

    if args.system:
        display_sys_info(get_sys_info())

if __name__ == "__main__":
    main()
