from datetime import datetime, timedelta
from copy import deepcopy

users = [
    {'name': 'Igor', 'birthday': datetime(2022, 8, 23)},
    {'name': 'Anna', 'birthday': datetime(2022, 8, 24)},
    {'name': 'Dima', 'birthday': datetime(2022, 8, 25)},
    {'name': 'Alex', 'birthday': datetime(2022, 8, 26)},
    {'name': 'Max', 'birthday': datetime(2022, 8, 27)},
    {'name': 'Jack', 'birthday': datetime(2022, 8, 28)},
    {'name': 'Hilda', 'birthday': datetime(2022, 8, 29)},
    {'name': 'Hilda2', 'birthday': datetime(2022, 8, 24)},
    {'name': 'Rich', 'birthday': datetime(2022, 8, 23)},
]
weakdays = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': []
}
WEEK_DAYS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday'
}


def dict_print(dictionary):
    for key, value in dictionary.items():
        if len(value) > 0:
            value = ', '.join(value)
            print(key, ':', value)


def get_birthdays_per_week(users):

    weakdays_1 = deepcopy(weakdays)
    weakdays_2 = deepcopy(weakdays)

    constant_time = datetime.now()

    for user in users:
        birth_date = user['birthday'].date().replace(year=constant_time.year)
        days_diff = birth_date - constant_time.date()
        week_day = WEEK_DAYS.get(birth_date.weekday(), 'Monday')
        date_start_1week = (constant_time -
                            (timedelta(days=constant_time.weekday() + 2))).date()
        date_end_1week = date_start_1week + timedelta(days=6)
        date_end_2week = date_end_1week + timedelta(days=7)
        if constant_time.weekday() == 0 and (constant_time.date() - timedelta(days=1) == birth_date or constant_time.date() - timedelta(days=2) == birth_date):
            weakdays_1['Monday'].append(i['name'])
        if days_diff.days <= 6 and days_diff.days >= 0:
            if birth_date >= date_start_1week and birth_date <= date_end_1week:
                weakdays_1[week_day].append(user['name'])
            elif birth_date >= date_end_1week and birth_date <= date_end_2week:
                weakdays_2[week_day].append(user['name'])
    dict_print(weakdays_1)
    dict_print(weakdays_2)


get_birthdays_per_week(users)
