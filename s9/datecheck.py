import datetime
import re
"""time_now=datetime.datetime.now()
print(time_now.hour)
print(time_now.year)
print(time_now.month)
print(time_now.day)
 """
""" 
from datetime import date
anniv=date(2001,11,11)
print(anniv)
print(anniv.year)
print(anniv.month)
print(anniv.day) """
""" now=datetime.datetime.now()
print(now.strftime(" %d/ %m /%y"))
print(now.strftime("%H:%M:%S")) """
""" date="11/01/2001"
dateobj=datetime.datetime.strptime(date,"%d/%m/%Y")
print(dateobj) """
""" from datetime import timedelta
aujourdhui =datetime.date.today() """
#print(aujourdhui+timedelta(days=10))
#print(aujourdhui-timedelta(days=7))
""" d1=datetime.date(1995,11,11)
d2=datetime.date(2002,11,11)
diff=d2-d1
print(d2-d1)
print(diff.days) """
text="la rénuinon est prevue le 11/05/1986 12:20:32"
pattern=r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}"
result=re.search(pattern,text)
print(result.group())
if result:
    dateobje=datetime.datetime.strptime(result.group(),"%d/%m/%Y %M:%H:%S")
    print(dateobje)