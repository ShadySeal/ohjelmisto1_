luvut = []

luku = input("Anna luku: ")

while luku!="":
    luvut.append(luku)
    luku = input("Anna luku: ")
luvut.sort(reverse=True)
for luvut in luvut[:5]:
    print(luvut)