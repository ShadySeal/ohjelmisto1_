import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='poorPe@ch98',
         autocommit=True
         )
def haeLentokentta(icao):
    sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{icao}';"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

icao = input("Annna lentokentän ICAO-koodi: ")

kentat = haeLentokentta(icao)
if kentat:
    print(kentat)
else:
    print("Lentokenttää ei löydy.")

yhteys.close()