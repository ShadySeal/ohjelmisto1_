leiviskat = float(input("Anna leiviskät. "))
naulat = float(input("Anna naulat. "))
luodit = float(input("Anna luodit. "))
luoti = 13.3
naula = luoti * 32
leiviska = naula * 20
massa = leiviskat * leiviska + naulat * naula + luoti * luodit
kg = int(massa / 1000)
g = massa % 1000
print ("Massa nykymittojen mukaan: ")
print(kg, "kilogrammaa ja", f"{g:6.2f} grammaa.")