print("Soal\nAnda disuruh memasukan gaji bulanan selama sebulan, setiap bulan 10% dari gaji anda gunakan untuk persepuluhan.\ndari sisa uang 50% digunakan untuk kebutuhan sehari-hari dan 30% anda gunakan untuk kebutuhan tidak terduga, lalu dari sisa uang yang tersisa anda gunakan tabungan.")

gaji = int(input("Masukan gaji bulan ini: "))
persepuluhan = (gaji * 10) /100

gaji_terkini = gaji - persepuluhan
kebutuhan_seharihari = (gaji_terkini * 50) / 100
kebutuhan_takterduga = (gaji_terkini * 30) / 100
sisa_uang = gaji_terkini - kebutuhan_seharihari - kebutuhan_takterduga

print("\nUang untuk persepuluhan: %d" %(persepuluhan))
print("Jumlah uang untuk kebutuhan sehari-hari dalam satu bulan: %d" %(kebutuhan_seharihari))
print("Jumlah uang untuk kebutuhan tak terduga bulan ini: %d" %(kebutuhan_takterduga))
print("Sisa uang untuk ditabung: %d" %(sisa_uang))
