# Задание №1
# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)
FORMAT = '{asctime:20} - {levelname: 5} - {name}: {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='logger.log', filemode='w', level=logging.DEBUG)

def division(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError as exc:
        logger.error(msg = f'{exc}')
        
# if __name__ == "__main__":
#     division(100, 0)
#     division(1, 1)
#     division(20, 0)
    
# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату
def data_in_text(st:str):
    isodate = datetime.strptime(st, '1-й четверг ноября')
    st = st.split()
    dict_m = {'ноября': 11, 'декабря': 12, 'мая': 5}
    st[2] = dict_m[st[2]]
    dict_w_d = {'четверг': 3, 'среда': 2}
    st[1] = dict_w_d[st[1]]
    res = ''
    for symb in st[0]:
        if symb.isdigit():
            res+= symb
    st[0] = int(res)
    my_date = datetime(year=2023, month=st[2], day=st[0])
    cur_number_weekday = 1
    while my_date.weekday() != st[1] and cur_number_weekday != st[0]:
        day_ = my_date.day
        day_ +=  1
        my_date.replace(day=day_)
        if my_date.weekday() == st[1]:
            cur_number_weekday += 1        
    print(my_date, st, my_date.weekday())
    
data_in_text('1-й четверг ноября')