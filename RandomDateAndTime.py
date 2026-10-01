import random
import time


def GetRandomDate(startDate, endDate):
    print("printing radnom date between",startDate,"and",endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'


    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate,dateFormat))


    randomTime = startTime + randomGenerator * (endTime - startTime)
    RandomDate = time.strftime(dateFormat,time.localtime(randomTime))
    return RandomDate



print("random date - ",GetRandomDate("1/1/2026", "12/12/2026"))