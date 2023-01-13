kuha = float(input("Anna kuhan pituus: "))

if kuha < 37:
    pituus = 37 - kuha
    print ("Kuha on ", pituus, "cm alamittainen, laske takaisin järveen.")
else:
    print("Kuha on tarpeeksi pitkä.")