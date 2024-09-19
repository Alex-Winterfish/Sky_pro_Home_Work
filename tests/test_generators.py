import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.mark.parametrize(
    "input_transaction_list,expected_output_1",
    [
        (
            (
                [
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
            ),
            [
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
            ],
        ),
    ],
)
def test_filter_by_currency_1(input_transaction_list, expected_output_1):
    "Функцция проверяет правильность выборки операций с параметром USD"
    result = list(filter_by_currency(input_transaction_list, "USD"))
    assert result == expected_output_1


@pytest.mark.parametrize(
    "input_transaction_list,expected_output_2",
    [
        (
            (
                [
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
            ),
            [
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
            ],
        ),
    ],
)
def test_filter_by_currency_2(input_transaction_list, expected_output_2):
    "Функцция проверяет правильность выборки операций с параметром RUB"
    result = list(filter_by_currency(input_transaction_list, "RUB"))
    assert result == expected_output_2


@pytest.mark.parametrize(
    "input_transaction_list,expected_output_3",
    [
        (
            (
                [
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
            ),
            [],
        ),
    ],
)
def test_filter_by_currency_3(input_transaction_list, expected_output_3):
    "Функцция проверяет правильность выборки операций с параметром, отсутствующем в списке"
    result = list(filter_by_currency(input_transaction_list, "JPY"))
    assert result == expected_output_3


@pytest.mark.parametrize("input_transaction_list,expected_output_4", [([], [])])
def test_filter_by_currency_4(input_transaction_list, expected_output_4):
    "Функцция отсутствие ошибки при пустом входном списке"
    result = list(filter_by_currency(input_transaction_list, "JPY"))
    assert result == expected_output_4


""""@pytest.mark.parametrize(
    "input_transaction_list, expected_transaction_1", [
        (
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {
                            "amount": "9824.07",
                            "currency": {
                                "name": "USD",
                                "code": "USD"
                            }
                        },
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702"
                    },
                    {
                        "id": 142264268,
                        "state": "EXECUTED",
                        "date": "2019-04-04T23:20:05.206878",
                        "operationAmount": {
                            "amount": "79114.93",
                            "currency": {
                                "name": "USD",
                                "code": "USD"
                            }
                        },
                        "description": "Перевод со счета на счет",
                        "from": "Счет 19708645243227258542",
                        "to": "Счет 75651667383060284188"
                    },
                    {
                        "id": 873106923,
                        "state": "EXECUTED",
                        "date": "2019-03-23T01:09:46.296404",
                        "operationAmount": {
                            "amount": "43318.34",
                            "currency": {
                                "name": "руб.",
                                "code": "RUB"
                            }
                        },
                        "description": "Перевод со счета на счет",
                        "from": "Счет 44812258784861134719",
                        "to": "Счет 74489636417521191160"
                    },
                    {
                        "id": 895315941,
                        "state": "EXECUTED",
                        "date": "2018-08-19T04:27:37.904916",
                        "operationAmount": {
                            "amount": "56883.54",
                            "currency": {
                                "name": "USD",
                                "code": "USD"
                            }
                        },
                        "description": "Перевод с карты на карту",
                        "from": "Visa Classic 6831982476737658",
                        "to": "Visa Platinum 8990922113665229"
                    },
                    {
                        "id": 594226727,
                        "state": "CANCELED",
                        "date": "2018-09-12T21:27:25.241689",
                        "operationAmount": {
                            "amount": "67314.70",
                            "currency": {
                                "name": "руб.",
                                "code": "RUB"
                            }
                        },
                        "description": "Перевод организации",
                        "from": "Visa Platinum 1246377376343588",
                        "to": "Счет 14211924144426031657"
                    }
                ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        )
    ]
)
def test_transaction_descriptions(input_transaction_list, expected_transaction_1):
    result_transaction = list(transaction_descriptions(input_transaction_list))
    assert result_transaction == expected_transaction_1"""


def test_transaction_descriptions(test_transaction_1):
    output_trans = transaction_descriptions(test_transaction_1)
    assert next(output_trans) == "Перевод организации"
    assert next(output_trans) == "Перевод со счета на счет"
    assert next(output_trans) == "Перевод со счета на счет"
    assert next(output_trans) == "Перевод с карты на карту"
    assert next(output_trans) == "Перевод организации"


@pytest.mark.parametrize(
    "start_gen, end_gen, num_list",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        )
    ],
)
def test_card_number_generator_1(start_gen, end_gen, num_list):
    result = list(card_number_generator(start_gen, end_gen))
    assert result == num_list


@pytest.mark.parametrize(
    "start_gen, end_gen, num_list",
    [
        (
            9999999999999995,
            9999999999999999,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        )
    ],
)
def test_card_number_generator_2(start_gen, end_gen, num_list):
    result = list(card_number_generator(start_gen, end_gen))
    assert result == num_list
