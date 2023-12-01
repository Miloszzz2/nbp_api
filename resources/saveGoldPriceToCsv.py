import requests
import pandas as pd


def saveGoldPriceToCsv():
    response = requests.get('https://api.nbp.pl/api/cenyzlota?format=json')
    key = "Złoto"
    value = response.json()[0]['cena']
    d = {key: value}
    res = pd.Series(d)
    res.rename('Mid', inplace=True)
    res.to_csv(r'C:\Users\wojtek\Pulpit\milosz\nbp_venv\res.csv', index=True, header=True)
