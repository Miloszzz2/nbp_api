import matplotlib.pyplot as plt
import pandas as pd
import requests


def createChartForCurrency(options, selection):

    if len(options) == 0:
        raise ValueError

    if isinstance(selection, str):
        raise ValueError

    response = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/last/30?format=json')
    if 1 <= selection <= len(options):
        res = []
        for i in range(30):
            key = response.json()[i]["effectiveDate"]
            value = response.json()[i]["rates"][selection - 1]["mid"]
            d = {"data": key, "mid": value}
            res.append(d)
        df = pd.DataFrame(res)
        plt.plot(range(len(df['data'])), df['mid'], marker='o', linestyle='-', color='b', label='Kurs')
        plt.title('Zmiana ceny ' + str(options[selection - 1]) + ' przez ostatnie 30 dni')
        plt.xlabel('Dni')
        plt.ylabel('Cena')
        plt.show()
    else:
        raise ValueError


