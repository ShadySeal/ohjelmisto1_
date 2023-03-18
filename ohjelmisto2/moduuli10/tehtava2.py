class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def siirry_kerrokseen(self, kerros):
        print(f"Hissi on kerroksessa {self.kerros}")
        while self.kerros < kerros:
            self.kerros_ylos()
        while self.kerros > kerros:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []
        for i in range(hissien_maara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissi_nro, kohdekerros):
        hissi = self.hissit[hissi_nro - 1]
        hissi.siirry_kerrokseen(kohdekerros)

talo = Talo(1, 10, 2)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 3)