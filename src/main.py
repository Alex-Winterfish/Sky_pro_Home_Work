from trace import Trace

file_path_json = "../data/operations.json"
file_path_csv = "../data/transactions.csv"
file_path_excel = "../data/transactions_excel.xlsx"
from src.utils import get_transaction_data
from src.dataframe_processing import csv_processing, excel_processing
from src.processing import filter_by_state, sort_by_date
from src.transaction_search import user_search
from src.witget import get_date, mask_account_card

def main():


    user_file_select = input(
        " Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        " Выберите необходимый пункт меню:\n "
        "1. Полоучить информацию о транзакциях из JSON-файла\n "
        "2. Полоучить информацию о транзакциях из CSV-файла\n "
        "3. Полоучить информацию о транзакциях из XLSX-файла\n "
        "ввод: "
    )

    if user_file_select == "1":  # получаем список транзакций из json файла
        print("Для обработки выбран json-файл")
        transaction_list = get_transaction_data(file_path_json)

    elif user_file_select == "2":  # получаем список транзакций из csv файла
        print("Для обработки выбран csv-файл")
        transaction_list = csv_processing(file_path_csv)

    elif user_file_select == "3":  # получаем список транзакций из excel файла
        print("Для обработки выбран excel-файл")
        transaction_list = excel_processing(file_path_excel)

    while True:  # цикл для ввода пользователем фильтра для операций
        # пока пользователь не введет статус операции, запращиваем ввод

        user_state_select = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтрации статусы:\n"
            "EXECUTED, CANCELED, PENDING\n"
            "ввод: "
        ).upper()

        if user_state_select in [
            "EXECUTED",
            "CANCELED",
            "PENDING",
        ]:  # если пользователь ввел статус операции, прерываем цыкл
            break
        else:
            print(f"Статус операции {user_state_select} недоступен")
    filtered_data = filter_by_state(
        transaction_list, state=user_state_select
    )  # фильтруем список по зпданному статусу
    print(f"Операции отфильтрованы по статусу {user_state_select}")


    user_sort_option = input("Отсортировать операции по дате? Да/нет\n Пользователь: ")

    if user_sort_option.upper() == "ДА":  # цикл для сортировки по дате

        user_sorting = input(
            "Отсортировать по возрастанию или по убыванию?\n Пользователь: "
        )
        if user_sorting.upper() == "ПО ВОЗРАСТАНИЮ":
            sort_options = False
            filtered_data = sort_by_date(filtered_data, sort_options)
        else:
            filtered_data = sort_by_date(filtered_data)

    user_sort_option = input(
        "Отсортировать список транзакций по определенному слову в описании? Да/нет\n Пользователь: "
    )
    if user_sort_option.upper() == "ДА":
        user_search_word = input("Введите слово для сортировки:\n Пользователь: ")
        filtered_data = user_search(filtered_data, user_search_word)

    if filtered_data == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:

        print(
            f"Распечатываю итоговый список транзакций...\n"
            f"Всего банковских операций: {len(filtered_data)}\n\n"
        )
        for i in range(len(filtered_data)):
            if filtered_data[i].get("description") == "Открытие вклада":
                print (
                    f"{get_date(filtered_data[i].get('date'))} {filtered_data[i].get('description')}\n"
                    f"{mask_account_card(filtered_data[i].get('to'))}\n"
                    f"Сумма: {filtered_data[i].get('amount')} {filtered_data[i].get('currency_name')}\n\n"
                )
            else:
                print (
                    f"{get_date(filtered_data[i].get('date'))} {filtered_data[i].get('description')}\n"
                    f"{mask_account_card(filtered_data[i].get('from'))} -> {mask_account_card(filtered_data[i].get('to'))}\n"
                    f"Сумма: {filtered_data[i].get('amount')} {filtered_data[i].get('currency_name')}\n\n"
                )


if __name__ == "__main__":

    print(main())
