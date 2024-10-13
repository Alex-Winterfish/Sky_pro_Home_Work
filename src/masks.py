import logging

logger = logging.getLogger("masks")
handler = logging.FileHandler("./logs/masks.log", "w")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_mask_card_number(card_num: int) -> str:
    """Функция, которая принимает номер карты и возвращает маску номера"""
    if len(str(card_num)) > 10:
        logger.info(
            "введен номер карты достаточной длинны для наложения маски, накладываем маску"
        )
        card_num_mask_delimited = ""
        card_num_mask = (
            str(card_num)[0:6] + "*" * (len(str(card_num)) - 10) + str(card_num)[-4:]
        )
        counter = 0  # переменная-счетчик для подсчета чисел в номере карты
        logger.info("начинаем отделять номер карты по 4 цифры")
        while counter < len(
            str(card_num)
        ):  # цикл для разделения пробелами по 4 символа номера карты

            card_num_mask_delimited += card_num_mask[counter : counter + 4] + " "
            counter += 4
        logger.info("Выводим маску номера")
        return card_num_mask_delimited[0:-1]
    else:
        logger.error("номер карты слишком короткий")
        return "номер карты слишком короткий для наложения маски"


# card_mask = get_mask_card_number(87685464564564546) #раскомитить для проверки лигирования


def get_mask_account(account: int) -> str:
    """Функция, которая принимает номер счета и возвращает маску номера"""
    if len(str(account)) > 4:
        logger.info(
            "введен номер  счета достаточной длинны для наложения маски, накладываем маску"
        )
        return "**" + str(account)[-4:]
    else:
        logger.error("номер счета слишком короткий для наложения маски")
        return "номер счета слишком короткий для наложения маски"


# account_mask = get_mask_account(23443232) #раскомитить для проверки лигирования
