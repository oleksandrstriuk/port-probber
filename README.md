# PortProbber

PortProbber prototype is a Python script for scanning a range of ports on a target host to identify open ports. It uses the socket module to establish TCP connections and provides feedback on the status of each port. 

## Features

- Scan a range of ports on a specified target host
- Identify open ports

## Usage

1. Clone the repository.

2. Navigate to the directory.

3. Run the script with the following command, specifying the target host and port range:

`python port_scan.py target_host start_port end_port`

Replace `target_host` with the IP address or domain name of the target host, `start_port` with the starting port of the scan, and `end_port` with the ending port of the scan.

## Example

python port_scan.py example.com 1 100

This will scan ports 1 to 100 on the host example.com.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
