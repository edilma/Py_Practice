from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta #timedelta is a duration in time

#We specify how much the time delta last
#print (timedelta(days=365, hours =5, minutes=1))

now = datetime.now()
print ("today is ", now) # date and time

#print today's date one year from now
#print("One year from now it will be ", str (now + timedelta(days=365)))

#print ("In 3 weeks and 2 days it will be: ", (now + timedelta(weeks=3, days=2)))

#time in the past
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("A week ago it was %A %B %d %Y")
# print (s)

#How many days until april fools
today = date.today() #only date
aprilsFools = date(today.year, 4,1)

if aprilsFools<today :
    print("Aprils fool already passed " , ((today-aprilsFools).days), " days ago")
    aprilsFools = aprilsFools.replace(year= today.year + 1)

time_to_apf = aprilsFools - today
print ("It is ", time_to_apf.days , " days until april fools")