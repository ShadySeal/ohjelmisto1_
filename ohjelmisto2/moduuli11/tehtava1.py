class Julkaisu:

    def __init__(self, nimi, sivumaara):
        self.nimi = nimi
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Julkaisu: {self.nimi}, {self.sivumaara} sivua.")

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi, sivumaara)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kirjoittaja: {self.kirjoittaja}")

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja, sivumaara):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi, sivumaara)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Päätoimittaja: {self.paatoimittaja}")

julkaisut = []
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä", 40))

for t in julkaisut:
    t.tulosta_tiedot()