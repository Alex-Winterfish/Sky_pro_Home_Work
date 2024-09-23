def log(filename: str = None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            # обработка исключений
            try:
                result = func(*args, *kwargs)
                # условие для записи в файл
                if filename != None:

                    with open(f"{filename}", "a") as file:
                        file.write(
                            f"\nФункция {func.__name__}: результат выполнения:{result}"
                        )
                # условие для вывода в консоль
                else:
                    print(f"Функция {func.__name__}: результат выполнения:{result}")
            except Exception as e:
                # условие для записи ошибки в файл
                if filename != None:

                    with open(f"{filename}", "a") as file:
                        file.write(
                            f"\nФункция {func.__name__}: ошибка:{e}, входные данные {*args, *kwargs}"
                        )
                # условие для вывода ошибки в консоль
                else:
                    print(
                        f"Функция {func.__name__}: ошибка: {e}, входные данные {*args, *kwargs}"
                    )

        return wrapper

    return my_decorator
