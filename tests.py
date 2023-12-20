import unittest

from main import main
from resources.createChartForCurrency import createChartForCurrency

currency_array = ['THB - bat (Tajlandia)', 'USD - dolar amerykański', 'AUD - dolar australijski',
                  'HKD - dolar Hongkongu', 'CAD - dolar kanadyjski', 'NZD - dolar nowozelandzki',
                  'SGD - dolar singapurski', 'EUR - euro', 'HUF - forint (Węgry)', 'CHF - frank szwajcarski',
                  'GBP - funt szterling', 'UAH - hrywna (Ukraina)', 'JPY - jen (Japonia)',
                  'CZK - korona czeska',
                  'DKK - korona duńska', 'ISK - korona islandzka', 'NOK - korona norweska',
                  'SEK - korona szwedzka', 'RON - lej rumuński', 'BGN - lew (Bułgaria)', 'TRY - lira turecka',
                  'ILS - nowy izraelski szekel', 'CLP - peso chilijskie', 'PHP - peso filipińskie',
                  'MXN - peso meksykańskie', 'ZAR - rand (Republika Południowej Afryki)',
                  'BRL - real (Brazylia)', 'MYR - ringgit (Malezja)', 'IDR - rupia indonezyjska',
                  'INR - rupia indyjska', 'KRW - won południowokoreański', 'CNY - yuan renminbi (Chiny)',
                  'XDR - SDR (MFW)']


class CreateChartForCurrencyTest(unittest.TestCase):
    def test_currency_array_is_not_none(self):
        user_input = 1

        with self.assertRaises(ValueError):
            createChartForCurrency([], user_input)

    def test_user_selection_is_string(self):
        user_input = "asd"
        with self.assertRaises(ValueError):
            createChartForCurrency(currency_array, user_input)

    def test_user_selection_out_of_range(self):
        user_input = 60
        with self.assertRaises(ValueError):
            createChartForCurrency(currency_array, user_input)

    def test_user_gave_input(self):
        user_input = 0
        with self.assertRaises(ValueError):
            createChartForCurrency(currency_array, user_input)

    def test_all_user_inputs(self):
        option1 = "asd"
        option2 = 1
        option3 = 1
        option4 = 0
        selection = 35
        with self.assertRaises(ValueError):
            main(option1, option2, option3, option4, selection)
