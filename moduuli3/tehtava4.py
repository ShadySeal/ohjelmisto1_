vuosi = int(input("Anna vuosi: "))

if vuosi % 4 == 0:
    print ("Annettu vuosi on karkausvuosi.")
elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print ("Annettu vuosi on karkausvuosi.")
else:
    print("Annettu vuosi ei ole karkausvuosi.")