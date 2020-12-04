#Latihan 2

def dataStat(x):
    i = []
    for data in x:
        a = sum(x) / len(x)
        b = max(x)
        c = min(x)
    i.append(a)
    i.append(b)
    i.append(c)
    print(i)
    
x = [24, 14, 10, 33, 40, 22, 8, 10, 18, 29]
dataStat(x)
