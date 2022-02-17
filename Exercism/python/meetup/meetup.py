from calendar import Calendar, day_name
from datetime import date

DAYS = dict(zip(day_name, range(7)))
WEEK_DAYS = dict(zip(['1st', '2nd', '3rd', '4th', '5th'], range(5)))
monthdates = Calendar().itermonthdates


class MeetupDayException(Exception):
    pass


def meetup(year: int, month: int, schedule: str, day_of_week: str) -> date:
    days = [d for d in monthdates(year, month)
            if d.weekday() == DAYS[day_of_week] and d.month == month]

    try:
        return [d for d in days if d.day in range(13, 20)][0] \
            if schedule == 'teenth' else days.pop() \
            if schedule == 'last' else days[WEEK_DAYS[schedule]]
    except Exception:
        raise MeetupDayException("There's no such day!")
