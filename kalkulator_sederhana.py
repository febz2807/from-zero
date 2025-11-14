print("=== KALKULATOR SEDERHANA ===")
print("Operasi + - * / // % **")

angka1 = float(input("Masukkan angka pertama: "))
operasi = input("Masukkan operasi (+, -, *, /, //, %, **)")
angka2 = float(input("Masukkan angka kedua: "))

if operasi == "=":
    hasil = angka1 + angka2
elif operasi == "-":
    hasil = angka1 - angka2
elif operasi == "*":
    hasil = angka1 * angka2
elif operasi == "/":
    hasil = angka1 / angka2
elif operasi == "//":
    hasil = angka1 // angka2
elif operasi == "%":
    hasil = angka1 % angka2
elif operasi == "**":
    hasil = angka1 ** angka2

else:
    print("Hasil tidak ditemukan")

print("hasil:", hasil)

print("=== JAM KALKULATOR ===")
import datetime
now = datetime.datetime.now()
print("Perhitungan dilakukan pada:", now)