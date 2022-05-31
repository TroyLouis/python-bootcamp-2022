import datetime as dt
from datetime import date,datetime

mytime = dt.time(2,20)
print(mytime.minute)
print(mytime.hour)
print(mytime)
print(type(mytime))

today = dt.date.today()
print(today)
print(today.month)
print(today.year)
print(today.day)
print(today.ctime())

mydatetime = date(2021,10,3)
print(mydatetime)

mydatetime = mydatetime.replace(year=2020)
print(mydatetime)

date1 = date(2021, 11, 3)
date2 = date(2022, 12, 4)

result = date1 - date2
print(result.days)

datetime1 = datetime(2021,11,3,22,0)

if __name__ == "__main__":
    pass

