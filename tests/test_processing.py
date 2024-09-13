from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_1(test_list_of_dic_1):
    """Функция тестирует корректный вывод словарей с параметром EXECUTED"""
    assert filter_by_state(test_list_of_dic_1) == [
        {
            "date": "2019-07-03T18:35:29.512364",
            "id": 41428829,
            "state": "EXECUTED",
        },
        {
            "date": "2018-06-30T02:08:58.425572",
            "id": 939719570,
            "state": "EXECUTED",
        },
    ]


def test_filter_by_state_2(test_list_of_dic_2):
    """Функция тестирует корректный вывод при отсутствии заданного параметра в списке словарей"""
    assert filter_by_state(test_list_of_dic_2) == []


def test_filter_by_state_3(test_list_of_dic_1):
    """Функция тестирует корректный вывод словарей с параметром CANCELED"""
    assert filter_by_state(test_list_of_dic_1, state="CANCELED") == [
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
    ]


def test_filter_by_state_4(test_list_of_dic_3):
    """Функция тестирует корректный вывод при пустом ключе state в словаре"""
    assert filter_by_state(test_list_of_dic_3) == []


def test_sort_by_date_1(test_list_of_dic_1):
    """Функция тестирует сортировку по убыванию даты"""
    assert sort_by_date(test_list_of_dic_1) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]


def test_sort_by_date_2(test_list_of_dic_1):
    """Функция тестирует сортировку по возрастанию даты"""
    assert sort_by_date(test_list_of_dic_1, sort_option=False) == [
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]


def test_sort_by_date_3(test_list_of_dic_2):
    """Функция тестирует сортировку словарей с одинаковыми датами"""
    assert sort_by_date(test_list_of_dic_2) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 939719570, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 594226727, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 615064591, "state": "CANCELED"},
    ]


def test_sort_by_date_4(test_list_of_dic_3):
    """Функция тестирует сортировку словарей разными форматами дат"""
    assert sort_by_date(test_list_of_dic_3) == [
        {"date": "2019/07/03T18:35:29.512364", "id": 41428829, "state": ""},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": " "},
        {"date": "2018/09/12T21:27:25.241689", "id": 594226727, "state": True},
        {"date": "2018.06.30T02:08:58.425572", "id": 939719570, "state": 1},
    ]


def test_sort_by_date_5(test_list_of_dic_4):
    """Функция тестирует сортировку словарей без даты"""
    assert sort_by_date(test_list_of_dic_4) == [
        {"id": 41428829, "state": "", "date": ""},
        {"id": 939719570, "state": 1, "date": ""},
        {"id": 594226727, "state": True, "date": ""},
        {"id": 615064591, "state": " ", "date": ""},
    ]
