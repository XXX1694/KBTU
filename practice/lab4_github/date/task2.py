import datetime

today = datetime.datetime.now()

tomorrow = today + datetime.timedelta(days=1)
yesterday = today - datetime.timedelta(days=1)

print(yesterday.strftime("%d-%m-%y"))
print(today.strftime("%d-%m-%y"))
print(tomorrow.strftime("%d-%m-%y"))
