#import the calendar module
import calendar

#Create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY) # the calendar should start on Sunday
# str = c.formatmonth (2023, 9,0,0)
# print (str)

# TODO: create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# str = hc.formatmonth (2023, 9)
# print (str)

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2023,9):
#     print (i)

  
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#     print(name)

# for name in calendar.day_name:
#     print(name)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Teams meeting will be on: ")
for m in range (1, 13):
    cal = calendar.monthcalendar(2023,m)
    weekOne = cal[0]
    weekTwo = cal[1]
    if weekOne[calendar.FRIDAY] != 0:
        meetday = weekOne[calendar.FRIDAY]
    else:
        meetday = weekTwo[calendar.FRIDAY]
    print(calendar.month_name[m], meetday)



