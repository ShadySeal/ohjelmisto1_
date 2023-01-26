def lasku(gallona):
    litra = 3.785
    summa = gallona * litra
    return summa

while True:
    gallona = int(input("Anna gallonamäärä: "))
    if gallona < 0:
        break
    tulos = lasku(gallona)
    print(tulos, "litraa")