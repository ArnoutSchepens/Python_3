
def return_day(day):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }

    current_day = days.get(day)
    if current_day:
        return current_day
    return None

print(return_day(8))