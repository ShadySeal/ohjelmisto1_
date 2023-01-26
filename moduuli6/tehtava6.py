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
halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
tulos1 = pizza1(halkaisija1)
tulos2 = pizza2(halkaisija2)
print("Esnimmäinen pizzan hinta:", tulos1, "€")
print("Toisen pizzan hinta:", tulos2, "€")
if (tulos1 < tulos2):
    print("Ensimmäinen pizza on halvempi.")
elif (tulos1 > tulos2):
    print("Toinen pizza on halvempi.")
elif (tulos1 == tulos2):
    print("Molemmat pizzat ovat saman arvoisia.")