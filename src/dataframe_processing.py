import csv

filepath = "../data/transactions.csv"
def csv_processing(filepath:str)->list:
    output_list = list()

    with open(filepath, encoding="utf-8") as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for row in csv_reader:
            output_list.append(row)
            next(csv_reader)

    return output_list


#print(csv_processing(filepath))
#print(f'число элемнтов списка {len(csv_processing(filepath))}')

filepath_excel = '../data/transactions_excel.xlsx'
def excel_processing(filepath:str):
    import pandas as pd
    transaction_data_xls = pd.read_excel(filepath)
    x = "id"
    return transaction_data_xls[x][0]

print(excel_processing(filepath_excel))