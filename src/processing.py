from datetime import datetime  # импорт функции для работы с датой

from src.witget import get_date


def filter_by_state(input_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и параметр.
    Возвращает список словарей с ключами, соответствующими параметру"""
    output_list = list()  # лист для накопления словарей с требуемым ключём
    for i in range(
        len(input_list)
    ):  # цикл для поиска элемента словаря с ключом, соответствующему параметру
        if input_list[i].get("state") == state:
            output_list.append(input_list[i])
    return output_list


def sort_by_date(input_list: list, sort_option: bool = True) -> list:
    """Функция для сортировки списка словарей по дате, по умолчанию список сортируется по убыванию"""
    return sorted(
        input_list,
        key=lambda input_list: datetime.strptime(
            get_date(input_list["date"]), "%Y.%m.%d"
        ).date(),
        reverse=sort_option,
    )
