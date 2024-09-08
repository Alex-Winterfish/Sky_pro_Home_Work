from datetime import datetime


def filter_by_state(input_list: list, state="EXECUTED") -> list:
    """Функция принимает список словарей и параметр.
    Возвращает список словарей с ключами, соответствующими параметру"""
    b = list()
    for i in range(
        len(input_list)
    ):  # цикл для поиска элемента словаря с ключом, соответствующему параметру
        if input_list[i].get("state") == state:
            b.append(input_list[i])
    return b


def sort_by_date(input_list: list, sort_option=True) -> list:
    """Функция для сортировки списка словарей по дате, по умолчанию список сортируется по убыванию"""
    return sorted(
        input_list,
        key=lambda input_list: datetime.strptime(
            input_list["date"][0:10], "%Y-%m-%d"
        ).date(),
        reverse=sort_option,
    )
