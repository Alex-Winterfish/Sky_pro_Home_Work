from re import search

from openpyxl.styles.builtins import output

"Counter({'Перевод с карты на карту': 285, 'Открытие вклада': 97, 'Перевод организации': 70, 'Перевод со счета на счет': 47, '': 1})"

from src.dataframe_processing import excel_processing, csv_processing
from src.utils import get_transaction_data

def user_search(transaction_list:list)->list:
    input_string = input('введите слово для поиска')
    output_list = list()
    import re
    pattern = re.compile(r'\D*')
    search_pattern = pattern.finditer(input_string)
    for i in range(len(transaction_list)):
        if search_pattern(transaction_list[i].get('description')):
            output_list.append(transaction_list[i].get('description'))

    print(output_list)

from collections import Counter

def descriptoin_count(input_list):
    output_list = list()
    for description in input_list.values():
        output_list.append(description)
    counted = Counter(output_list)
    return counted

if __name__ == '__main__':
    filepath = "../data/transactions.csv"

    input_list = csv_processing(filepath)

    user_search(input_list)