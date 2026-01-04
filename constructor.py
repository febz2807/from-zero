class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nim , nama):
        self.nim = nim
        self.nama = nama

mhs = Mahasiswa(123456, "Arya")

print(mhs.nim)
print(mhs.nama)


class BankAccount:
    no = ""
    saldo = 0

def __init__(self, no, saldo =0):
    if saldo < 0:
        raise ValueError("Saldo haarus positif")
    
    self.no = no
    self.saldo = saldo

eko = BankAccount("123456789", 10000000)
#budi = BankAccount("123456789", -1000000)
