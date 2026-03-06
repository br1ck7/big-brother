from scanner import scan_network
from config import POLL_INTERVAL, NETWORK_RANGE, DATABASE_PATH
import sqlite3, database

def check_status(ip_address):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM devices WHERE ip_address=?", (ip_address,))
    result = cursor.fetchone()

    return result[0] if result else None

def update_device():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    ip_address = ""
    status = "online"
    last_seen = ""
    last_changed = ""

    devices = scan_network(NETWORK_RANGE)

    device_list = []
    for device in devices:
        device_list.append(str(device))

    for ip in device_list:

        cursor.execute("""
                   INSERT OR REPLACE INTO devices (ip_address, status, last_seen, last_changed)
                   VALUES
                   (?, ?, ?, CURRENT_TIMESTAMP)
                   """, (ip, status, last_seen,))
    
    conn.commit()
    conn.close()
    
update_device()