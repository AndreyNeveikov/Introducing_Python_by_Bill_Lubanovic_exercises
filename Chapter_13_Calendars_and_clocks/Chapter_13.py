#1
import datetime as dt

now = dt.date.today()
print(now)

now_str = now.isoformat()
print(now_str)

with open('today.txt', 'wt') as output:
    print(now_str, file = output)

# 2
with open('today.txt', 'rt') as input:
    today_string = input.read()

print(today_string)


#3
fmt = "%Y-%m-%d\n"

print(dt.datetime.strptime(today_string, fmt))


# 4
class Birthday():
    def __init__(self, birthday):
        self.birthday = birthday


birthday_date = dt.date(2002, 6, 12)
my_birthday = Birthday(birthday_date)

print(my_birthday.birthday)


#5
print("I was born at", my_birthday.birthday.isoweekday(), "rd day of the week Wednesday")


#6
i_will_be_10000_days_old = birthday_date + dt.timedelta(days=10000)
print(i_will_be_10000_days_old)