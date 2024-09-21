# Пакет обработки банковских операций
Пакет состоит из следующих модулей:
- masks - модуль накладывает маски на номера карт или номера счетов
- witget - модуль накладывает маски на счета и карты, а так же выводит дату в требуемом формате
- processing - модуль принимает список словарей. Выводит список словарей с заданным ключом, сортирует список словарей дате
- generators - модуль принимает входной список словарей с транзакциями и выводит по запросу транзакции с заданной валютой, выводит по запросу вид транзакций из входного списка, генерирует номера карт в заданном диапазоне.
- decorators - модуль содержит декоратор log, который выполняет логирование функций
## Примеры работы функций
Функция transaction_descriptions выводит тип транзакции
```
transaction_type = transaction_descriptions(transactions)

#transactions - список транзакций

print(next(transaction_type))
print(next(transaction_type))
print(next(transaction_type))
print(next(transaction_type))
print(next(transaction_type))

#вывод типов транзакций 

Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации
```
Функция filter_by_currency выводит по запросу тип транзакции с заданной валютой
```
currency_type = filter_by_currency(transactions, "USD")
#USD - параметр, который определяет валюту транзакции
print(next(currency_type))
print(next(currency_type))
print(next(currency_type))

#вывод транзакции

{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
{'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}

```
Функция card_number_generator генерирует номера карт в заданном диапазоне
```
card_nunber = card_number_generator(19287398,19287410)

#функция генерирует морема карт в диапазоне от 19287398 до 19287410

print(next(card_nunber))
print(next(card_nunber))
print(next(card_nunber))

#вывод номеров карт

0000 0000 1928 7398
0000 0000 1928 7399
0000 0000 1928 7400
```
Декоратор log. Может принимать необязательный аргумент в виде строки с именем файла для записи лога функции. Если аргумент не передается, логи передаются в консоль.
## Установка:
- требования:
```Python 3.12+```
- Клонируйте репозиторий:
```git@github.com:Alex-Winterfish/Sky_pro_Home_Work.git```
- Установите зависимости
```pip install -r requirements.txt```

## тестирование
Написаны тесты для модулей masks, processing, witget, decorators
Для запуска тестов:
```poetry run pytest --cov```

