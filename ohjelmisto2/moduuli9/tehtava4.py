import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def nopeus(self, nopeus):
        self.tamanhetkinen_nopeus += nopeus
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        if self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kiihdytä(self):
        arvottu_nopeus = random.randint(-10, 15)
        self.nopeus(arvottu_nopeus)

    def kulje(self, aika):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * aika

autot = []
for i in range(1,11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

for auto in autot:
    while auto.kuljettu_matka < 10000:
        auto.kiihdytä()
        auto.kulje(1)

    print(f"Rekisteritunnus: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}, tamänhetkinen nopeus: {auto.tamanhetkinen_nopeus}, kuljettu matka: {auto.kuljettu_matka}")