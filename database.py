import sqlite3

conn = sqlite3.connect("event.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS TIKET(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_event TEXT,
    harga INTEGER
)
""")

conn.commit()
conn.close()

print("Tabel tiket berhasil dibuat")