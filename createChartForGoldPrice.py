import requests
import pandas as pd
import matplotlib.pyplot as plt

def createChartForGoldPrice():
    response = requests.get('http://api.nbp.pl/api/cenyzlota/last/30?format=json')
    res = []
    for i in range(30):
        key = response.json()[i]["data"]
        value = response.json()[i]["cena"]
        d = {"data": key, "mid": value}
        res.append(d)
    df = pd.DataFrame(res)
    plt.plot(range(len(df['data'])), df['mid'], marker='o', linestyle='-', color='b', label='Kurs')
    plt.title('Zmiana ceny złota przez ostatnie 30 dni')
    plt.xlabel('Dni')
    plt.ylabel('Cena')
    plt.show()
