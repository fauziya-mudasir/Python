import pandas as pd
import datetime
from datetime import timedelta


myDict={}



def timeTracker():
    datetimeFormat =  '%Y-%m-%d %H:%M:%S'
    print("Please enter date and time in format = 'year-month-day time' \n")
    print("An example will be '2016-04-16 13:00:00' \n")
    date = input("Enter date:")
    startTime = input("Enter start time:")
    endTime =input("Enter end time:")
    rate = int(input("Enter your hourly rate:"))
    #using the python built in library datetime, we can calculate the time difference between two dates
    diff = datetime.datetime.strptime(endTime, datetimeFormat)-datetime.datetime.strptime(startTime, datetimeFormat)
    seconds = (diff.seconds)/3600
    days= (diff.days)* 24
    totalHours =  int(seconds + days) 
    print("Your total hours worked is  %d hours" % ( totalHours))
    moneyEarned= totalHours * rate
    myDict[date]=[startTime,endTime,totalHours,moneyEarned]
   
    df = pd.DataFrame.from_dict(myDict, orient='index',
                           columns=['Start_Time', 'End_Time', 'Total_hours', 'Money_earned'])
    df.to_csv("time_tracker.csv")
    return (moneyEarned)

print("Welcome to the time tracker.We help you calculate your earnings based on your total hours of work")
response = input("Do you want to track your time? [Y/N]:")

if response== "Y" :
    moneyEarned = timeTracker()
    print("Your total money earned is $ %d" % (moneyEarned))
    print("Have a nice day")
    
else :
    print("Have a nice day")
