# Penjualan tiket event
class Tiket:
    def __init__(self, nama_event, harga):
        self.nama_event = nama_event
        self.harga = harga

class Transaksi:
    def __init__(self, tiket, jumlah):
        self.tiket = tiket
        self.jumlah = jumlah
        self.total = tiket.harga * jumlah

    def cetak_detail(self):
        print("\n===== DETAIL TRANSAKSI =====")
        print(f"Event        : {self.tiket.nama_event}")
        print(f"Harga Tiket  : {self.tiket.harga}")
        print(f"Jumlah       : {self.jumlah}")
        print(f"Total Bayar  : {self.total}")
        print('============================')

# Membuat 3 objek tiket
t1 = Tiket("Konser Musik", 150000)
t2 = Tiket("Seminar AI", 100000)
t3 = Tiket("Festival Kuliner", 50000)

# Daftar event
print("=== PILIH EVENT ===")
print("1.", t1.nama_event, "-Rp", t1.harga)
print("2.", t2.nama_event, "-Rp", t2.harga)
print("3.", t3.nama_event, "-Rp", t3.harga)

pilih = int(input("Pilih event 1-3: "))

# Menentukan tiket yang dipilih
if pilih == 1:
    tiket_dipilih = t1
elif pilih == 2:
    tiket_dipilih = t2
elif pilih == 3:
    tiket_dipilih = t3
else:
    print("Pilihan tidak valid!")
    exit()

jumlah = int(input("Masukkan jumlah tiket: "))

# Membuat transaksi
transaksi = Transaksi(tiket_dipilih, jumlah)

# Cetak detail transaksi
transaksi.cetak_detail()