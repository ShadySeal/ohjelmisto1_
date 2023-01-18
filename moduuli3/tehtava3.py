sukupuoli = input("Anna sukupuoli: ")
hemoglobiini = float(input("Anna hemoglobiiniarvo: "))

if sukupuoli == "mies" and hemoglobiini >= 134 and hemoglobiini <= 195:
    print ("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli == "mies" and hemoglobiini > 195:
    print("Hemoglobiiniarvo on korkea.")

if sukupuoli == "nainen" and hemoglobiini >= 117 and hemoglobiini <= 175:
    print ("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "nainen" and hemoglobiini < 117:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiiniarvo on korkea.")