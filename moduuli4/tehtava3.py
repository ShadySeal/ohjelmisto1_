max = None
min = None
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luku = int(luku)
    if (max is None or luku > max):
        max = luku
    elif (min is None or luku < min):
        min = luku
print("Suurin", max)
print("Pienin", min)