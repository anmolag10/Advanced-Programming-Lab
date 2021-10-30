import datetime
now=datetime.datetime.now()
name=input("Enter your name : ")
time5am=now.replace(hour=8,minute=0,second=0,microsecond=0)
time12pm=now.replace(hour=12,minute=0,second=0,microsecond=0)
time6pm=now.replace(hour=18,minute=0,second=0,microsecond=0)
if now>=time5am and now<time12pm:
    print("Good morning ",name)
elif now<time6pm:
    print("Good afternoon ",name)
else:
    print("Good evening ", name)
