tuumaCm = 2.54
while True:
    tuuma = float(input("Anna tuuma: "))
    lasku = tuumaCm * tuuma
    if not lasku > 0:
        break
    print(lasku, "cm")