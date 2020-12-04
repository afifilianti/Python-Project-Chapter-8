#Latihan 3

print('===== Program Mahasiswa =====')
status = True
i = []
while status == True:
    nama = input('Masukkan nama mahasiswa : ',)
    i.append(nama)
    i.sort()
    lagi = input('Lagi? (y/n) : ')
    if lagi != 'y':
        print()
        for data in i:
            print(data, '(', len(data), 'karakter', ')')
            status = False
