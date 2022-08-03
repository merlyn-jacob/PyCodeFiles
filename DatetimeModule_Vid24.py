import datetime

#getting just date
d = datetime.date(2022, 8, 15) #pass the year, month and date
print(d)

#can also get today's date
tday = datetime.date.today()
print(tday)

#can grab just the year or month or day or even weekday from tday
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.weekday()) #this indexes monday as 0 and sunday as 6
print(tday.isoweekday()) #this indexes monday as 1 and sunday as 7

#timedeltas - difference b/w two dates or times

#create a timedelta variable for the number of days as the difference
#date2 = date1 +/- tdelta

tdelta = datetime.timedelta(days = 7)

print(tday + tdelta) #add to todays date to get which date it is 1 week from now
print(tday - tdelta) #subt from todays date to get which date it was 1 week before

#you can also get timedelta by adding/subt dates
#tdelta = date1 +/- date2

#lets say I want to know how many days until my birthday this year

bday = datetime.date(2022, 8, 15)

till_bday = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

#just getting time

t = datetime.time(9, 30, 15, 100000) #input hours,mins,secs,microsecs
print(t)
print(t.hour)

#getting date and time

dt = datetime.datetime(2022, 8, 15, 10, 30, 15, 100000)
print(dt)
print(dt.date())
print(dt.time())

#can also add/subt timedeltas

tdelta = datetime.timedelta(days = 7)
print(dt + tdelta)

tdelta = datetime.timedelta(hours = 12)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now )
print(dt_utcnow)

#today() gives current local date time with timezone as none
#now() also gives current local date time without timezone but here there is an option to set timezone
#utcnow gives us current utc none but timezone is still none

#use pytz package for timezones as it is easier to use

import pytz
dt = datetime.datetime(2022, 8, 15, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
print(dt_utcnow)

#convert one timezone to another

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_mytz = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mytz)


#to find out what to write in timezone
#for tz in pytz.all_timezones:
    #print(tz)

#you cannot directly convert as above a local datetime (without timezone) into another timezone
dt_local = datetime.datetime.now() #this is not timezone aware
print(dt_local) 

#to convert timezone unaware datetime (naive datetime) into another timezone
#first create a variable of the timezone you want to convert naive to

new_tz = pytz.timezone('US/Mountain')

dt_local = new_tz.localize(dt_local)
print(dt_local)

#print dates in specific formats
#strftime - converts datetime to string

print(dt_local.strftime('%B %d, %Y')) #get these format codes from datetime documentation

#print dates that are already in string format
#strptime = converts string to datetime
dt_str = 'August 15, 2022'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

























