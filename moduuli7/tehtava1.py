vuodenaika = int(input("Anna kuukauden numero: "))
vuodenajat = ("kevät", "kesä", "syksy", "talvi")
if vuodenaika == 12 or vuodenaika == 1 or vuodenaika == 2:
    print(vuodenajat[3])
if vuodenaika == 3 or vuodenaika == 4 or vuodenaika == 5:
    print(vuodenajat[0])
if vuodenaika == 6 or vuodenaika == 7 or vuodenaika == 8:
    print(vuodenajat[1])
if vuodenaika == 9 or vuodenaika == 10 or vuodenaika == 11:
    print(vuodenajat[2])