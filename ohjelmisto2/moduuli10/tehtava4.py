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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä()
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"Rekisteritunnus: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}, tamänhetkinen nopeus: {auto.tamanhetkinen_nopeus}, kuljettu matka: {auto.kuljettu_matka}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = []
for i in range(1,11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

kilpailun_kesto = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    kilpailun_kesto += 1
    if kilpailu.kilpailu_ohi() == True:
        print(f"Kilpailua ajettu {kilpailun_kesto} tuntia.")
        kilpailu.tulosta_tilanne()
    if kilpailun_kesto % 10 == 0:
        print(f"Kilpailua ajettu {kilpailun_kesto} tuntia.")
        kilpailu.tulosta_tilanne()
