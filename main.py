from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    current_date = date.today()
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    
    birthdays_per_week = {day: [] for day in weekdays.values()}
    for user in users:
        name = user['name']
        birthday = user['birthday']
        future_birthday = birthday.replace(year=current_date.year)
        
        if future_birthday < current_date:
            future_birthday = future_birthday.replace(year=current_date.year + 1)
        
        if current_date <= future_birthday <= current_date + timedelta(days=7):
            day_of_week = future_birthday.weekday()
            day_name = weekdays[day_of_week]  
            if day_name in ['Saturday', 'Sunday']:
                day_name = 'Monday' 
            birthdays_per_week[day_name].append(name)
  
    birthdays_per_week_res = birthdays_per_week.copy()
    for key, value in birthdays_per_week_res.items():
       if value == []:
        del birthdays_per_week[key]
    print(birthdays_per_week)    
    return birthdays_per_week
    


if __name__ == "__main__":
    users = [
        {'name': 'Maria', "birthday": datetime(1991, 11, 4).date()},
        {'name': 'Ihor', "birthday": datetime(1993, 10, 28).date()},
        {'name': 'Andriy', "birthday": datetime(1989, 11, 2).date()},
        {'name': 'Iryna', "birthday": datetime(1988, 11, 4).date()},
        {'name': 'Mykola', "birthday": datetime(1991, 10, 31).date()},
        {'name': 'Svitlana', "birthday": datetime(1985, 11, 6).date()},
        {'name': 'Olena', "birthday": datetime(1986, 11, 10).date()},
        {'name': 'Alex', "birthday": datetime(1985, 11, 15).date()},
        {'name': 'Viktoria', "birthday": datetime(1995, 11, 7).date()}
        ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
