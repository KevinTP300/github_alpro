#Kevin Triantama Prayitno || 71180300
#Universitas Kristen Duta Wacana

merek_hp = {'Samsung' , 'Apple ', 'Xiaomi ', 'Sony '}
merek_ac = { 'LG' ,'Samsung', 'Panasonic', 'Daikin', 'Sony'}

gabungan = merek_hp | merek_ac
# bisa ditulis juga gabungan = merek_hp.union(merek_ac)

irisan = merek_hp & merek_ac
# bisa ditulis juga irisan = merek_hp.intersection(merek_ac)

selisih = merek_hp - merek_ac
# bisa ditulis juga selisih = merek_hp.difference(merek_ac)

komplemen =merek_hp ^ merek_ac
# bisa ditulis juga komplemen = merek_hp.symmetric_difference(merek_ac)

print(gabungan)
print(irisan)
print(selisih)
print(komplemen)

