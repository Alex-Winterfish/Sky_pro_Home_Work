import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "input_int, output_string",
    [
        (70007922896063612342323, "7000 79** **** **** ***2 323"),
        (7000792289606361, "7000 79** **** 6361"),
        (76878127361, "7687 81*7 361"),
        (353587938, "номер карты слишком короткий для наложения маски"),
    ],
)
def test_get_mask_card_number_1(input_int, output_string):
    assert get_mask_card_number(input_int) == output_string


def test_get_mask_card_number_2(test_card_number_1):
    assert get_mask_card_number(test_card_number_1) == "3287 68** **** ***2 873"


@pytest.mark.parametrize(
    "input_int, output_string",
    [
        (70007922896063612342323, "**2323"),
        (7000792289606361, "**6361"),
        (76878127361, "**7361"),
        (7938, "номер счета слишком короткий для наложения маски"),
    ],
)
def test_get_mask_account_1(input_int, output_string):
    assert get_mask_account(input_int) == output_string


def test_get_mask_account_2(test_card_number_1):
    assert get_mask_account(test_card_number_1) == "**2873"
