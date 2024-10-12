from src.utils import get_transaction_data
from src.dataframe_processing import csv_processing, excel_processing
from src.processing import filter_by_state, sort_by_date
from src.transaction_search import user_search
from src.witget import get_date, mask_account_card

file_path_json = "../data/operations.json"
file_path_csv = "./data/transactions.csv"
file_path_excel = "../data/transactions_excel.xlsx"


def user_file_select():
    return input(
        " Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        " Выберите необходимый пункт меню:\n "
        "1. Полоучить информацию о транзакциях из JSON-файла\n "
        "2. Полоучить информацию о транзакциях из CSV-файла\n "
        "3. Полоучить информацию о транзакциях из XLSX-файла\n "
        "ввод: "
    )


def user_state_select():
    a = input(
        "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтрации статусы:\n"
        "EXECUTED, CANCELED, PENDING\n"
        "ввод: "
    ).upper()
    return a


def user_sort_option():
    a = input("Отсортировать операции по дате? Да/нет\n Пользователь: ")
    return a


def user_sorting():
    a = input("Отсортировать по возрастанию или по убыванию?\n Пользователь: ")
    return a


def user_search_word():
    a = input("Введите слово для сортировки:\n Пользователь: ")
    return a


def user_sorting_range():
    a = input("Отсортировать по определенному слову? Да/Нет:\n Пользователь: ")
    return a


def main():

    file_select = user_file_select()  # выбераем файл для обработки

    if file_select == "1":  # получаем список транзакций из json файла
        print("Для обработки выбран json-файл")
        transaction_list = get_transaction_data(file_path_json)

    elif file_select == "2":  # получаем список транзакций из csv файла
        print("Для обработки выбран csv-файл")
        transaction_list = csv_processing(file_path_csv)

    elif file_select == "3":  # получаем список транзакций из excel файла
        print("Для обработки выбран excel-файл")
        transaction_list = excel_processing(file_path_excel)

    while True:  # цикл для ввода пользователем фильтра для операций
        # пока пользователь не введет статус операции, запрашиваем ввод

        state_select = user_state_select()

        if state_select in [
            "EXECUTED",
            "CANCELED",
            "PENDING",
        ]:  # если пользователь ввел статус операции, прерываем цикл
            break
        else:
            print(f"Статус операции {state_select} недоступен")
    filtered_data = filter_by_state(
        transaction_list, state=state_select
    )  # фильтруем список по заданному статусу
    print(f"Операции отфильтрованы по статусу {state_select}")

    sort_option = user_sort_option()

    if sort_option.upper() == "ДА":  # цикл для сортировки по дате

        sorting = user_sorting()
        if sorting.upper() == "ПО ВОЗРАСТАНИЮ":
            sort_options = False
            filtered_data = sort_by_date(filtered_data, sort_options)
        else:
            filtered_data = sort_by_date(filtered_data)

    sort_option = user_sorting_range()
    if sort_option.upper() == "ДА":
        search_word = user_search_word()
        filtered_data = user_search(filtered_data, search_word)

    if filtered_data == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:

        print(
            f"Распечатываю итоговый список транзакций...\n"
            f"Всего банковских операций: {len(filtered_data)}\n\n"
        )
        for i in range(len(filtered_data)):
            if filtered_data[i].get("description") == "Открытие вклада":

                print(
                    f"{get_date(filtered_data[i].get('date'))} {filtered_data[i].get('description')}\n"
                    f"{mask_account_card(filtered_data[i].get('to'))}\n"
                    f"Сумма: {filtered_data[i].get('amount')} {filtered_data[i].get('currency_name')}\n\n"
                )
            else:
                print(
                    f"{get_date(filtered_data[i].get('date'))} {filtered_data[i].get('description')}\n"
                    f"{mask_account_card(filtered_data[i].get('from'))} \
                    -> {mask_account_card(filtered_data[i].get('to'))}\n"
                    f"Сумма: {filtered_data[i].get('amount')} {filtered_data[i].get('currency_name')}\n\n"
                )


if __name__ == "__main__":

    print(main())
