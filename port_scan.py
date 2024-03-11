import socket # Import the socket module to enable network communication.

def port_scan(target_host, start_port, end_port):
    """
    Scan a range of ports on a specified target host for open ports.

    Args:
        target_host (str): The target host to scan. Can be a domain name or an IP address.
        start_port (int): The starting port of the scan (inclusive).
        end_port (int): The ending port of the scan (inclusive).

    Returns:
        None

    Prints:
        Port status messages indicating whether each port in the specified range is open or closed.
    """
    try:
        target_ip = socket.gethostbyname(target_host)  # Convert domain name to IP address if needed.
    except socket.gaierror:
        print("Invalid target IP or domain")
        return

    print(f"Scanning target: {target_host} ({target_ip})")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for connection attempt.
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Example usage:
target_host = "primalbitmedia.com" # Specify the target host (domain name or IP address).
start_port = 1 # Specify the starting port of the scan.
end_port = 100 # Specify the ending port of the scan.

port_scan(target_host, start_port, end_port) # Call the function to perform the port scan.
