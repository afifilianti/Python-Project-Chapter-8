#Latihan 1


listAngka = []
bil = int ( input ('Tulislah banyaknya bilangan yang akan dimasukkan : '))
while(len(listAngka) < bil):
    angka = int ( input ("Masukkan angka : "))
    listAngka.append(angka)
listAngka.sort(reverse = True)
print ("Urutan besar ke kecil dari angka yang sudah dimasukkan adalah\n",listAngka)
