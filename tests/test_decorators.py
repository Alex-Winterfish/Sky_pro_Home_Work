from src.decorators import log


def test_my_division_1(capsys):
    # функция проверяет вывод в консоль при положительных аргументах
    @log()
    def my_division(x, y):
        return x / y

    my_division(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "Функция my_division: результат выполнения:2.0\n"


def test_my_division_2(capsys):
    # функция проверяет вывод в консоль ошибки при делении на ноль
    @log()
    def my_division(x, y):
        return x / y

    my_division(4, 0)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Функция my_division: ошибка: division by zero, входные данные (4, 0)\n"
    )
