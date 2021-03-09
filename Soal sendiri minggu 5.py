#Kevin Triantama Prayitno | 71180300
#UniversitaS Kristen Duta Wacana

while True:
    print("Daftar Menu\n1. makan\n2. minum\n3. belanja\n4. jalan\n5. exit/keluar")
    pilihan = int(input("Piihan anda: "))
    if pilihan == 1:
        opsi = input("Mau makan apa: ")
        jumlah = int(input("Mau berapa banyak: "))
        print("mau makan %s dengan jumlah %d sudah dicatat." %(opsi, jumlah))
    elif pilihan == 2:
        opsi = input("mau minum apa: ")
        print("pesanan %s anda telah dicatat." %(opsi))
    elif pilihan == 3:
        opsi = input("mau beli apa: ")
        jumlah = int(input("berapa banyak: "))
        print("anda beli %s dengan jumlah %d sudah dicatat." %(opsi, jumlah))
    elif pilihan == 4:
        opsi = input("mau jalan kemana: ")
        print("anda telah pesan tempat ke %s" %(opsi))
    elif pilihan == 5:
        break
    else:
        print("pilihan ga ada.")