import pytest

from src.masks import get_mask_card_number

def test_get_mask_card_number():
    assert get_mask_card_number(70007922896063612342323) == '7000 79** **** **** ***2 323'
    assert get_mask_card_number(7000792289606361) == '7000 79** **** 6361'
    assert get_mask_card_number(76878127361) == '7687 81*7 361'
    assert get_mask_card_number(353587938) == 'номер карты слишком короткий для наложения маски'
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number()
    assert str(exc_info) == "Номер карты не введен"