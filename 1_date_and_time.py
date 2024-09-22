"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    from datetime import datetime, timedelta
    print(datetime.now().strftime('%d-%m-%Y'))
    print((datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y'))
    print((datetime.now() - timedelta(days=30)).strftime('%d-%m-%Y'))


def str_2_datetime(date_string,):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    from datetime import datetime, timedelta
    date_string = "01/01/20 12:10:03.234567"
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print(date_dt)
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
