import datetime


def time_(y, m, d):
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    result = [y - year, m - month, d - day]
    return result


print(time_(2023, 7, 22))
