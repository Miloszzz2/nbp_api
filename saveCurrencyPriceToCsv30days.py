import requests
import pandas as pd


def saveCurrencyPriceToCsv30Days(options, selection):
    response = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/last/30?format=json')

    if 1 <= selection <= len(options):
        res = []
        for i in range(30):
            key = response.json()[i]["effectiveDate"]
            value = response.json()[i]["rates"][selection - 1]["mid"]
            d = {"data":key, "mid": value}
            res.append(d)
        dataFrame = pd.DataFrame(res)

        dataFrame.to_csv(r'C:\Users\wojtek\Pulpit\milosz\nbp_venv\res.csv', index=False, header=True)
    else:
        print("Niepoprawna liczba")
