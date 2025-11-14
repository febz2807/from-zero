# Latihan
nama = input("Masukkan nama anda: ")
npm = input("Masukkan nomor npm anda: ")
kelas = input("Masukkan kelas anda: ")
alamat = input("Masukkan alamat lengkap anda: ")

print(f"halo saya {nama},nomor npm saya {npm}, kelas {kelas}, saya tinggal di {alamat}")

# Kalkulator sederhana
print("=== KALKULATOR SEDERHANA ===")
print("Operasi + - * /")

angka1 = float(input("Masukkan angka pertama: "))
operasi = input("Masukkan operasi (+ - * /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operasi == "+":
    hasil = angka1 + angka2
elif operasi == "-":
    hasil = angka1 - angka2
elif operasi == "*":
    hasil = angka1 * angka2
elif operasi == "/":
    hasil = angka1 / angka2

else:
    print("Hasil tidak ditemukan")

print("Hasil", hasil)

import datetime
now = datetime.datetime.now()
print("Perhitungan dilakukan pada:", now)


# Menggabungkan string
nama = input("Masukkan nama kamu: ")
hobi = input("Masukkan hobi kamu: ")

print("halo " + nama + ", kamu suka " + hobi)