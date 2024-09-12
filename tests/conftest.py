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
