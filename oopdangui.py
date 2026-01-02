import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# --- DATABASE OOP ---
class DatabasePasien:
    def __init__(self, db="klinik.db"):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pasien(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT,
                umur INTEGER,
                alamat TEXT,
                jk TEXT
            )
        """)
        self.conn.commit()

    def tambah(self, nama, umur, alamat, jk):
        self.cursor.execute("INSERT INTO pasien(nama, umur, alamat, alamat, jk) VALUES(?,?,?,?)",
                            (nama, umur, alamat, jk ))
        self.conn.commit()

    def tampilkan(self):
        self.cursor.execute("SELECT * FROM pasien")
        return self.cursor.fetchall()

    def update(self, id, nama, umur, alamat, jk):
        self.cursor.execute("UPDATE pasien SET nama=?, alamat=?, jk=? WHERE id=?",
                            (nama, umur, alamat, jk, id))
        self.conn.commit()

    def hapus(self, id):
        self.cursor.execute("DELETE FROM pasien WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# --- GUI TKINTER ---
db = DatabasePasien()

root = tk.Tk()
root.title("Manajemen Pasien Klinik")
root.geometry("700x500")

# Frame input
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nama").grid(row=0, column=0)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=0, column=1)

tk.Label(frame_input, text="Umur").grid(row=1, column=0)
entry_umur = tk.Entry(frame_input)
entry_umur.grid(row=1, column=1)

tk.Label(frame_input, text = "Alamat").grid(row=2, column=0)
entry_alamat = tk.Entry(frame_input)
entry_alamat.grid(row=2, column=1)

tk.Label(frame_input, text="Jenis Kelamin").grid(row=3, column=0)
combo_jk = ttk.Combobox(frame_input, values=["Laki-laki", "Perempuan"])
combo_jk.grid(row=3, column=1)


# Tabel pasien
table = ttk.Treeview(root, columns=("ID", "Nama", "Umur", "Alamat","JK"), show="headings")
for col in ("ID","Nama","Umur","Alamat","JK"):
    table.heading(col, text=col)
table.pack(fill="both", expand=True, pady=10)

def refresh_table():
    for item in table.get_children():
        table.delete(item)
    for row in db.tampilkan():
        table.insert("", "end", values=row)

# Fungsi CRUD GUI
def tambah_pasien():
    try:
        nama = entry_nama.get().strip()
        umur_text = entry_umur.get().strip()
        alamat = entry_alamat.get().strip()
        jk = combo_jk.get()

        if umur_text == "":
            messagebox.showerror("Error", "Umur harus berupa angka!")
            return
        
        if not umur_text.isdigit():
            messagebox.showerror("Error", "Umur harus berupa angka!")
            return
        
        umur = int(umur_text)


        db.tambah(nama, umur, alamat, jk)
        messagebox.showinfo("Berhasil", "Pasien Ditambahkan")
        clear_form()
        refresh_table()
    except:
        messagebox.showerror("Error", "Umur harus angka!")

def update_pasien():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Pilih Data", "Pilih pasien di tabel!")
        return
    id = table.item(selected[0])['values'][0]
    db.update(id, entry_nama.get(), int(entry_umur.get()), entry_alamat.get, combo_jk.get())
    messagebox.showinfo("Berhasil", "Data pasien diupdate")
    refresh_table()

def hapus_pasien():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Pilih Data", "Pilih pasien di tabel!")
        return
    id = table.item(selected[0])['values'][0]
    db.hapus(id)
    messagebox.showinfo("Berhasil", "Pasien dihapus")
    refresh_table()

def clear_form():
    entry_nama.delete(0, tk.END)
    entry_umur.delete(0, tk.END)
    entry_alamat.delete(0, tk.END)
    combo_jk.set("")

# Tombol
frame_btn = tk.Frame(root)
frame_btn.pack()

tk.Button(frame_btn, text="Tambah", command=tambah_pasien).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Update", command=update_pasien).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Hapus", command=hapus_pasien).grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="Clear", command=clear_form).grid(row=0, column=3, padx=5)
tk.Button(frame_btn, text="Exit", command=root.destroy).grid(row=0, column=4, padx=5)

refresh_table()
root.mainloop()
