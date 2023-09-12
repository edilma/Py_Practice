from datetime import date
from datetime import time
from datetime import datetime
import timedelta

def count_days(theyear, themonth, theday):
    import calendar
    countOfDays = 0
    listOfWeeks = calendar.monthcalendar(theyear, themonth)
    for week in listOfWeeks:
        if week[theday] != 0:
            countOfDays +=1
    return countOfDays

#print (count_days(2030,12,3))
# today = date.today()
# today2 = today.weekday()

# print (today)
# print (today2)

today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#print("Tomorrow will be "+days[today.weekday()+1])
#print("Tomorrow will be "+days[(today.weekday()+1)])
#print("Tomorrow will be "+days[(today.weekday()+1)%7])

tomorrow = today+timedelta(days=1)
#tomorrow = date(today.year,today.month,today.day+1)
print(tomorrow)