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

    def kulje(self, aika):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * aika

auto = Auto("ABC-123", 142)

auto.nopeus(60)
auto.kulje(2)

print(f"Rekisteritunnus: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}, tamänhetkinen nopeus: {auto.tamanhetkinen_nopeus}, kuljettu matka: {auto.kuljettu_matka}")