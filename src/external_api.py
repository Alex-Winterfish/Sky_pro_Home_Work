import os
from dotenv import load_dotenv
import requests
load_dotenv()

def amount_exchange(amount:float, from_currency:str, to_currency:str)->float:
    api = os.getenv("API_EXCHANGE_KEY")
    amount = str(amount)
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    payload = {}
    headers = {
        "apikey": api
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload, timeout=5)
    except requests.exceptions.ConnectionError:
        return "Connection Error. Please check your network connection"
    except requests.exceptions.HTTPError:
        return "HTTP Error. Please check the URL"
    except requests.exceptions.Timeout:
        return "Request timed out. Please check your network connection"

    result = response.json().get("result")
    return result

