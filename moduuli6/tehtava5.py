def lista1 (lista01):
    for lista in lista01:
        print(lista)
    return
def lista2 (lista02):
    for lista in lista02:
        if lista % 2 == 0:
            print("Parillinen luku:", lista)
    return

lista01 = [2, 7, 4, 9, 1, 3]
lista02 = [2, 7, 4, 9, 1, 3]
lista1(lista01)
lista2(lista02)