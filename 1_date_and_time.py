import datetime
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    date_format = '%d.%m.%Y'
    today = datetime.date.today()
    yesterday = datetime.date.today() - datetime.timedelta(1)
    days_30_before = datetime.date.today() + datetime.timedelta(30)
    print(today.strftime(date_format))
    print(yesterday.strftime(date_format))
    print(days_30_before.strftime(date_format))



def str_2_datetime(date_string):
    date_converted = datetime.datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date_converted

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234"))
