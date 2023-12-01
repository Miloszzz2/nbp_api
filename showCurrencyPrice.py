import requests


def showCurrencyPrice(options, selection):
    response = requests.get('https://api.nbp.pl/api/exchangerates/tables/A?format=json')

    if 1 <= selection <= len(options):
        print("Kurs waluty " + response.json()[0]["rates"][selection - 1]["currency"] + ' (' +
              response.json()[0]["rates"][selection - 1]["code"] + ") wynosi: " + str(
            response.json()[0]["rates"][selection - 1]["mid"]))
    else:
        print("Niepoprawna liczba")
