import random

def noppa():
    arvo = random.randint(1, 6)
    while arvo < 6:
        arvo = random.randint(1, 6)
        print(arvo)
    return
noppa()