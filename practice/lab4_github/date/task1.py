import datetime

# date_obj = datetime.date(2024, 1, 5)
# time_obj = datetime.time(12, 11, 13, 230000)
# datetime_obj = datetime.datetime(2024, 12, 24, 12, 11 , 13 , 23)

# current_datetime = datetime.datetime.now()

# print(date_obj)
# print(time_obj)
# print(datetime_obj)


current_date = datetime.datetime.now()

five_days_ago = current_date - datetime.timedelta(days=5)

print(current_date.strftime("%d-%m-%y"))
print(five_days_ago.strftime("%d-%m-%y"))