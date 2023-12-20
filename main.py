from resources.createChartForCurrency import *
from resources.createChartForGoldPrice import *
from resources.saveCurrencyPriceToCsv import *
from resources.saveCurrencyPriceToCsv30days import *
from resources.saveGoldPriceToCsv import *
from resources.saveGoldPriceToCsv30Days import *
from resources.showCurrencyPrice import *
from resources.showCurrencyPrice30days import *
from resources.showGoldPrice30days import *

response = requests.get('https://api.nbp.pl/api/exchangerates/tables/A?format=json')
all_currencies_codes = []
for element in response.json()[0]["rates"]:
    all_currencies_codes.append(element["code"] + ' - ' + element["currency"])


def is_parsable_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def main(user_option1, user_option2, user_option3, user_option4, user_selection):
    if user_option1.isdigit() and user_option2.isdigit() and user_option3.isdigit() and user_option4.isdigit() and user_selection.isdigit() and (
            0 < user_option1 < 3) and (0 < user_option2 < 3) and (0 < user_option3 < 3) and (
            user_option4 == 0 or (0 < user_option4 < 3)) and (
            user_selection == 0 or (0 < user_selection < 34)):

        if user_option3 == 1:
            if user_option1 == 1 and user_option2 == 1:
                saveCurrencyPriceToCsv(all_currencies_codes, user_selection)
            elif user_option1 == 2 and user_option2 == 1:
                saveCurrencyPriceToCsv30Days(all_currencies_codes, user_selection)
            elif user_option1 == 1 and user_option2 == 2:
                saveGoldPriceToCsv()
            elif user_option1 == 2 and user_option2 == 2:
                saveGoldPrice30daysToCsv()
            else:
                print("Niepoprawna wartosc")

        elif user_option3 == 2:
            if user_option1 == 1 and user_option2 == 1:
                showCurrencyPrice(all_currencies_codes, user_selection)
            elif user_option1 == 1 and user_option2 == 2:
                response2 = requests.get('https://api.nbp.pl/api/cenyzlota?format=json')
                print("Aktualna cena złota wynosi: " + str(response2.json()[0]['cena']))
            elif user_option1 == 2 and user_option2 == 1:
                showCurrencyPrice30days(all_currencies_codes, user_selection)
            elif user_option1 == 2 and user_option1 == 2:
                showGoldPrice30days()
            else:
                print("Niepoprawna wartosc")
        else:
            print("Niepoprawna wartosc")

        if user_option4 == 1:
            if user_option2 == 1:
                createChartForCurrency(all_currencies_codes, user_selection)
            if user_option2 == 2:
                createChartForGoldPrice()
        elif user_option4 > 2:
            print("Niepoprawna wartosc")
    else:
        print("Któraś wartość jest niepoprawna")
        raise ValueError


if __name__ == "__main__":
    print("1. Cena")
    print("2. Historia cen")
    option1 = input("Wybierz opcje: ")
    print("Czego? ")
    print("1. Waluty")
    print("2. Złota")
    option2 = input("Wybierz opcje: ")
    print("Zapisać do pliku CSV?")
    print("1. Tak")
    print("2. Nie")
    option3 = input("Wybierz opcje: ")
    option4 = 0
    selection = 0
    if option1 == 2:
        print("Pokazać wykres dla danych okresowych? ")
        print("1. Tak")
        print("2. Nie")
        option4 = input("Wybierz opcje: ")
    if option2 == 1:
        for idx, option in enumerate(all_currencies_codes, start=1):
            print(f"{idx}. {option}")

        selection = input("Twój wybór (liczba): ")
    main(option1, option2, option3, option4, selection)
