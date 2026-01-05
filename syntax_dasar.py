#nama = input("Masukkan Nama Anda: ")
#umur = input("Masukkan Umur Anda: ")

#umur = 10
#
#if umur >= 17 and punya_ktp:
    #print("Umur Anda Sudah Cukup ")
#else:
    #print("Umur Anda Belum Cukup")


#angka1 = float(input("Masukkan Angka Pertama: "))
#operasi = input("Masukkan Operasi +, -, *, /: ")
#angka2 = float(input("Masukkan Angka Kedua: "))

#if operasi == "+":
   #hasil = angka1 + angka2
#elif operasi == "-":
    #hasil = angka1 - angka2
#elif operasi == "*":
    #hasil = angka1 * angka2
#elif operasi == "/":
    #hasil = angka1 / angka2
#else:
    #print("Angka Tidak Valid")

#print("Jumlah Perhitungan:", hasil)

print("=== Pengambilan Nilai ===")
nilai = int(input("Masukkan Nilai 0-100: "))

if nilai < 0 or nilai > 100:
    print("Nilai Tidak Valid")
elif nilai >= 95 and 100:
    grade = print("A+")
    komentar = print("Luar Biasa")
elif nilai >= 85 and 90:
    grade = print("A")
    komentar = print("Tingkatkan Lagi")
elif nilai >= 75 and 80:
    grade = print("B+")
    komentar = print("Cukup")
elif nilai >= 70 and 75:
    grade = print("C")
    komentar = print("Mengulang")
else:
    print("E")
    print("Mengulang")

print(f"Nilai Anda: {nilai}")
print(f"Grade Anda: {grade}")
print(f"komentar: {komentar}")