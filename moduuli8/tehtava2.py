import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='poorPe@ch98',
         autocommit=True
         )
def haeLentokentta(maakoodi):
    sql = f"SELECT iso_country, type FROM airport WHERE iso_country = '{maakoodi}';"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

maakoodi = input("Annna lentokentän maakoodi: ")
kentat = haeLentokentta(maakoodi)
closed = 0
small_airport = 0
medium_airport = 0
large_airport = 0
heliport = 0
for rivi in kentat:
    if rivi['type'] == 'closed':
        closed += 1
    if rivi['type'] == 'small_airport':
        small_airport += 1
    if rivi['type'] == 'medium_airport':
        medium_airport += 1
    if rivi['type'] == 'large_airport':
        large_airport += 1
    if rivi['type'] == 'heliport':
        heliport += 1
print("Suljettuja kenttiä:", closed)
print("Pieniä kenttiä:", small_airport)
print("Keskikokoisia kenttiä:", medium_airport)
print("Suuria kenttiä:", large_airport)
print("Helikopterikenttiä:", heliport)
yhteys.close()