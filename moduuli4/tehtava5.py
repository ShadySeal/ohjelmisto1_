kayttajatunnus = "python"
salasana = "rules"
i = 0

while True:
    if i == 5:
        break
    tunnus = input("Arvaa käyttäjätunnus: ")
    sala = input("Arvaa salasana: ")
    if tunnus == kayttajatunnus and sala == salasana:
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")
        i = i + 1