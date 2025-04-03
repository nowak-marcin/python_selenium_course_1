import datetime
from datetime import timedelta

d = datetime.datetime(1984, 4, 22, 15, 00)

print(d)
print('date:', d.date(), 'hour:', d.time())
print(d.year, d.month, d.day)

# https://www.w3schools.com/python/gloss_python_date_format_codes.asp

print(d.strftime("%dnd %B,%Y")) # 22nd April,1984

# actual date:

da = datetime.datetime.now()
print(da.strftime("%Y-%m-%d %H:%M"))
print(da.strftime("%c"))

# add one day:

da1 = da + timedelta(days=1)
print(da1)
