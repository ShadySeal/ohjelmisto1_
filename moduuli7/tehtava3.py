lentoasemat = {"EFHK":"Helsinki-Vantaan lentoasema",
               "EFET":"Enontekiön lentoasema",
               "EFIV":"Ivalon lentoasema"}
while True:
    lentoasema = input("Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa? ")
    if lentoasema == "uusi":
        icao = input("Annna lentokentän ICAO-koodi: ")
        nimi = input("Annna lentokentän nimi: ")
        lentoasemat[icao] = nimi
    if lentoasema == "hae":
        koodi = input("Annna lentokentän ICAO-koodi: ")
        print(lentoasemat[koodi])
    if lentoasema == "lopeta":
        break