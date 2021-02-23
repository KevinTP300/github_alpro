#Kevin Triantama Prayitno | 71180300
#Universitas Kristen Duta Wacana Yogyakarta
#ada code yang saya tambahi seperti apabila nilai IPK lebih dari 4

print("Buatlah program pengecekan IPK untuk menentukan kelulus, minimin IPK untuk lulus adalah 2.7 dan bila lulus beri range Gradenya.")
try:
    standar = 2.6
    nama = input("Nama mahasiswa: ")
    nilai_ipk = float(input("Masukan IPK anda (0.0 - 4.0): "))

    if nilai_ipk > standar:
        if nilai_ipk == 4:
            print("Selamat %s kamu lulus dengan nilai sempurna: A" %(nama))
        elif nilai_ipk > 4:
            print("pakai kekuatan orang dalam")
        elif nilai_ipk >= 3.7:
            print("Selamat %s kamu lulus dengan nilai membanggakan: A-" %(nama))
        elif nilai_ipk >= 3.3:
            print("%s kamu lulus dengan nilai yang baik: B+" %(nama))
        elif nilai_ipk >= 3:
            print("%s kamu lulus dengan nilai cukup baik: B" %(nama))
        elif nilai_ipk >= standar:
            print("%s kamu lulus dengan nilai standar: B-" %nama)
    elif nilai_ipk <= standar:
        print("%s kamu perlu pendalaman kuliah lagi" %(nama))
except:
    print("inputan salah")
