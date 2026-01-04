class Kampus:
    nama = ""
    alamat = ""

class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

kampus1 = Kampus()
print(kampus1.alamat)
print(kampus1.nama)


#instance attribute
mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 12345
mahasiswa1.nama = "eko"
mahasiswa1.perkenalan()

print(mahasiswa1.nim)
print(mahasiswa1.nama)

kampus2 = Kampus()

mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 12345
mahasiswa2.nama = "Budi"
mahasiswa2.perkenalan()

print(mahasiswa2.nim)
print(mahasiswa2.nama)
