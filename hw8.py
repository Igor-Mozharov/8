from datetime import datetime, timedelta

users = [
    {'name': 'Igor', 'birthday': datetime(2022, 8, 22)},
    {'name': 'Anna', 'birthday': datetime(2022, 8, 24)},
    {'name': 'Dima', 'birthday': datetime(2022, 8, 23)},
    {'name': 'Alex', 'birthday': datetime(2022, 8, 26)},
    {'name': 'Max', 'birthday': datetime(2022, 8, 25)},
    {'name': 'Jack', 'birthday': datetime(2022, 8, 26)},
    {'name': 'Hilda', 'birthday': datetime(2022, 8, 27)},
    {'name': 'Hilda2', 'birthday': datetime(2022, 8, 28)},
    {'name': 'Rich', 'birthday': datetime(2022, 8, 29)},
]


def get_birthdays_per_week(users):
    weakdays_1 = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }
    weakdays_2 = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }
    constant_time = datetime.now()  # Сьогодні
    for i in users:
        birth_date = i['birthday'].date().replace(year=constant_time.year)
        days_diff = birth_date - constant_time.date()
        if constant_time.weekday() == 0 and (constant_time.date() - timedelta(days=1) == birth_date or constant_time.date() - timedelta(days=2) == birth_date):
            weakdays_1['Monday'].append(i['name'])
        if days_diff.days <= 6 and days_diff.days >= 0:
            if birth_date.weekday() >= constant_time.weekday():
                if birth_date.weekday() == 0:
                    weakdays_1['Monday'].append(i['name'])
                elif birth_date.weekday() == 1:
                    weakdays_1['Tuesday'].append(i['name'])
                elif birth_date.weekday() == 2:
                    weakdays_1['Wednesday'].append(i['name'])
                elif birth_date.weekday() == 3:
                    weakdays_1['Thursday'].append(i['name'])
                elif birth_date.weekday() == 4:
                    weakdays_1['Friday'].append(i['name'])
                elif birth_date.weekday() == 5:
                    weakdays_2['Monday'].append(i['name'])
                elif birth_date.weekday() == 6:
                    weakdays_2['Monday'].append(i['name'])
            else:
                if birth_date.weekday() == 0:
                    weakdays_2['Monday'].append(i['name'])
                elif birth_date.weekday() == 1:
                    weakdays_2['Tuesday'].append(i['name'])
                elif birth_date.weekday() == 2:
                    weakdays_2['Wednesday'].append(i['name'])
                elif birth_date.weekday() == 3:
                    weakdays_2['Thursday'].append(i['name'])
                elif birth_date.weekday() == 4:
                    weakdays_2['Friday'].append(i['name'])
    for k, v in weakdays_1.items():
        v = ', '.join(v)
        if len(v) > 0:
            print(k, ':', v)
    for k, v in weakdays_2.items():
        v = ', '.join(v)
        if len(v) > 0:
            print(k, ':', v)


get_birthdays_per_week(users)
