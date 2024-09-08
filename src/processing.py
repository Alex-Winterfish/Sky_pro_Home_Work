def filter_by_state(a: list, state = 'EXECUTED' )-> list:
    """Функция принимает список словарей и параметр. Возвращает список словарей с ключами, соответствующими параметру"""
    b=list()
    for i in range(len(a)): # цикл для поиска элемента словаря с ключом, соответствующему параметру
        if a[i].get('state') == state:
            b.append(a[i])
    return(b)

from datetime import datetime
def sort_by_date(a:list, sort_option = True)->list:
    #Функция для сортировки списка словаряей по дате, по умолчанию список сортируется по убыванию
    return sorted(a, key=lambda a: datetime.strptime(a['date'][0:10], "%Y-%m-%d").date(), reverse = sort_option)
