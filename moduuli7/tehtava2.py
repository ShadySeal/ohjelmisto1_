nimet = {""}
nimi = input("Anna nimi: ")
while nimi != "":
    nimet.add(nimi)
    nimi = input("Anna toinen nimi: ")
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
for i in nimet:
    print(i)