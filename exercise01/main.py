from datetime import datetime

def get_days_from_today(date):
    date_now = datetime.now().date()
    input_date = datetime.strptime(date, "%Y-%m-%d").date()
    return (date_now - input_date).days

print(get_days_from_today("2024-11-26"))