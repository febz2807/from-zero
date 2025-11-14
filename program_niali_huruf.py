print("=== PROGRAM PENENTU NILAI HURUF ===")
nilai = int(input("Masukkan nilai kamu (0-100): "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid!")
elif nilai >= 95 and 100:
    grade = ("A+")
elif nilai >= 90 and 94:
    grade = ("A")
elif nilai >= 85 and 89:
    grade = ("B+")
elif nilai >= 75 and 80:
    grade = ("B")
elif nilai >= 65 and 70:
    grade = ("C+")
elif nilai >= 55 and 60:
    grade = ("C")
else:
    grade = ("E")

print(f"Nilai kamu: {nilai}")
print(f"Grade: {grade}")

# Waktu
print("=== WAKTU PERHITUNGAN DILAKUKAN ===")
import datetime
now = datetime.datetime.now()
print("Perhitungan dilakukan pada:", now)
