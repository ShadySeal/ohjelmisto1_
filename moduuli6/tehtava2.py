import random

luku = int(input("Anna maksimiluku: "))

def noppa():
    maara = 0
    while maara < luku:
        arvo = random.randint(1, 6)
        print(arvo)
        maara = maara + arvo
        if (maara > luku):
            maara = maara - arvo
    print(maara)
    return
noppa()