#Kevin Triantama Prayitno || 71180300
#Universitas Kristen Duta Wacana

n = {"bakso", "soto", "sate"}
number = {1,2,3,4,5}
number2 = {5,4,3,2,1}
number3 = {3,4,5}

l = list(n)
l.append("burger")

sorted(number)
sorted(number2)
sorted(number3)

if number == number2:
    print("isi sama")
else:
    print("isi berbeda")

if number2 == number3:
    print("isi sama yo")
else:
    print("isi beda yo")

n = tuple(l)

print(n)
print(number)