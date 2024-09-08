from masks import (
    get_mask_account,  # импорт функции для наложения маски на номер счета
    get_mask_card_number,  # импорт функции для наложения маски на номер карты
)


def mask_account_card(card_ac_num: str) -> str:
    """функция наложения маски на номер счета или номер карты"""

    count = 1  # переменная-счетчик для определения индекса начала цифр в списке
    if (
        "Счет" not in card_ac_num
    ):  # условие для определения ввода: номер счета или номер карты

        while card_ac_num[-count] != " ":  # цикл для определения индекса начала цифр
            count += 1
        return (
            card_ac_num[0 : len(card_ac_num) - count]
            + " "
            + get_mask_card_number(int(card_ac_num[-count::]))
        )

    else:
        while card_ac_num[-count] != " ":
            count += 1
        return (
            card_ac_num[0 : len(card_ac_num) - count]
            + " "
            + get_mask_account(int(card_ac_num[-count::]))
        )


def get_date(date: str) -> str:
    """функция выводит дату в формате ДД.ММ.ГГГГ"""
    return date[8:10] + "." + date[5:7] + "." + date[0:4]
