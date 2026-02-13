import datetime
now = datetime.datetime.now()
today = datetime.date.today()
date = datetime.date(2024, 6, 1)
print(now)
print(today)


from datetime import datetime

day_of_year = datetime.now().strftime('%j')
print(f"Поточний день року: {day_of_year}")

# Приклад для конкретної дати
specific_date = datetime(2026, 1, 15)
print(f"15 січня 2026 - це {specific_date.strftime('%j')} день року")