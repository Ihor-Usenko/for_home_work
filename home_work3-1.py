from datetime import datetime
input_date = '1970-04-03'


def get_days_from_today(date) -> int:
    try:
        input_date_datetime = \
            (datetime.strptime(input_date, '%Y-%m-%d').date())
        # create datetime var
        date_today = (
            datetime.today().date())  # get today's date
        difference_day = (
            (input_date_datetime - date_today).days)
        return difference_day
    except ValueError as m:
        print(m)


print(get_days_from_today(input_date))
