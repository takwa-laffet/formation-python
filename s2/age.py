from datetime import date
from dateutil.relativedelta import relativedelta

anee =int(input("donner votre anee de naissance\n"))
mois=int(input("donner votre mois de naissance\n"))
jour=int(input("donner votre jour de naissance\n"))

today =date.today() #date 

if(today.year>=anee or today.month>=mois or today.day>=jour):
        age = relativedelta(today,date(anee , mois , jour))
        print("vous avez",age.years,"ans",age.months,"mois",age.days,"jours")
else:
        print("nous sommes en ",today)