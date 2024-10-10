filepath = "../data/transactions.csv"


def csv_processing(filepath: str) -> list:
    """Функция принимает путь к файлу csv и возвращает список словарей с транзакциями"""
    import csv

    output_list = list()
    try:
        with open(filepath, encoding="utf-8") as csv_file:

            csv_reader = csv.DictReader(
                csv_file, delimiter=";"
            )  # читаем файл как словарь

            for row in csv_reader:  # цикл для добавления словарей в список
                output_list.append(row)
                next(csv_reader)

        return output_list
    except FileNotFoundError:
        return f"Файл по адресу {filepath} не найден"


filepath_excel = "../data/transactions_excel.xlsx"


def excel_processing(filepath: str) -> list:
    """Функция принимает путь к файлу xls и возвращает список словарей с транзакциями"""
    import pandas as pd

    try:
        transaction_data_xls = pd.read_excel(filepath).to_dict(
            "index"
        )  # читаем файл excel и переводим в словарь
        output_list = list()
        for (
            values
        ) in (
            transaction_data_xls.values()
        ):  # цикл для добавления словарй с транзакциями в список
            output_list.append(values)

        return output_list
    except FileNotFoundError:
        return f"Файл по адресу {filepath_excel} не найден"


