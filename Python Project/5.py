#Latihan 5

def kuadrat(bil):
    hasil = []
    for data in bil:
        data = data**2
        hasil.append(data)
    print(hasil)

bil = [2, 4, 5, 6]  
hasil = kuadrat(bil)
