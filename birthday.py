"""
birthday.py
Author: Roger Danilek
Credit: 
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
month = month_name[todaymonth]

print(month)
print(todaydate)

name = input("Hello, what is your name? ")
yourmonth = input("Hi "+ name +", what was the name of the month you were born in? ")
year = int(input("And what year were you born in, "+ name +"? "))
day = input("And the day? ")
if (yourmonth == "October" and day == "31"):
    print("You were born on Halloween!")
elif (yourmonth == month) and (day == int(todaydate)):
    print("Happy birthday!")
    
if (yourmonth== "December") or month==("January") or month==("February"):
    season = "winter"
elif (yourmonth== "March") or month==("April") or month==("May"):
    season = "spring"
elif (yourmonth== "June") or month==("July") or month==("August"):
    season = "summer"
elif (yourmonth== "September") or month==("October") or month==("November"):
    season = "fall"
    
if (year<1980):
    decade = "Stone Age"
elif ((year>=1980) and (year<=1989)):
    decade = "eighties"
elif ((year>=1990) and (year<=1999)):
    decade = "nineties"
elif (year>2000):
    decade = "two thousands"
    
print(name + ", you are a "+ season +" baby of the "+ decade+".")

