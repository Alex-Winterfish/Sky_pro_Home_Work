from masks import \
    get_mask_account  # импорт функции наложения маски на номер счета из модуля masks
from masks import \
    get_mask_card_number  # импорт функции наложения маски на номер карты из модуля masks


def mask_account_card(card_ac_num: str) -> str:
    """функция наложения маски на номер счета или номер карты"""

    i = 1
    if (
        "Счет" not in card_ac_num
    ):  # условие для определения ввода: номер счета или номер карты

        while card_ac_num[-i] != " ":  # цикл для определения индекса начала цифр
            i += 1
        return (
            card_ac_num[0 : len(card_ac_num) - i]
            + " "
            + get_mask_card_number(int(card_ac_num[-i::]))
        )

    else:
        while card_ac_num[-i] != " ":
            i += 1
        return (
            card_ac_num[0 : len(card_ac_num) - i]
            + " "
            + get_mask_account(int(card_ac_num[-i::]))
        )


def get_date(date: str) -> str:
    """функция для выводит дату в формате ДД.ММ.ГГГГ"""
    return date[8:10] + "." + date[5:7] + "." + date[0:4]
