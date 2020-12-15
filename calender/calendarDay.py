import calendar as cl 
from datetime import datetime as dt 

day=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(day[cl.weekday(dt.now().year,dt.now().month,dt.now().day)])

