def pizza1(halkaisija1):
    pi = 3.142
    sade = halkaisija1 / 2
    tulos = pi * (sade * sade)
    return round(tulos)
def pizza2(halkaisija2):
    pi = 3.142
    sade = halkaisija2 / 2
    tulos = pi * (sade * sade)
    return round(tulos)
halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))
tulos1 = pizza1(halkaisija1)
tulos2 = pizza2(halkaisija2)
hinta1 -= tulos1
hinta2 -= tulos2
if hinta1 < 0:
    hinta1 = -hinta1
if hinta2 < 0:
    hinta2 = -hinta2
print("Ensimmäinen pizzan hinta:", tulos1, "€")
print("Toisen pizzan hinta:", tulos2, "€")
if (hinta1 < hinta2):
    print("Ensimmäinen pizza on parempi vastine rahalle.")
elif (hinta1 > hinta2):
    print("Toinen pizza on parempi vastine rahalle.")
elif (hinta1 == hinta2):
    print("Molemmat pizzat ovat yhtä hyviä vastineita rahalle.")