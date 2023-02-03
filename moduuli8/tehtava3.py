import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='poorPe@ch98',
         autocommit=True
         )
def lentokentta1(icao1):
    sql = f"SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident = '{icao1}';"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
def lentokentta2(icao2):
    sql = f"SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident = '{icao2}';"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
icao1 = input("Annna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Annna toisen lentokentän ICAO-koodi: ")
kentta1 = lentokentta1(icao1)
kentta2 = lentokentta2(icao2)
for rivi in kentta1:
    latitude1 = rivi['latitude_deg']
    longitude1 = rivi['longitude_deg']
for rivi in kentta2:
    latitude2 = rivi['latitude_deg']
    longitude2 = rivi['longitude_deg']
from geopy import distance
lentokentta1 = (latitude1, longitude1)

lentokentta2 = (latitude2, longitude2)

print("Etäisyys:", distance.distance(lentokentta1, lentokentta2).km, "km")
