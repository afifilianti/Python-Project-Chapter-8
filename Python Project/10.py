#Latihan 10

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('***** Program Harga Buah *****')
print('------------------------------')
print('Daftar harga buah per/kg : ')
print(buah)
print('------------------------------')
total = []
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
            break
