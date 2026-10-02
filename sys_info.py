import platform
import socket


def get_sys_info():
    opsys = platform.system()
    architecture = platform.machine()
    processor = platform.processor()
    hostname = socket.gethostname()

    sys_info = {
        "os": opsys,
        "architecture": architecture,
        "processor": processor,
        "hostname" : hostname
    }

    return sys_info

sys_info = get_sys_info()

print("SYSTEM INFORMATION")
print("------------------")
print(f"OS           : {sys_info['os']}")
print(f"Architecture : {sys_info['architecture']}")
print(f"Processor    : {sys_info['processor']}")
print(f"Hostname     : {sys_info['hostname']}")


