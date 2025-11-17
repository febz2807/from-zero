class Mahasiswa:
    def __init__(self, npm, nama, prodi):
        self.npm = npm
        self.nama = nama
        self.prodi = prodi

    def tampilkan(self):
        print(f"NPM: {self.npm}")
        print(f"Nama: {self.nama}")
        print(f"Prodi: {self.prodi}")

class DatabaseMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self, mhs):
        self.data.append(mhs)

    def tampilkan_semua(self):
        for m in self.data:
            print("----------------")
            m.tampilkan()

# penggunaan
db = DatabaseMahasiswa()

m1 = Mahasiswa("202243500473", "Febryanto Nugroho", "Teknik Informatika")
m2 = Mahasiswa("2022000111111", "Budi", "Sistem Informasi")
m3 = Mahasiswa("2022435004728", "Rifai", "Ilmu Komunikasi")

db.tambah(m1)
db.tambah(m2)
db.tambah(m3)

db.tampilkan_semua()


# Sistem penujalan tiket
class Tiket:
    def __init__(self, konser, harga, nama):
        self.konser = konser
        self.harga = harga
        self. nama = nama
    
    def tampilkan(self):
        print(f"Konser: {self.konser}")
        print(f"Harga: {self.harga}")
        print(f"Nama: {self.nama}")

class Transaksi:
        print(input("Masukkan Jmlah Tiket: "))
