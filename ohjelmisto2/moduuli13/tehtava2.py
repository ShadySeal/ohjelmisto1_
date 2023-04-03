from flask import Flask, request, Response
import mysql.connector
import json

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='poorPe@ch98',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<teksti>')
def summa(teksti):

    sql = f"SELECT name, municipality FROM airport WHERE ident = '{teksti}';"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchone()

    vastaus = {
        "ICAO" : teksti,
        "Name" : tulos['name'],
        "Municipality" : tulos['municipality']
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)