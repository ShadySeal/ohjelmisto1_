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

auto = Auto("ABC-123", 142)

auto.nopeus(30)
auto.nopeus(70)
auto.nopeus(50)

print(auto.rekisteritunnus, auto.huippunopeus, auto.tamanhetkinen_nopeus, auto.kuljettu_matka)