hour=int(input())
minute=int(input())
minute=minute + 15
if minute>59:
    hour + 1
    minute -=60
elif hour >23:
    hour =0
elif minute<10:
    print(str(hour) +":0" + str(minute))
else:
    print(str(hour + ":" +minute))