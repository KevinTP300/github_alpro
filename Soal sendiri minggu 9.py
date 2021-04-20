#Kevin Triantama Prayitno || 71180300
#Universitas Kristen Duta Wacana

makanan = ['bakso','sate','padang','rujak','soto']
makanan.extend (['mc', 'steak'])
# makanan.append (['kaldu', 'gorengan'])
makanan.sort()

makanan.pop(2)
del makanan [3]
makanan.remove('bakso') 

print(makanan)