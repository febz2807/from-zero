#password_benar = "python123"
#percobaan = 0
#max_perrcobaan = 3 

#while percobaan < max_perrcobaan:
 #   password = input("Masukkan password: ")
  #  percobaan += 1

   # if password == password_benar:
        #print("Login berhasil!")
    #    break
    #else:
#        print("Paswword salah. Sisa percobaan:", max_perrcobaan - percobaan)
#else:
 #   print("Terlalu banyak percobaan gagal. Akses Di Tolak")

daftar_kosong = []
print(daftar_kosong)

angka = [ 1, 2, 3, 4, 5]
print(angka)

nama = ["Alice", "Bob", "CHarlie"]
print(nama)

campuran = ["alice", 25, "Bob", 30]
print(campuran)

buah = ["apel", "jeruk", "mangga"]
print(buah[0])
print(buah[1])
print(buah[2])

warna = ["merah", "orange", "hijau"]
print(warna)
warna[1] = "kuning"
print(warna)

buah = ["appel", "jeruk"]
print(buah)
buah.append("durian")
print(buah)
buah.insert(1, "naga")
print(buah)

buah.remove("jeruk")
print(buah)

buah.pop()
print(buah)

del buah[0]
print(buah)

buah = ["apel", "jeruk", "mangga"]
print(len(buah))

satu = [1,2,3,4,5]
print(satu)
dua = [6,7,8,9,10]
print(dua)

gabungan = satu + dua
print(gabungan)

banyak_buah = ["apel", "jeruk", "mangga", "durian"]
for buah in banyak_buah:
    print(buah)

for i in range(0, len(banyak_buah)):
    print(banyak_buah[i])

if "salak" in banyak_buah:
    print("ada salak")
else:
    print("tidak ada salak")

point = (5, 10)
print(point)
print(point[0])
print(point[1])