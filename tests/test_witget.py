import pytest

from src.witget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_int, output_string",
    [
        (70007922896063612342323, "7000 79** **** **** ***2 323"),
        (7000792289606361, "7000 79** **** 6361"),
        (76878127361, "7687 81*7 361"),
        (353587938, "номер карты слишком короткий для наложения маски"),
    ],
)
def test_mask_account_card(input_int, output_string):
    assert mask_account_card(input_int) == output_string