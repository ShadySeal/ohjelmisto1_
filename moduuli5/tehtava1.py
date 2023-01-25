import random

maara = int(input("Kuinka monta arpakuutiota: "))
summa = 0

for luku in range(maara):
    arpakuutio = random.randint(1, 6)
    summa = summa + arpakuutio
print("Summa:", summa)