import datetime

current_date = datetime.datetime.now()

print(current_date) # with
print(current_date.replace(microsecond=0)) # without
