def ambil_soal():
    soal_asli = []
    with open("bank_soal.txt","r") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli

def buat_soal():
    soal_asli = ambil_soal()

    #acak soal
    import random
    random.shuffle(soal_asli)

    soal_ujian = []
    for i in range(10):
        soal = soal_asli[i]
        data = soal.split(",")

        pertanyaan = data[0]
        semua_jawaban = data[1]

        jawaban = semua_jawaban.split(",")
        jawaban_benar = jawaban[0]

        # acak jawaban
        random.shuffle(jawaban)

        soal_ujian.append({
            "pertanyaan": pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar
        })

    return soal_ujian

def app_ujian():
    soal_ujian = buat_soal()
    opsi = ["A", "B", "C", "D"]
    for i in range(len(soal_ujian)):
        soal = soal_ujian[i]
        print("Pertanyaan", i + 1, ":", soal["pertanyaan"])
        print("Jawaban:")
        for j in range(len(soal["jawaban"])):
            jawaban = soal["jawaban"] [j]
            print(opsi[j], ".", jawaban)

app_ujian()