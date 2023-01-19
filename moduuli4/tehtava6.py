import random
import math

N = int(input("Arvottomien pisteiden määrä: "))
n = 0

arvottujaPisteita = 0
while arvottujaPisteita < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x * x + y * y < 1:
        n += 1
    arvottujaPisteita += 1

piinLikiarvo = 4 * n / N
print(f"Piin likiarvo on {piinLikiarvo}")
print(f"Piin tarkka arvo on {math.pi} ja erotus on {piinLikiarvo - math.pi} ")