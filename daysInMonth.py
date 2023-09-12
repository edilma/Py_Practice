from datetime import date
from datetime import time
from datetime import datetime


def main():
    
    desiredDay = input ("Which day of the week do you want to count? ")
    desiredYear = input ("Enter the year ")
    desiredMonth = input ("Enter the month ")
    d = int (desiredDay)
    y =int(desiredYear)
    m = int (desiredMonth)
    thecount = count_days(y,m,d)
    print ("There are ", thecount, " days on the year and months specified")
    

def count_days(theyear, themonth, theday):
    import calendar
    countOfDays = 0
    listOfWeeks = calendar.monthcalendar(theyear, themonth)
    for week in listOfWeeks:
        if week[theday] != 0:
            countOfDays +=1
    return countOfDays


if __name__ ==("__main__"):
    main()