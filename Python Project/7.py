#Latihan 7

def maxValue(buah):
    nilaiMax = max(buah, key = buah.get)
    print(nilaiMax)

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
maxValue(buah)
