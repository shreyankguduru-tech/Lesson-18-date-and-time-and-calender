from datetime import date, time, datetime

today = date.today()
todayTime = datetime.now()

print ("The current date is", today)

print ("\nthe current time is", todayTime)


print ("\n date components", today.year, today.month, today.day)