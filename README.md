# Basic Network Scanner

A simple network scanner that checks for open ports on a range of IP addresses. 

## Features

- Scans specified IP addresses for open ports
- Displays whether the port is open or closed

## Usage

1. Modify the ip_range list in network_scanner.py with the IP addresses you want to scan.
2. Set the desired port number/s in the port variable, or use the default seven ports: 80, 443, 22, 21, 25, 3306, 3389
3. Run the script:

```sh
python network_scanner.py
