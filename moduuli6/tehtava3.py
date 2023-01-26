litra = 3.785

def lasku():
    litra = 3.785
    while True:
        gallona = int(input("Anna gallonamäärä: "))
        if gallona < 0 :
            break
        tulos = gallona * litra
        print(tulos, "litraa")
    return True

lasku()