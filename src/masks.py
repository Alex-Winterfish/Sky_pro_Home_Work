def get_mask_card_number(card_num: int) -> str:
    """Функция, которая принимает номер карты и возвращает маску номера"""
    card_num_mask_delimited = ""
    card_num_mask = (
        str(card_num)[0:6] + "*" * (len(str(card_num)) - 10) + str(card_num)[-4:]
    )
    i = 0

    while i < len(
        str(card_num)
    ):  # цикл для разделения пробелами по 4 символа номера карты

        card_num_mask_delimited += card_num_mask[i : i + 4] + " "
        i += 4

    return card_num_mask_delimited


def get_mask_account(account: int) -> str:
    """Функция, которая принимает номер счета и возвращает маску номера"""
    return "**" + str(account)[-4:]
