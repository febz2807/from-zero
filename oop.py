# CLASS & OBJECT
class Manusia:
    nama = "Tidak ada nama"

# membuat object
orang = Manusia()
print(orang.nama)


#Constructor (init)
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

orang1 = Manusia("Febry", 20)

print(orang1.nama)
print(orang1.umur)

# Method (fungsi di dalam kelas)
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    
    def info(self):
        print("Mobil", self.merk, "warnanya", self.warna)

m1 = Mobil("Honda", "Merah")
m1.info()

# Encapsulation (Private attribute)
class Bank:
    def __init__(self, saldo):
        self.__saldo = saldo # private

    def lihat_saldo(self):
        print("Saldo:", self.__saldo)

akun = Bank(500000)
akun.lihat_saldo()

# Inheritance (Pewarisan)
class Hewan:
    def suara(self):
        print("Hewan bersuara")

class Kucing(Hewan):
    def suara(self):
        print("Meong")

k = Kucing()
k.suara()


# POLYMORPHISM
class Burung:
    def suara(self):
        return "Cuit"

class Ayam:
    def suara(self):
        return "kukuruyuk"

def cetak_suara(hewan):
    print(hewan.suara())

cetak_suara(Burung())
cetak_suara(Ayam())