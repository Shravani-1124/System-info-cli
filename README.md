
# System Information CLI

A Python-based command-line tool that displays essential system information, including CPU usage, memory, disk space, network details, and system uptime.

## Features

- Operating system and architecture information
- CPU count and usage
- Memory usage and availability
- Disk space information
- Hostname and local IPv4 address
- System uptime
- Command-line options to select specific information
- JSON output for programmatic use
- Help and version options

## Requirements

- Python 3
- psutil

## Installation

Clone the repository:

```bash
git clone https://github.com/Shravani-1124/System-info-cli.git
cd System-info-cli
```

Install the dependency:

```bash
python3 -m pip install psutil
```

## Usage

Display the full system report:

```bash
python3 sys_info.py
```

Display specific information:

```bash
python3 sys_info.py --system
python3 sys_info.py --cpu
python3 sys_info.py --memory
python3 sys_info.py --disk
python3 sys_info.py --network
```

Display JSON output:

```bash
python3 sys_info.py --json
python3 sys_info.py --json --cpu
```

Other options:

```bash
python3 sys_info.py --help
python3 sys_info.py --version
```

## Technologies

- Python
- argparse
- psutil
- socket
- platform
- json

## Learning Outcomes

- Python functions and dictionaries
- Operating system information retrieval
- Command-line argument parsing
- Network information using sockets
- JSON serialization
- Python standard library modules
