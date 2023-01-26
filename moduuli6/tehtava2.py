import random

def noppa():
    arvo = 1
    while arvo < 6:
        arvo = random.randint(1, 6)
        print(arvo)
    return
noppa()