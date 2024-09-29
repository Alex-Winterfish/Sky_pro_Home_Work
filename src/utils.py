
def get_transaction_data(file_path:str)->list:
    "функция принимает путь до json файла и возвращает список словарей"
    output_list = list()
    import os
    import json
    #обрабатываем ошибку "файл не найден"
    try:
        with open(os.path.abspath(file_path), 'r', encoding="utf-8") as f:
            #обрабатываем ошибку декодирования файла
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print('Ошибка декодирования файла')
                return output_list
    except FileNotFoundError:
        print('Файл не найден')
        return output_list
    return data

file_path = '../data/operations.json'

def transaction_sum(transaction:dict)->float:
    "Функция возвращает сумму транзакций"
    from src.external_api import amount_exchange

    try: # обрабатываем ошибку функции конвертации валюты amount_exchange

        if transaction != {}:
            if transaction.get("operationAmount").get("currency").get('code') == "RUB":
                output_sum = float(transaction.get("operationAmount").get('amount'))
            elif transaction.get("operationAmount").get("currency").get('code') == "USD":
                usd_sum = float(transaction.get("operationAmount").get('amount'))
                output_sum = amount_exchange(usd_sum, "USD","RUB")
            elif transaction.get("operationAmount").get("currency").get('code') == "EUR":
                eur_sum = float(transaction.get("operationAmount").get('amount'))
                output_sum = amount_exchange(eur_sum, "EUR", "RUB")


    except TypeError:
        return "Ошибка конвертации валюты"
    return output_sum
