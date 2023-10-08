import datetime
currentDate=datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

#formatting date with strftime
    #%d is the day of the month
    #%b is the abbreviation for the month
    #%Y is the 4 digit year

print(currentDate.strftime('%d %b,%Y'))

#%b is the month abbreviation
#%B is the full month name
#%y is two digit year
#%a is the day of the week abbreviated
#%A is the day of the week

print(currentDate.strftime('%A %d %B %Y'))


birthday=input("What is your birthday? (MM/DD/YY) ") 
birthdate=datetime.datetime.strptime(birthday,"%m/%d/%Y").date() 
print("Your birth month is "+ birthdate.strftime('%B'))

#why did we list datetime twice?  
#because we are calling the strptime function 
#which is part of the datetime class 
#which is in the datetime module 


nextBirthday=datetime.datetime.strptime('01/06/2024','%m/%d/%Y').date()
currentDate=datetime.date.today() 
#If you subtract two dates you get back the number of days 
#between those dates
difference = nextBirthday - currentDate
print(difference.days)

currentDate=datetime.date.today() 
#timedelta allows you to specify the time 
#to add or subtract from a date 
print(currentDate+datetime.timedelta(days=15)) 
print(currentDate+datetime.timedelta(hours=15))




