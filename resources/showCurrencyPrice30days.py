import requests
def showCurrencyPrice30days(options, selection):
    response = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/last/30?format=json')

    if 1 <= selection <= len(options):
        for i in range(30):
            print(response.json()[i]["effectiveDate"] + '   -   ' + str(response.json()[i]["rates"][selection-1]["mid"]))
    else:
        print("Niepoprawna liczba")
