from showCurrencyPrice import *
from showCurrencyPrice30days import *
from showGoldPrice30days import *
from saveCurrencyPriceToCsv import *
from saveCurrencyPriceToCsv30days import *
from saveGoldPriceToCsv import *
from saveGoldPriceToCsv30Days import *
from createChartForCurrency import *
from createChartForGoldPrice import *
response = requests.get('https://api.nbp.pl/api/exchangerates/tables/A?format=json')
all_currencies_codes = []
for element in response.json()[0]["rates"]:
    all_currencies_codes.append(element["code"] + ' - ' + element["currency"])

print("1. Cena")
print("2. Historia cen")
option1 = int(input("Wybierz opcje: "))
print("Czego? ")
print("1. Waluty")
print("2. Złota")
option2 = int(input("Wybierz opcje: "))
print("Zapisać do pliku CSV?")
print("1. Tak")
print("2. Nie")
option3 = int(input("Wybierz opcje: "))
option4 = 0
if option1==2:
    print("Pokazać wykres dla danych okresowych? ")
    print("1. Tak")
    print("2. Nie")
    option4 = int(input("Wybierz opcje: "))
if option2 == 1:
    for idx, option in enumerate(all_currencies_codes, start=1):
        print(f"{idx}. {option}")

    selection = input("Twój wybór (liczba): ")
    selection = int(selection)
if option3 == 1:
    if option1 == 1 and option2 == 1:
        saveCurrencyPriceToCsv(all_currencies_codes, selection)
    elif option1 == 2 and option2 == 1:
        saveCurrencyPriceToCsv30Days(all_currencies_codes, selection)
    elif option1 == 1 and option2 == 2:
        saveGoldPriceToCsv()
    elif option1 == 2 and option2 == 2:
        saveGoldPrice30daysToCsv()
    else:
        print("Niepoprawna wartosc")

elif option3 == 2:
    if option1 == 1 and option2 == 1:
        showCurrencyPrice(all_currencies_codes, selection)
    elif option1 == 1 and option2 == 2:
        response = requests.get('https://api.nbp.pl/api/cenyzlota?format=json')
        print("Aktualna cena złota wynosi: " + str(response.json()[0]['cena']))
    elif option1 == 2 and option2 == 1:
        showCurrencyPrice30days(all_currencies_codes, selection)
    elif option1 == 2 and option1 == 2:
        showGoldPrice30days()
    else:
        print("Niepoprawna wartosc")
else:
    print("Niepoprawna wartosc")

if option4 == 1:
    if option2 == 1:
        createChartForCurrency(all_currencies_codes, selection)
    if option2 ==2:
        createChartForGoldPrice()
elif option4>2:
    print("Niepoprawna wartosc")
