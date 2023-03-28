from datetime import datetime

def add_years_to_date(original_date: datetime, years_to_add: int) -> datetime:
    return original_date.replace(year=original_date.year + years_to_add)