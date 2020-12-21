from datetime import datetime as dt

#time in other locations
#GMT
import pytz


#current time
dt.now()
print(dt.now())

#setting timezone
tz=pytz.timezone("Singapore")
print(dt.now(tz))

#list all timezones
#print(pytz.all_timezones)
print(len(pytz.all_timezones))