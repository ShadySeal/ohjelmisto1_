lista = [1, 2, 3, 4, 5, 6, 7]

def lasku(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

tulos = lasku(lista)
print(tulos)