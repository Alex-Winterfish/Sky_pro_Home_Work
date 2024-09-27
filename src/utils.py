import os


def get_transaction_data(file_path:str):
    import os
    import json
    with open((os.path.abspath(file_path))) as f:
        data = json.load(f)
    return data

file_path = ('D:\Python Projects\Home_work\data\operation.json')

print(get_transaction_data(file_path))

