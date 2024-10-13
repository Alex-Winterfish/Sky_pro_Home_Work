import logging

logger = logging.getLogger("utils")
handler = logging.FileHandler("./logs/utils.log", "w")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

file_path = "../data/operations.json"  # раскомитить для проверки лигирования #раскомитить для проверки лигирования


def get_transaction_data(file_path: str) -> list:
    "функция принимает путь до json файла и возвращает список словарей"
    output_list = list()
    import json
    import os

    # обрабатываем ошибку "файл не найден"
    try:
        logger.info(f"Открываем файл {file_path}")
        with open(os.path.abspath(file_path), "r", encoding="utf-8") as f:
            # обрабатываем ошибку декодирования файла
            try:
                logger.info(f"Получаем данные из файла {file_path}")
                data = json.load(f)
            except json.JSONDecodeError:
                logger.error(f"Ошибка декодирования файла {file_path}")
                print("Ошибка декодирования файла")
                return output_list
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        print("Файл не найден")
        return output_list
    return data


# transaction_data = get_transaction_data(file_path)
def transaction_sum(transaction: dict) -> float:
    "Функция возвращает сумму транзакций"
    from src.external_api import amount_exchange

    try:  # обрабатываем ошибку функции конвертации валюты amount_exchange

        logger.info("получаем словарь с транзакцией")
        if transaction != {}:
            if transaction.get("operationAmount").get("currency").get("code") == "RUB":
                logger.info("Транзакция совершена в рублях, получаем сумму транзакции")
                output_sum = float(transaction.get("operationAmount").get("amount"))
            elif (
                transaction.get("operationAmount").get("currency").get("code") == "USD"
            ):
                logger.info("Транзакция совершена в валюте USD, получаем сумму транзакции")
                usd_sum = float(transaction.get("operationAmount").get("amount"))
                output_sum = amount_exchange(usd_sum, "USD", "RUB")
            elif (
                transaction.get("operationAmount").get("currency").get("code") == "EUR"
            ):
                logger.info(
                    "Транзакция совершена в валюте EUR, получаем сумму транзакции"
                )
                eur_sum = float(transaction.get("operationAmount").get("amount"))
                output_sum = amount_exchange(eur_sum, "EUR", "RUB")
        else:
            logger.warning("Данные по транзакции не найдены")
            return dict()

    except TypeError:
        logger.error("Ошибка конвертации валюты")
        return "Ошибка конвертации валюты"
    return output_sum


# transaction_sum(transaction_data[0]) #раскомитить для проверки лигирования
