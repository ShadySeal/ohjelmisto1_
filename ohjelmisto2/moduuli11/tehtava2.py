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

    def kulje(self, aika):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * aika

class Sähköauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)

sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.nopeus(60)
sahkoauto.kulje(3)

polttomoottoriauto.nopeus(40)
polttomoottoriauto.kulje(3)

print(f"Auton {sahkoauto.rekisteritunnus} kulkema matka {sahkoauto.kuljettu_matka}.")
print(f"Auton {polttomoottoriauto.rekisteritunnus} kulkema matka {polttomoottoriauto.kuljettu_matka}.")