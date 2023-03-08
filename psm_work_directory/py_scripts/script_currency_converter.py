"""
Not yet in psm
Data fetched from: https://www.ecb.europa.eu/home/html/index.en.html
Doc: https://pypi.org/project/CurrencyConverter/
"""

from currency_converter import CurrencyConverter

# Variables
c = CurrencyConverter()

euro_symbol = "€"
dollar_symbol = "$"
yen_symbol = "¥"
allCurrencies = "{}{} = {}{} = {}{}"


def value_in_numbers():
    # We start with 100€
    euro_amount = 100
    dollar_amount = c.convert(euro_amount, 'EUR', 'USD')
    yen_amount = c.convert(euro_amount, 'EUR', 'JPY')

    return euro_amount, euro_symbol, dollar_amount, dollar_symbol, yen_amount, yen_symbol


# TODO
def value_in_percent():
    euro_percent = 100
    dollar_percent = c.convert(euro_percent, 'EUR', 'USD')
    yen_percent = c.convert(euro_percent, 'EUR', 'JPY')


# Print currencies value relative to € in numbers
print(allCurrencies.format(*value_in_numbers()))

# Print currencies value relative to € in percent
