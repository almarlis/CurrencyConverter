import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
            if quote == base:
                raise ConvertionException(f`Невозможно перевести одинаковые валюты {base}`)

                try:
                    quote_ticker = keys[quote]
                except KeyError:
                    raise ConvertionException(f`Не удалось обработать валюту {quote}`)

                try:
                    base_ticker = keys[base]
                except KeyError:
                    raise ConvertionException(f`Не удалось обработать валюту {base}`)

                try:
                    amount = float(amount)
                except ValueError:
                    raise ConvertionException(f`Не удалось обработать количество {amount}`)

            r = requests.get(f`https://api.apilayer.com/exchangerates_data/live?base={quote_ticker}&symbols={base_ticker}`, headers = {'apikey': `nSxQvhASp8dgjnUX4Ua33o19vKercyMg'})
            total_base = json.loads(r.content)[keys[base]]

            return total_base
