from database import init_db
from scanner import scan_network
from config import NETWORK_RANGE

if __name__ == "__main__":
    init_db()
    devices = scan_network(NETWORK_RANGE)
    print(f"Found {len(devices)} devices")
    for device in devices:
        print(device)