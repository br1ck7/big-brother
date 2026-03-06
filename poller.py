from scanner import scan_network
from config import POLL_INTERVAL, NETWORK_RANGE, DATABASE_PATH
import sqlite3, database, datetime

def check_status(ip_address):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM devices WHERE ip_address=?", (ip_address,))
    result = cursor.fetchone()

    return result[0] if result else None

def update_device(ip_address, status):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
     
    last_seen = datetime.now()
    last_changed = datetime.now()

    cursor.execute("""
                   INSERT OR REPLACE INTO devices (ip_address, status, last_seen, last_changed)
                   VALUES
                   (?, ?, ?, ?)
                   """,
                   (ip_address, status, last_seen, last_changed)
                   )
    
    conn.commit()
    conn.close()

def poll_network():
    while True:
        devices = scan_network(NETWORK_RANGE)
        for device in devices:
            ip_address = str(device)
            status = "online" if check_status(ip_address) == "offline" else "offline"
            update_device(ip_address, status)

        datetime.time.sleep(POLL_INTERVAL)

if __name__ == "__main__":   
    poll_network()