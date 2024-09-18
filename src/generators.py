def filter_by_currency(transactions_list: list, currency: str):
    "Функция сортирует входной список и выводит список транзакций с заданной валютой 'USD' или 'RUB' параметр currency"
    for i in range(len(transactions_list)):  # цикл для перебор словарей в списке
        if (
            transactions_list[i].get("operationAmount").get("currency").get("code")
            == currency
        ):
            yield transactions_list[i]


def transaction_descriptions(transactions_list: list):
    "Функция выводит тип транзакции во входном списке"
    i = 0  # переменная счетчик для перебора словарей в списке
    while True:
        yield transactions_list[i].get("description")
        i += 1


def card_number_generator(start: int, end: int):
    "Функция для генерации номеров карт"
    support_num = start - 1  # опорное число формирования номера карты
    while support_num < end:  # цикл для генерации номера карты
        support_num += 1
        output_list = list()  # список для накопления выходного значения номера карты
        list_of_num = (
            support_num // 10**12 % 10**4,
            support_num // 10**8 % 10**4,
            support_num // 10**4 % 10**4,
            support_num % 10**4,
        )  # список для разбиения сгенерированного
        # числа по 4 цифры
        for i in range(4):  # цикл для добавления нолей в пустые разряды
            if len(str(list_of_num[i])) < 4:
                output_list.append(
                    (4 - len(str(list_of_num[i]))) * "0" + str(list_of_num[i])
                )
            else:
                output_list.append(str(list_of_num[i]))
        yield " ".join(output_list)
