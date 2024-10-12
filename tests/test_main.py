from unittest.mock import patch
from src.main import main


@patch("src.main.user_search_word")
@patch("src.main.user_sorting_range")
@patch("src.main.user_sorting")
@patch("src.main.user_sort_option")
@patch("src.main.user_state_select")
@patch("src.main.user_file_select")
def test_main(
    mock_file_select,
    mock_state_select,
    mock_sort_option,
    mock_sorting,
    mock_sorting_range,
    mock_user_search_word,
    capsys,
):
    mock_file_select.return_value = "2"
    mock_state_select.return_value = "CANCELED"
    mock_sort_option.return_value = "ДА"
    mock_sorting.return_value = "ПО ВОЗРАСТАНИЮ"
    mock_sorting_range.return_value = "ДА"
    mock_user_search_word.return_value = "ОТКРЫТИЕ"
    main()
    captured = capsys.readouterr()
    assert (
        captured.out
        == f"Для обработки выбран csv-файл\nОперации отфильтрованы по статусу CANCELED\n"
        f"Распечатываю итоговый список транзакций...\nВсего банковских операций: 10\n\n\n"
        f"2020.08.31 Открытие вклада\nСчет **5859\nСумма: 14438 Ruble\n\n\n2020.09.12 Открытие вклада"
        f"\nСчет **4669\nСумма: 15585 Peso\n\n\n2020.10.15 Открытие вклада\nСчет **4889\nСумма: 15811 Real"
        f"\n\n\n2021.02.01 Открытие вклада\nСчет **5683\nСумма: 23789 Peso\n\n\n2021.02.22 Открытие вклада"
        f"\nСчет **6967\nСумма: 30172 Dollar\n\n\n2021.09.08 Открытие вклада\nСчет **2702"
        f"\nСумма: 15359 Euro\n\n\n2022.09.19 Открытие вклада\nСчет **8369\nСумма: 28646 Rupiah"
        f"\n\n\n2023.03.13 Открытие вклада\nСчет **9840\nСумма: 15427 Rupiah\n\n\n2023.09.08 Открытие вклада"
        f"\nСчет **4769\nСумма: 24237 Hryvnia\n\n\n2023.10.19 Открытие вклада\nСчет **9858\nСумма: 28133 Krona\n\n\n"
    )
