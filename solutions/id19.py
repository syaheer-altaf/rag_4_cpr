def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_first_sundays(start_year, end_year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    current_day_of_week = 1
    sunday_count = 0
    
    
    for year in range(1900, start_year):
        current_day_of_week += 366 if is_leap_year(year) else 365
        current_day_of_week %= 7

    for year in range(start_year, end_year + 1):
        for month in range(12):
            if current_day_of_week == 0:
                sunday_count += 1
            current_day_of_week += days_in_month[month]
            if month == 1 and is_leap_year(year):
                current_day_of_week += 1
            current_day_of_week %= 7

    return sunday_count

result = count_first_sundays(1901, 2000)
print(result)