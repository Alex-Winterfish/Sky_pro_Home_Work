import pytest

from src.witget import get_date, mask_account_card


def test_mask_account_card(test_card_type_number_1):
    assert mask_account_card(test_card_type_number_1) == "Visa Gold 5999 41** **** 6353"


@pytest.mark.parametrize(
    "input_string, output_string",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 98378978", "Счет **8978"),
        ("Счет 9837", "Номер слишком короткий для наложения маски"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold 5967887563", "Номер слишком короткий для наложения маски"),
    ],
)
def test_mask_account_card_2(input_string, output_string):
    assert mask_account_card(input_string) == output_string


def test_get_date_1(test_date_1):
    """Функция проверяет корректность вывода даты"""
    assert get_date(test_date_1) == "2019.07.03"


def test_get_date_2(test_date_2):
    """Функция проверяет корректность вывода даты"""
    assert get_date(test_date_2) == "2019.07.03"


def test_get_date_3(test_date_3):
    """Функция проверяет корректность вывода даты"""
    assert get_date(test_date_3) == "2019.07.03"


def test_get_date_4(test_date_4):
    """Функция проверяет корректность вывода даты"""
    assert get_date(test_date_4) == "0001.01.01"
