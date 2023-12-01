import requests
import pandas as pd
def saveCurrencyPriceToCsv(options, selection):
    response = requests.get('https://api.nbp.pl/api/exchangerates/tables/A?format=json')

    if 1 <= selection <= len(options):
        key = response.json()[0]["rates"][selection - 1]["currency"]
        value = response.json()[0]["rates"][selection - 1]["mid"]
        d = {key: value}
        res = pd.Series(d)
        res.rename('Mid', inplace=True)
        res.to_csv(r'C:\Users\wojtek\Pulpit\milosz\nbp_venv\res.csv', index=True, header=True)
    else:
        print("Niepoprawna liczba")
