from collections import defaultdict
from itertools import count
from logging import raiseExceptions

from src.dataframe_processing import csv_processing

def user_search(transaction_list:list, search_str)->list:
    '''Функция выполняет поиск во входном списке словарей опреаци по заданному слову'''
    output_list = list() #переменная для накопления найденных транзакций
    import re

    for i in range(len(transaction_list)): #цикл для поиска транзакций

        search_pattern = re.search(f'{search_str}', transaction_list[i].get('description'), flags = re.I)
        if search_pattern is not None:
            output_list.append(transaction_list[i].get('description'))
    if output_list == []:
        return 'транзакции не найдены'
    else:
        return output_list

def transaction_discripption(transaction_list:list)->list:
    '''Функция принимает список с транзакциями, возвращает список со всеми типами транзакций'''
    output_list = list()
    for i in range(len(transaction_list)):
        if transaction_list[i].get("description") != "":
            output_list.append(transaction_list[i].get("description"))
    output_list = set(output_list)
    output_list = list(output_list)

    return output_list

def transaction_count(transaction_list:list, transaction_type:list)->dict:

    from collections import Counter
    list_of_transaction = list()
    for i in range(len(transaction_list)):
        if transaction_list[i].get("description") != "":
            list_of_transaction.append(transaction_list[i].get("description"))
    counted_transactions = Counter(list_of_transaction)
    output_dict = dict()
    for types in transaction_type:
        output_dict[types] = counted_transactions[types]



    return output_dict






if __name__ == '__main__':
    filepath = "../data/transactions.csv"

    #input_string = input('введите слово для поиска')
    input_list = csv_processing(filepath)
    trans_type = transaction_discripption(input_list)
    #['Открытие вклада', 'Перевод с карты на карту', 'Перевод организации']

    print(transaction_count(input_list, trans_type))