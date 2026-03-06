import ipaddress
from ping3 import ping
from config import NETWORK_RANGE

def scan_network(network_range):
    network = ipaddress.ip_network(network_range)
    address_list = []

    for ip in network.hosts():
        try:
            result = ping(str(ip), timeout=2)
            if result:
                print(f"{ip} responded in {result} seconds")
                address_list.append(ip)
        except Exception as e:
            print(f"Error pinging {ip}: {e}")

    return address_list

if __name__ == "__main__":
    scan_result = scan_network(NETWORK_RANGE)
    print(scan_result)