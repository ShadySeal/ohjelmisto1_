import random

Oikealuku = random.randint(1,10)

while True:
    luku = int(input("Arvaa oikea luku: "))
    if luku == Oikealuku:
        print("Oikein")
        break
    elif luku < Oikealuku:
        print("Liian pieni arvaus")
    elif luku > Oikealuku:
        print("Liian suuri arvaus")