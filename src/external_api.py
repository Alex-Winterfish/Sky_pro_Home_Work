import os

import requests
from dotenv import load_dotenv

load_dotenv()


def amount_exchange(amount: float, from_currency: str, to_currency: str) -> float:
    """Функция конвертирует сумму из одной валюты в другую с помощью внешнего API"""
    api = os.getenv("API_EXCHANGE_KEY")
    amount = str(amount)
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    payload = {}
    headers = {"apikey": api}
    try:
        response = requests.request(
            "GET", url, headers=headers, data=payload, timeout=5
        )
    except requests.exceptions.ConnectionError:  # обрабатываем ошибку подключенияя
        return "Connection Error. Please check your network connection"
    except requests.exceptions.HTTPError:  # обрабатываем ошибку HTTP запроса
        return "HTTP Error. Please check the URL"
    except (
        requests.exceptions.Timeout
    ):  # обрабатываем ошибку привышения времени подключения
        return "Request timed out. Please check your network connection"

    result = response.json().get("result")
    return result
