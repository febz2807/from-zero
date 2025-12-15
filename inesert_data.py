import sqlite3

conn = sqlite3.connect("event.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO tiket (nama_event, harga) VALUES (?, ?)",
                ("Konser Noah", 150000))

conn.commit()
conn.close()

print("Data nerhasil ditambahkan")