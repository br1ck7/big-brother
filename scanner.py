import ipaddress
from ping3 import ping
from config import NETWORK_RANGE

def scan_network(network_range):
    network = ipaddress.ip_network(network_range)
    for ip in network.hosts():
        result = ping(str(ip))
        if result:
            print(f"{ip} responded in {result} seconds")

scan_network(NETWORK_RANGE)