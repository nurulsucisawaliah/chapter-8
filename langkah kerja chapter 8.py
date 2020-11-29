print('================================================================================')
print('=============================== tipe data list =================================')
print('================================================================================')
#langkah kerja nomor 1
a = [1,5,6,3,6,9,11,20,12]
print(a)
b = [7,4,5,6,7,1,12,5,9]
print(b)

#langkah kerja nomor 2
a.insert(3,10)
print(a)
b.insert(2,15)
print(b)

#langkah kerja nomor 3
a.append(4)
print(a)
b.append(8)
print(b)

#langkah kerja nomor 4
a.sort()
print(a)
b.sort()
print(b)

#langkah kerja nomor 5
c = a[0:7]
print(c)
d = b[2:9]
print(d)

#langkah kerja nomor 6
e =[]
for j in range (len(c)):
    listnya = c[j]+ d[j]
    e = e + [listnya]
print(e)

#langkah kerja nomor 7
e = tuple(e)
print(e)

#langkah kerja nomor 8
min = min(e)
max = max(e)
jum = sum(e)
print(min,max,jum)

print('================================================================================')
print('=============================== tipe data set ==================================')
print('================================================================================')
#langkah kerja nomor 9
myString = "python adalah bahasa pemrograman yang menyenangkan"

#langkah kerja nomor 10
penyusunKarakter = set(myString)
print(penyusunKarakter)

#langkah kerja nomor 11
myList = list(penyusunKarakter)
myList.sort()
print(myList)
