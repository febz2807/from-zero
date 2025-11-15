print("=== PENGAMBILAN NILAI ===")
nilai = int(input("Masukkan nilai (0-100): "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid!")
elif nilai >= 95 and 100:
    grade = ("A+")
    komentar = ("Luar biasa!")
elif nilai >= 85 and 90:
    grade = ("A")
    komentar = ("Sangat baik")
elif nilai >= 75 and 80:
    grade = ("B+")
    komentar = ("Cukup baik")
elif nilai >= 65 and 70:
    grade = ("B")
    komentar = ("cukup")
elif nilai >= 55 and 60:
    garde = ("C")
    komentar = ("Kurang baik")
else:
    grade = ("E")
    komentar = ("Mengulang")

print(f"Nilai kamu: {nilai}")
print(f"Grade: {grade}")
print(f"Komentar: {komentar}")

print("=== TANGGAL NILAI DICATAT ===")
import datetime
now = datetime.datetime.now()
print("Perhitungan dilakukan pada:", now)