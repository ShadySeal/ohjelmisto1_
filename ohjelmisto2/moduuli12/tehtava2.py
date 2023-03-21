import requests
import json

paikkakunta = input("Anna pakkakunnan nimi: ")

pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid=084a0b57bd89a0ea540a1c0ea1c738ca&units=metric"
vastaus = requests.get(pyyntö).json()
print("Lämpötila:", json.dumps(vastaus["main"]["temp"], indent=2),"astetta.")

for a in vastaus["weather"]:
    print("Säätila:", a["description"])