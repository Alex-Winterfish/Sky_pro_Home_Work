from src.masks import (  # импорт функции для наложения маски на номер счета и на номер карты
    get_mask_account,
    get_mask_card_number,
)


def mask_account_card(card_ac_num: str) -> str:
    """функция наложения маски на номер счета или номер карты"""

    count = 1  # переменная-счетчик для определения индекса начала цифр в списке
    if (
        "Счет" not in card_ac_num
    ):  # условие для определения ввода: номер счета или номер карты

        while card_ac_num[-count] != " ":  # цикл для определения индекса начала цифр
            count += 1
        output_string = (
            card_ac_num[0 : len(card_ac_num) - count]
            + " "
            + get_mask_card_number(int(card_ac_num[-count::]))
        )

    else:
        while card_ac_num[-count] != " ":
            count += 1
        output_string = (
            card_ac_num[0 : len(card_ac_num) - count]
            + " "
            + get_mask_account(int(card_ac_num[-count::]))
        )
    if "*" in output_string:  # условие для исключения коротких номеров
        return output_string
    else:
        return "Номер слишком короткий для наложения маски"


def get_date(date: str) -> str:
    """функция выводит дату в формате ДД.ММ.ГГГГ"""
    date_store = ""  # переменная для накопления строки с датой
    count_index = 1  # переменная счетчик для определения индекса конца даты
    if date.find("T") != -1:
        while date[count_index] != "T":
            count_index += 1

        date = date[0:count_index]  # срез строки, содержащий только дату
        for i in range(len(date)):  # цикл для замены разделителей год.месяц.число
            if date[i].isdigit():
                date_store += date[i]
            else:
                date_store += "."

        return date_store
    else:
        return "0001.01.01"
