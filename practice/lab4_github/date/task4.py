import datetime

today = datetime.datetime.now()
yestarday = today - datetime.timedelta(days=1)

diff =  yestarday - today

print(abs(int(diff.total_seconds()))) 