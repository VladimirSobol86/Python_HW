import argparse

def _is_leap(year: int) -> bool:
    return not year%4 and year%100 or not year%400

def check_date(date:str) -> bool | str:
    separator = [sep for sep in date if not sep.isdigit()]
    if len(set(separator)) > 1:
        return 'Ошибка ввода'
    else:
        separator = separator[0]
    day, month, year = list(map(int, date.split(separator)))
    months = {1:31, 2:29 if _is_leap(year) else 28, 3:31, 4:30,
             5:31, 6: 30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if 0 < year < 10000:
        if 0 < month < 13:
            if 0 < day <= months[month]:
                return True
    return False

parser = argparse.ArgumentParser(description='Check date.')
parser.add_argument('date', type=str, help='Date to check in the format dd-mm-yy')
args = parser.parse_args()
print(check_date(args.date))