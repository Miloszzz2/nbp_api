import requests
def showGoldPrice30days():
    response = requests.get('http://api.nbp.pl/api/cenyzlota/last/30?format=json')
    for i in range(30):
        print(response.json()[i]["data"] + '   -   ' + str(response.json()[i]["cena"]))