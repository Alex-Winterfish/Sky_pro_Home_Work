from trace import Trace

file_path_json = "../data/operations.json"
file_path_csv = "../data/transactions.csv"
file_path_excel = "../data/transactions_excel.xlsx"
def main():
    from src.utils import get_transaction_data
    from src.dataframe_processing import csv_processing, excel_processing
    from src.processing import filter_by_state
    user_input = input(
        " Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        " Выберите необходимый пункт меню:\n "
        "1. Полоучить информацию о транзакциях из JSON-файла\n "
        "2. Полоучить информацию о транзакциях из CSV-файла\n "
        "3. Полоучить информацию о транзакциях из XLSX-файла\n "
        "ввод: "
    )

    if user_input =="1": # получаем список транзакций из json файла
        print("Для обработки выбран json-файл")
        transaction_list = get_transaction_data(file_path_json)

    elif user_input == "2": # получаем список транзакций из csv файла
        print("Для обработки выбран csv-файл")
        transaction_list = csv_processing(file_path_csv)

    elif user_input == "3":# получаем список транзакций из excel файла
        print("Для обработки выбран excel-файл")
        transaction_list = excel_processing(file_path_excel)

    while True:

        state = input("Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтрации статусы:\n"
                  "EXECUTED, CANCELED, PENDING\n"
                  "ввод: ").upper()

        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f"Статус операции {state} недоступен")
    output_data = filter_by_state(transaction_list, state=state)
    print(f'Операции отфильтрованы по статусу {state}')



    return output_data




if __name__ == "__main__":

    file_path = "../data/operations.json"
    print(main())