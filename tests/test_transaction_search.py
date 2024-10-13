from src.transaction_search import user_search, transaction_count


def test_user_search_1(test_transaction_1, input_string_1):
    assert user_search(test_transaction_1, input_string_1) == [
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"code": "USD", "name": "USD"},
            },
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"code": "USD", "name": "USD"},
            },
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"code": "RUB", "name": "руб."},
            },
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        },
        {
            "date": "2018-08-19T04:27:37.904916",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "id": 895315941,
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"code": "USD", "name": "USD"},
            },
            "state": "EXECUTED",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"code": "RUB", "name": "руб."},
            },
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_user_search_2(test_transaction_1, input_string_2):
    assert user_search(test_transaction_1, input_string_2) == "транзакции не найдены"


def test_transaction_count_1(test_transaction_1, test_transaction_list_1):
    assert transaction_count(test_transaction_1, test_transaction_list_1) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
    }
