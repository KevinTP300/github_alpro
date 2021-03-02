#Kevin Triantama Prayitno | 71180300
#Universitas Kristen Duta Wacana

print("Buatlah program penjumlahan, pengurangan, perkalian dan pembagian\n")

def kalkulator(a, b, pilihan):
    hasil = 0
    if pilihan == 1:
        hasil = a + b
    elif pilihan == 2:
        hasil = a - b
    elif pilihan == 3:
        hasil = a * b
    elif pilihan == 4:
        hasil = a / b
    else:
        print("ga ada yoi")
    return hasil

a = int(input("Masukan angka pertama: "))
b = int(input("Masukan angka kedua: "))
print("Pilih lah\n1. Tambah\n2. Kurang\n3. Kali\n4. Bagi")
try:
    pilihan = int(input("Pilihan anda: "))
    print("Hasilnya: ", kalkulator(a, b, pilihan))
except:
    print("input yang bener dong")