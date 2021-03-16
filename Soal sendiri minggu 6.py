#Kevin Triantama Prayitno | 71180300
#Universitas Kristen Duta Wacana
#REF: https://www.petanikode.com/python-perulangan/

print("Membuat perulangan terus menerus sampai memilih untuk keluar")

jumlah = 0
while True:
    
    jawab = input("Mau diulang (ya/tidak)? ")
    if jawab == "ya":
        jumlah += 1
        print()
    else:
        if jawab == "tidak":
            print()
            break
        else:
            print("bukan jawaban (ya/tidak)")

print("Jumlah perulangan: ", jumlah)