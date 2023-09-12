
from datetime import date
from datetime import time
from datetime import datetime

def main():
    # DATE OBJECT 
    # today = date.today() #this gives me a DATE OBJECT yyyy-mm-dd
    # print("Today's date: ", today)
    # print ("today year: ", today.year)
    # print ("today month: ", today.month)
    # print ("today day :", today.day)
    # days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # print ("Today's weekday is: ", days[today.weekday()])

    #DATIME OBJECT
    #
    # today = datetime.now()
    # print("The current day time is ", today) # gives me the object with date and time yyyy-mm-dd HH:MM:SEC.msc
    # # current time
    # t = datetime.time(datetime.now()) #only time
    # print (t)
    
    #Formating time
    now = datetime.now()
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    #print(now.strftime("The current time is: %Y" ,))
    #%a/%A - abbreviated weekday in lowercase (%a) -  %A is the whole day Title case
    #%b/%B - month, Capital for full month
    #print(now.strftime("The current date is: %A %d %B %y" ,))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print (now.strftime("Locale date and time: %c"))

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print (now.strftime("Current time: %I:%M:%S %p")) # 12-Hour:Minute:Second:AM
    print (now.strftime("24-hour time: %H:%M")) # 24-Hour:Minute


if __name__ =="__main__":
    main()