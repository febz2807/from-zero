def app_tebak_angka():
    import random
    angka_acak = random.randint(1, 10)
    maksimal_tebakan = 3
    tebakan = 0
    while tebakan < maksimal_tebakan:
        tebakan += 1
        angka_user = int(input("Masukkan angka: "))
        if angka_user > angka_acak:
            print("Angka terlalu besar")
        elif angka_user < angka_acak:
            print("Angka terlalu kecil")
        else:
            print("Selamat, Angka benar")
            break
    else:
        print("Kamu telah melewati maksimal tebakan anda")
        print("Angka acak adalah", angka_acak)


def app_menu():
    while True:
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")
        print("1. Tebak Angka")
        print("2. Keluar")
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")

        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            app_tebak_angka()
        elif pilihan == 2:
            print("=== PROGRAM SELESAI ===")
            break
        else:
            print("Error: Pilihan tidak valid")


app_menu()