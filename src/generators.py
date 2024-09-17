import random

def filter_by_currency(transactions_list:list, currency: str):
    "Функция сортирует входной список выводит список транзакций с"
    for i in range(len(transactions_list)):
        if transactions_list[i].get("operationAmount").get("currency").get("code") == currency:
            yield transactions_list[i]

def transaction_descriptions(transactions_list:list):
    i = 0
    while True:
        yield  transactions_list[i].get("description")
        i+=1

def card_number_generator(start,end):
    while True:
        a = random.randint(start, end)
        output_list = list()
        list_of_num = (a//10**12%10**4,a//10**8%10**4,a//10**4%10**4,a%10**4)
        for i in range(4):
            if len(str(list_of_num[i])) < 4:
                output_list.append((4-len(str(list_of_num[i])))*"0" + str(list_of_num[i]))
            else:
                output_list.append(str(list_of_num[i]))
        yield " ".join(output_list)





in_list = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

filt_cur = filter_by_currency(in_list,"RUB")
print(next(filt_cur))
print(next(filt_cur))






trans_des = transaction_descriptions(in_list)
print(next(trans_des))
print(next(trans_des))
print(next(trans_des))
print(next(trans_des))
print(next(trans_des))

card_num = card_number_generator(1,9999999999999999)
print(next(card_num))
print(next(card_num))
print(next(card_num))
print(next(card_num))
print(next(card_num))
print(next(card_num))
print(next(card_num))