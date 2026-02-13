from datetime import datetime as dt

def get_days_from_today(date: str) -> int | None:
    try:
        date_obj = dt.strptime(date, "%Y-%m-%d")
        today = dt.today()
        delta = today - date_obj
        return delta.days
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")

days_from_today = get_days_from_today('2026-01-01')
print(days_from_today)    

days_from_today = get_days_from_today('2026-01-32')
print(days_from_today)