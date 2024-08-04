import socket

def scan_network(ip_range, port):
	"""
	Scan the specified IP range for open ports.
	"""
	for ip in ip_range:
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
			print(f"Error scanning {ip}: {e}")

if __name__ == "__main__":
	# Define a list of IP addresses to scan (e.g., '192.168.1.1', '192.168.1.2')
	ip_range = ['192.168.1.1', '192.168.1.2']
	# Define the port to scan
	port = 80
	scan_network(ip_range, port)
