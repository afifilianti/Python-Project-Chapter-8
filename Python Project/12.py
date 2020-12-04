#Latihan 12

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
status = True
print('***** Program Harga Buah *****')
print('------------------------------')
print('Daftar harga buah per/kg : ')
print(buah)
print('------------------------------')
while status == True:
    print('Menu :')
    print('A. Tambah data buah \nB. Beli buah \nC. Hapus data \nKeluar')
    menu = input('\nPilihan menu : ')
    total = []
    if menu == 'A':
        i = True
        while i == True:
            dataBaru = input('Masukkan nama buah : ')
            if dataBaru not in buah:
                harganya = int(input('Masukkan harga per/kg : '))
                buah[dataBaru] = harganya
                print('------------------------------')
                print('Daftar Harga Baru')
                for data in buah:
                    print (data, '( Harga Rp', buah.get(data),')')
                    i = False
                print()
            
    elif menu == 'B':
        while True:
            beli = input('Nama buah yang dibeli : ')
            if beli in buah:
                kg = int(input('Berapa Kg             : '))
                harga = kg * buah[beli]
                total.append(harga)
                lagi = input('Beli buah yang lain (y/n)? ')
                if lagi != 'y':
                    print('------------------------------')
                    print('Total harga           : ', sum(total))
                    print()
                    break
    elif menu == 'C':
        i = True
        while i == True:
            delete = input('Tuliskan nama buah yang akan dihapus : ')
            if delete in buah:
                del buah[delete]
                print('Daftar harga baru')
                for data in buah:
                    print(data, '( Harga Rp', buah.get(data),')')
                    i = False
                print()
        
    elif menu == 'Keluar':
        break
