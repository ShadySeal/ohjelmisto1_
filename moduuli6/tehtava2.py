import random

def noppa(luku):
    maara = 0
    while maara < luku:
        arvo = random.randint(1, 6)
        maara = maara + arvo
        if (maara > luku):
            maara = maara - arvo
        else:
            print(arvo)
    print(maara)
    return
luku = int(input("Anna maksimiluku: "))
noppa(luku)