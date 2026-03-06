import sqlite3
from config import DATABASE_PATH

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT UNIQUE NOT NULL,
            status TEXT DEFAULT 'unknown',
            last_seen TIMESTAMP,
            last_changed TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()