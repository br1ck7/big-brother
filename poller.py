from scanner import scan_network
from config import POLL_INTERVAL, NETWORK_RANGE, DATABASE_PATH
import sqlite3, database

def check_status(ip_address):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM devices WHERE ip_address=?", (ip_address,))
    result = cursor.fetchone()

    return result[0] if result else None