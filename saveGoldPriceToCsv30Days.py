import requests
import pandas as pd

def saveGoldPrice30daysToCsv():
    response = requests.get('http://api.nbp.pl/api/cenyzlota/last/30?format=json')
    res = []
    for i in range(30):
        key = response.json()[i]["data"]
        value = response.json()[i]["cena"]
        d = {"data": key, "mid": value}
        res.append(d)
    dataFrame = pd.DataFrame(res)
    dataFrame.to_csv(r'C:\Users\wojtek\Pulpit\milosz\nbp_venv\res.csv', index=False, header=True)
