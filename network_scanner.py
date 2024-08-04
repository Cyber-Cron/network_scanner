import socket

def scan_network(ip_range, ports):
    """
    Scan the specified IP range for open ports.
    """
    for ip in ip_range:
        print(f"Scanning IP: {ip}")
        for port in ports:
            try:
                # Create a socket object
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                
                # Attempt to connect to the IP address and port
                result = sock.connect_ex((ip, port))
                
                if result == 0:
                    print(f"Port {port} is open on {ip}")
                else:
                    print(f"Port {port} is closed on {ip}")
                
                # Close the socket
                sock.close()
            
            except Exception as e:
                print(f"Error scanning {ip}:{port} - {e}")

if __name__ == "__main__":
    # Define a list of IP addresses to scan
    ip_range = ['192.168.1.1', '192.168.1.2', '192.168.1.10']
    # Define a list of ports to scan
    ports = [80, 443, 22, 21, 25, 3306, 3389]
    scan_network(ip_range, ports)

