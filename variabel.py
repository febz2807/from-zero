nama = "Febryanto"
umur = 21
tinggi = 1.75
mahasiswa = True

# ======= HASIL =======
print(type(nama))  # <class 'str'>
print(type(umur))  # <class 'int'>
print(type(tinggi)) # <class 'float'>
print(type(mahasiswa)) # <class 'bool'>

a = 10
b = 3
print ("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian Bulat:", a // b)
print("Sisa Bagi:", a % b)
print("Pangkat:", a ** b)

print("# ============= HASIL ===========")

nama = input("Masukkan nama kamu: ")
umur = int(input("Masukkan umur kamu: "))
tinggi = float(input("Masukkan tinggi kamu (m): "))

print(f"halo {nama}, umurmu {umur} tahun, tinggi {tinggi} meter.")

# Oprasi Matematika
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

print("Hasil Penjumlahan:", a + b)
print("Hasil Pengurangan:", a - b)
print("Hasil Perkalian:", a * b)
print("Hasil Pembagian:", a / b)
print("Sisa bagi:", a % b)


# Menggabungkan String
nama = input("Masukkan nama kamu: ")
hobi = input("Masukkan hobi kamu: ")

print("halo " + nama + ", kamu suka " + hobi)

import datetime
now = datetime.datetime.now()
print("Perhitungan dilakukkan pada:", now)