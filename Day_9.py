import time
from datetime import datetime
# Exercise 1: Print current date and time in Python
print(time.ctime())
print(datetime.datetime.now())
print(datetime.datetime.now().time())

print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
# ---------------------------------------------------------
# Exercise 2: Convert string into a datetime object
date_string = "Feb 25 2020 4:20PM"
datetime_obj = datetime.strptime(date_string,'%b %d %Y %I:%M%p')
print(datetime_obj)
# ---------------------------------------------------------
# Exercise 3: Subtract a week (7 days)  from a given date in Python
from datetime import timedelta
given_date = datetime(2020, 2, 25)
print(given_date)
res = given_date - timedelta(days=7)
print(res)
# ---------------------------------------------------------
# Exercise 4: Print a date in a the following format 
# Day_name  Day_number  Month_name  Year
given_date = datetime(2020, 2, 25)

print(given_date.strftime("%A %d %B %Y"))
# ---------------------------------------------------------
# Exercise 5: Find the day of the week of a given date
given_date = datetime(2020, 7, 26)

print(given_date.strftime("%A"))

