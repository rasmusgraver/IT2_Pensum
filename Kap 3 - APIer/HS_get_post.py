import requests as req

URL = "https://rasmusweb.no/hs.php"
GameID = "game3"
# MERK: Om du ønsker å lage et "leader board", så kan du legge til en
# underscore etter GameID, og på den måten lage flere IDer (som alle "tilhører deg")
# På denne måten: "game3_1", "game3_2", osv.)
# Så må du selv passe på når du oppdaterer til en ny HS, at du overskriver den "dårligste"
# av de de gamle highscores. Og når du leser highscores, så må du manuelt hente inn alle
# GameIDene. 


def getHS():
    resultat = req.get(URL + "?id=" + GameID)  # , requestOptions)
    print(f"Statuskode: {resultat.status_code}")
    data = resultat.json()
    print(data)
    print("hs:" + data["hs"])
    print("player:" + data["player"])

def postHS(hs, player):
    data = {"id": GameID , "hs": hs, "player": player}
    resultat = req.post(URL, json=data)  #, requestOptions)
    print(f"Statuskode: {resultat.status_code}")
    print(resultat.json())


postHS(33, "Morten")
getHS()

