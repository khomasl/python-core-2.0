from datetime import datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


start_date = string_to_date("2024.03.26")  # Перетворення рядка на дату - Вівторок=1
next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
print(next_monday)
next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
print(next_friday)