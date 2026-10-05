import platform
import socket
import os
import psutil


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

sys_info = get_sys_info()
cpu_info = get_cpu_info()
memory_info = get_memory_info()


print("SYSTEM INFORMATION")
print("------------------")
print(f"OS           : {sys_info['os']}")
print(f"Architecture : {sys_info['architecture']}")
print(f"Processor    : {sys_info['processor']}")
print(f"Hostname     : {sys_info['hostname']}")

print()
print("CPU INFORMATION")
print("----------------")
print(f"CPU Count    : {cpu_info['CPU count']}")
print(f"CPU Usage    : {cpu_info['CPU usage']}%")

print()
print("MEMORY INFORMATION")
print("------------------")
print(f"Total     : {bytes_to_gb(memory_info['total']):.2f} GB")
print(f"Used      : {bytes_to_gb(memory_info['used']):.2f} GB")
print(f"Available : {bytes_to_gb(memory_info['available']):.2f} GB")
print(f"Usage     : {memory_info['percentage']}%")