import pytest


@pytest.fixture
def test_card_number_1():
    return 3287682873647732873


@pytest.fixture
def test_card_type_number_1():
    return "Visa Gold 5999414228426353"


@pytest.fixture
def test_list_of_dic_1():  # набор с разными параметрами state и разными датами
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def test_list_of_dic_2():  # набор с одинаковыми параметрами state и одинаковыми датами
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def test_list_of_dic_3():  # набор для тестирования с ключами различных классов и разными форматами дат
    return [
        {"id": 41428829, "state": "", "date": "2019/07/03T18:35:29.512364"},
        {"id": 939719570, "state": 1, "date": "2018.06.30T02:08:58.425572"},
        {"id": 594226727, "state": True, "date": "2018/09/12T21:27:25.241689"},
        {"id": 615064591, "state": " ", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def test_list_of_dic_4():  # набор для тестирования с ключами различных классов и без дат
    return [
        {"id": 41428829, "state": "", "date": ""},
        {"id": 939719570, "state": 1, "date": ""},
        {"id": 594226727, "state": True, "date": ""},
        {"id": 615064591, "state": " ", "date": ""},
    ]


@pytest.fixture
def test_date_1():
    return "2019/07/03T18:35:29.512364"


@pytest.fixture
def test_date_2():
    return "2019-07-03T18:35:29.512364"


@pytest.fixture
def test_date_3():
    return "2019.07.03T18:35:29.512364"


@pytest.fixture
def test_date_4():
    return ""


@pytest.fixture
def test_transaction_1():
    return [
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
