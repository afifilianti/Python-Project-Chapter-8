#Latihan 4

print('===== Program Data Sayur =====')
sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print('Sayur :', sayur)
while True :
    print('Menu : \nA. Tambah data sayur \nB. Hapus data sayur \nC. Tampilkan data sayur \nKeluar\n')
    menu = input('Masukkan pilihan Anda : ')
    if menu == 'A':
        tambah = input('Tulislah sayur yang ingin Anda tambahkan : ')
        print(tambah, 'telah dimasukkan ke dalam list\n')
        sayur.append(tambah)
    elif menu == 'B':
        try:
            hapus = input('Tulislah sayur yang ingin Anda hapus : ')
            print(hapus, 'sudah dihapus dari list\n')
            sayur.remove(hapus)
        except ValueError:
            print('Sayur tersebut tidak terdapat dalam list\n')
    elif menu == 'C':
        print('Data sayur : ', sayur, '\n')
    elif menu == 'Keluar':
        break
