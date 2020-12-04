#Langkah kerja

#buatlah list a dan b
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(a)
print(b)
print('--------------------------------')

#sisipkan nilai 10 indeks ke 3 dari a dan nilai 15 indeks ke 2 dari b
a.insert(3, 10)
b.insert(2, 15)
print(a)
print(b)
print('--------------------------------')

#sisipkan nilai 4 indeks terakhir dari a dan 8 indeks terakhir dari b
a.append(4)
b.append(8)
print(a)
print(b)
print('--------------------------------')

#sorting secara ascending pada list a dan b
a.sort()
b.sort()
print(a)
print(b)
print('--------------------------------')

#buat list c dari list a 0-7 dan d dari list b 2-9
c = a[0:8]
d = b[2:10]
print(c)
print(d)
print('--------------------------------')

#buat list e hasil dari penjumlahan elemen c dan d
e = []
for i in range (len(c)):
    j = c[i] + d[i]
    e.append(j)
print(e)
print('--------------------------------')

#ubah list ke tuple
e = tuple(e)
print(e)
print('--------------------------------')

#carilah nilai min, maks, dan jumlahan seluruh elemen dari e
minim = min(e)
maks = max(e)
jumlah = sum(e)
print('Nilai min : ', minim, '\nNilai max : ', maks, '\nJumlah : ', jumlah)
print('--------------------------------')

#buat sebuah string
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)
print('--------------------------------')

#tentukan huruf apa saja untuk menyusun string tersebut
myString = set(myString)
print(myString)
print('--------------------------------')

#ubah ke list dan urutkan secara alfabet
myString = list(myString)
myString.sort()
print(myString)








